"""
Convert BraTS 2021 images from NIfTI to DICOM with metadata that integrates with the NRG_AI pipelines.
"""

# Inputs.
import argparse
import datetime
import os
import pydicom
import tqdm
import nibabel as nib
import numpy as np
from os import path
from pydicom import dataset, uid

# Arguments.
parser = argparse.ArgumentParser()
parser._action_groups.pop()

required = parser.add_argument_group('Required Arguments')
required.add_argument('-i', '--in_dir', type=str, required=True, help='Path to BraTS2021_Training_Data with NIfTI images.')
required.add_argument('-o', '--out_dir', type=str, required=True, help='Path to put the DICOM images in the right format.')

args = parser.parse_args()

if not path.exists(args.out_dir):
    os.mkdir(args.out_dir)

# Functions.
def create_dicom_template(series_descript):
    """
    Create DICOM template to use for NIfTI->DICOM conversion.

    Input:
        series_descript(str): Series description.
    Output:
        ds(FileDataset): DICOM template.
    """
    file_meta = pydicom.Dataset()
    ds = dataset.FileDataset(None, {}, file_meta=file_meta, preamble=b"\0" * 128)

    ds.BitsAllocated = 16
    ds.BitsStored = 16
    ds.ContentDate = str(datetime.date.today()).replace('-', '')
    ds.ContentTime = str(datetime.datetime.now().time()).replace(':', '').split('.')[0]
    ds.HighBit = 15
    ds.ImageOrientationPatient = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0] # Axial.
    ds.Modality = "MR"
    ds.MRAcquisitionType = "2D" # tag [0018,0023] used to get_image_orientation in src/classifier1_metadata.py.
    ds.PatientName = "Test^Firstname"
    ds.PatientID = "123456" 
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.PixelRepresentation = 1
    ds.PixelSpacing = [1.0, 1.0]
    ds.SamplesPerPixel = 1
    ds.SeriesDescription = series_descript
    ds.SeriesInstanceUID = uid.generate_uid()
    ds.SliceThickness = 1.0
    ds.SpacingBetweenSlices = 1.0
    ds.StudyInstanceUID = uid.generate_uid()
    ds.StudyID = "1"

    return ds

if __name__=="__main__":
    # Iterate through the sessions.
    for session_id in tqdm.tqdm(os.listdir(args.in_dir)):
        # Create corresponding output folders.
        if not path.exists(path.join(args.out_dir, session_id)):
            os.mkdir(path.join(args.out_dir, session_id))
        
        # Iterate through session images.
        for nfti_file in os.listdir(path.join(args.in_dir, session_id)):
            # Focus on FLAIR, T1c, and T2, as those sequence types are the only ones needed for feature extraction.
            sequence = nfti_file.split('_')[-1][:-7]
            if sequence == 't1ce': 
                sequence = 't1c'
            if sequence in ['flair','t1c','t2']:
                # Create DICOM template.
                dicom_template = create_dicom_template(sequence.upper())
                
                # Read in image and get data.
                img = nib.load(path.join(args.in_dir, session_id, nfti_file))
                img_data = img.get_fdata()
                img_header = img.header
                origin_x = img_header['qoffset_x']
                origin_y = img_header['qoffset_y']
                origin_z = img_header['qoffset_z']

                # Rotate image.
                try:
                    img_data = np.rot90(np.flip(img_data,axis=1))
                except Exception as e:
                    print(f"Error processing file: {path.join(args.in_dir, session_id, nfti_file)}")
                    print(f"Exception: {e}")

                # Convert to 16 bytes.
                img_data = img_data.astype(np.int16)

                # Create directory for DICOM images.
                if not path.exists(path.join(args.out_dir, session_id, sequence)):
                    os.mkdir(path.join(args.out_dir, session_id, sequence))
                
                # Iterate through slices.
                for i in range(img.shape[2]):
                    dicom_slice = dicom_template.copy()
                    dicom_slice.PixelData = img_data[:,:,i].tobytes()
                    dicom_slice.Rows, dicom_slice.Columns = img.shape[:2]
                    dicom_slice.InstanceNumber = i + 1
                    dicom_slice.ImagePositionPatient = [origin_x, origin_y, origin_z + float(i) * dicom_template.SliceThickness]
                    dicom_slice.SOPInstanceUID = uid.generate_uid()
                    dicom_slice.save_as(path.join(args.out_dir, session_id, sequence, f'slice_{i + 1}.dcm'))

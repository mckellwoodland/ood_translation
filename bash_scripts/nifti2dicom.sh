#!/bin/bash

# Required arguments.
IN="data/BraTS2021_Training_Data/"
OUT="data/BraTS2021_Training_Data_DICOM/"

# Run script.
docker run --rm \
	   -v $(pwd):/workspace \
	   ood_translation python /workspace/python_scripts/nifti2dicom.py \
	   							--in_dir=$IN \
								--out_dir=$OUT 

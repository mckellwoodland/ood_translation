#!/bin/bash

# Required arguments.
IN=""
OUT=""

# Run script.
docker run --rm \
	   -v $(pwd):/workspace \
	   ood_translation python /workspace/python_scripts/nifti2dicom.py \
	   							--in_dir=$IN \
								--out_dir=$OUT 

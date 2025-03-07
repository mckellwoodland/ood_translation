#!/bin/bash

# Required arguments.
IN="data/BraTS2021_Training_Data/BraTS2021_00000/"
OUT="features/BraTS2021_Training_Data/"

# Optional arguments.
CODE="NRG_AI_NeuroOnco_segment/"

# Segmentation.
docker run --rm -v $(pwd)/$IN:/input \
		-v $(pwd)/$OUT:/output_root \
		-v $(pwd)/$OUT/4-segmentation:/output \
		-v $(pwd)/$CODE:/$CODE \
		satrajit2012/nrg_ai_neuroonco_segment:v0 segmentation --docker

# Out-of-Distribution Detection Translation

This repository contains the code utilized to translate OOD detection into clinical applications.

# Translation Applications

## Brain Tumor Segmentation

This project focuses on out-of-distribution detection for a brain tumor segmentation model. 
This model is described in the paper titled "Integrative Imaging Informatics for Cancer Research: Workflow Automation for Neuro-Oncology (I3CR-WANO)" ([paper](https://ascopubs.org/doi/full/10.1200/CCI.22.00177), [preprint](https://arxiv.org/pdf/2210.03151), [supplement](https://ascopubs.org/action/downloadSupplement?doi=10.1200%2FCCI.22.00177&file=DS_CCI.22.00177.pdf))<sup>1</sup>.

### Data

The model was trained on the BraTS 2021 training data.
This data was downloaded from [Kaggle](https://www.kaggle.com/datasets/dschettler8845/brats-2021-task1?resource=download).

### Code

The `NRG_AI_NeuroOnc_preproc` and `NRG_AI_NeuroOnco_segment` submodules were forked from GitHub ([preproc](https://github.com/satrajitgithub/NRG_AI_NeuroOnco_preproc), [segment](https://github.com/satrajitgithub/NRG_AI_NeuroOnco_segment)).

Docker images for these repositories can be pulled as follows:
```
docker pull satrajit2012/nrg_ai_neuroonco_preproc:v0
```
```
docker pull satrajit2012/nrg_ai_neuroonco_segment:v0
```

# References
1. Satrajit Chakrabarty, Syed Amaan Abidi, Mina Mousa, Mahati Mokkarala, Isabelle Hren, Divya Yadav, Matthew Kelsey, Pamela LaMontagne, John Wood, Michael Adams, Yuzhuo Su, Sherry Thorpe, Caroline Chung, Aristeidis Sotiras, Daniel S. Marcus, "Integrative Imaging Informatics for Cancer Research: Workflow Automation for Neuro-oncology (I3CR-WANO)." JCO Clinical Cancer Informatics, no. 7, e2200177, 2023. Available: [https://doi.org/10.1200/CCI.22.00177](https://doi.org/10.1200/CCI.22.00177).

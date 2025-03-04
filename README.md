# Out-of-Distribution Detection Translation

This repository contains the code utilized to translate OOD detection into clinical applications.

# Brain Tumor Segmentation

This project focuses on out-of-distribution detection for a brain tumor segmentation model. 
This model is described in the paper titled "Integrative Imaging Informatics for Cancer Research: Workflow Automation for Neuro-Oncology (I3CR-WANO)" ([paper](https://ascopubs.org/doi/full/10.1200/CCI.22.00177), [preprint](https://arxiv.org/pdf/2210.03151), [supplement](https://ascopubs.org/action/downloadSupplement?doi=10.1200%2FCCI.22.00177&file=DS_CCI.22.00177.pdf))<sup>1</sup>.

## Data

The model was trained on the BraTS 2021<sup>2,3,4,5,6</sup> training data.
This data was downloaded from [Kaggle](https://www.kaggle.com/datasets/dschettler8845/brats-2021-task1?resource=download)<sup>7</sup>.

## Code

The `NRG_AI_NeuroOnc_preproc` and `NRG_AI_NeuroOnco_segment` submodules were forked from GitHub ([preproc](https://github.com/satrajitgithub/NRG_AI_NeuroOnco_preproc), [segment](https://github.com/satrajitgithub/NRG_AI_NeuroOnco_segment)).

Docker images for these repositories can be pulled as follows:
```
docker pull satrajit2012/nrg_ai_neuroonco_preproc:v0
```
```
docker pull satrajit2012/nrg_ai_neuroonco_segment:v0
```

As the BraTS 2021 training data is already organized in NIfTI, the first step (Two-stage scan-type classifiers) was skipped. 
To accomodate this skipping, a `custom_flag.txt` file containing the line `segmentation_ready=true` was placed in the `output_root` file.

# References
1. Satrajit Chakrabarty, Syed Amaan Abidi, Mina Mousa, Mahati Mokkarala, Isabelle Hren, Divya Yadav, Matthew Kelsey, Pamela LaMontagne, John Wood, Michael Adams, Yuzhuo Su, Sherry Thorpe, Caroline Chung, Aristeidis Sotiras, Daniel S. Marcus, "Integrative Imaging Informatics for Cancer Research: Workflow Automation for Neuro-oncology (I3CR-WANO)." JCO Clinical Cancer Informatics, no. 7, e2200177, 2023. Available: [https://doi.org/10.1200/CCI.22.00177](https://doi.org/10.1200/CCI.22.00177).
2. U.Baid, et al., "The RSNA-ASNR-MICCAI BraTS 2021 Benchmark on Brain Tumor Segmentation and Radiogenomic Classification", arXiv:2107.02314, 2021. [https://arxiv.org/abs/2107.02314](https://arxiv.org/abs/2107.02314)
3. B. H. Menze, A. Jakab, S. Bauer, J. Kalpathy-Cramer, K. Farahani, J. Kirby, et al. "The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS)", IEEE Transactions on Medical Imaging 34(10), 1993-2024 (2015) DOI: [10.1109/TMI.2014.2377694 ](https://ieeexplore.ieee.org/document/6975210)
4. S. Bakas, H. Akbari, A. Sotiras, M. Bilello, M. Rozycki, J.S. Kirby, et al., "Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features", Nature Scientific Data, 4:170117 (2017) DOI: [10.1038/sdata.2017.117](https://www.nature.com/articles/sdata2017117)
5. S. Bakas, H. Akbari, A. Sotiras, M. Bilello, M. Rozycki, J. Kirby, et al., "Segmentation Labels and Radiomic Features for the Pre-operative Scans of the TCGA-GBM collection", The Cancer Imaging Archive, 2017. DOI: [10.7937/K9/TCIA.2017.KLXWJJ1Q](https://www.cancerimagingarchive.net/analysis-result/brats-tcga-gbm/)
6. S. Bakas, H. Akbari, A. Sotiras, M. Bilello, M. Rozycki, J. Kirby, et al.,(opens in a new window) "Segmentation Labels and Radiomic Features for the Pre-operative Scans of the TCGA-LGG collection", The Cancer Imaging Archive, 2017. DOI: [10.7937/K9/TCIA.2017.GJQ7R0EF](https://www.cancerimagingarchive.net/analysis-result/brats-tcga-lgg/)
7. Adam Flanders, Christopher Carr, Evan Calabrese, Felipe Kitamura, Jeffrey Rudie, John Mongan, Julia Elliott, Luciano Prevedello, Michelle Riopel, Spyridon Bakas, and Ujjwal Baid. RSNA-MICCAI Brain Tumor Radiogenomic Classification. [https://kaggle.com/competitions/rsna-miccai-brain-tumor-radiogenomic-classification](https://kaggle.com/competitions/rsna-miccai-brain-tumor-radiogenomic-classification), 2021. Kaggle.

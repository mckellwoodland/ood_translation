# Out-of-Distribution Detection Translation

This repository contains the code utilized to translate OOD detection into clinical applications.

# Brain Tumor Segmentation

This project focuses on out-of-distribution (OOD) detection for a brain tumor segmentation model. 
This model is described in the paper titled "Integrative Imaging Informatics for Cancer Research: Workflow Automation for Neuro-Oncology (I3CR-WANO)" ([paper](https://ascopubs.org/doi/full/10.1200/CCI.22.00177), [preprint](https://arxiv.org/pdf/2210.03151), [supplement](https://ascopubs.org/action/downloadSupplement?doi=10.1200%2FCCI.22.00177&file=DS_CCI.22.00177.pdf))<sup>1</sup>.

## Docker

The Docker image for this repository can be built with:
```
docker build --tag ood_translation .
```

Docker images for the `NRG_AI_NeuroOnc_preproc` and `NRG_AI_NeuroOnco_segment` repositories can be pulled as follows:
```
docker pull satrajit2012/nrg_ai_neuroonco_preproc:v0
```
```
docker pull satrajit2012/nrg_ai_neuroonco_segment:v0
```

## Data

The model was trained on the BraTS 2021<sup>2,3,4,5,6</sup> training data.
This data was downloaded from [Kaggle](https://www.kaggle.com/datasets/dschettler8845/brats-2021-task1?resource=download)<sup>7</sup>.

To prepare the BraTS data for I3CR-WANO, the NIfTI images were converted to DICOM.
Only T1-weighted contrast-enhanced, T2-weighted, and FLAIR-weighted MRIs were converted as I3CR-WANO models with T1-weighted MRIs are [not publicly available](https://github.com/satrajitgithub/NRG_AI_NeuroOnco_segment/tree/master/trained_models).
This conversion can be done by providing the required arguments to `nifti2dicom.sh`.
The script will produce an output folder structure consistent with the prerequisites of I3CR-WANO.

```
./bash_scripts/nifti2dicom.sh
```
```
usage: nifti2dicom.py [-h] -i IN_DIR -o OUT_DIR

Required Arguments:
  -i IN_DIR, --in_dir IN_DIR
                        Path to BraTS2021_Training_Data with NIfTI images.
  -o OUT_DIR, --out_dir OUT_DIR
                        Path to put the DICOM images in the right format.
```

The script will throw an exception for `BraTS2021_00466_t1ce.nii.gz`, due to a suspected file corruption.
A corrupted file would be an outlier to the BraTS2021 training distribution.
As outliers can skew feature distances in downstream OOD detection, all three BraTS2021_00466 MRIs were excluded from downstream analysis.

## Code

The `NRG_AI_NeuroOnc_preproc` and `NRG_AI_NeuroOnco_segment` submodules were forked from GitHub ([preproc](https://github.com/satrajitgithub/NRG_AI_NeuroOnco_preproc), [segment](https://github.com/satrajitgithub/NRG_AI_NeuroOnco_segment)).
The forks contains minor updates, including to `tput` to interface with our pipeline.

# References
1. Satrajit Chakrabarty, Syed Amaan Abidi, Mina Mousa, Mahati Mokkarala, Isabelle Hren, Divya Yadav, Matthew Kelsey, Pamela LaMontagne, John Wood, Michael Adams, Yuzhuo Su, Sherry Thorpe, Caroline Chung, Aristeidis Sotiras, Daniel S. Marcus, "Integrative Imaging Informatics for Cancer Research: Workflow Automation for Neuro-oncology (I3CR-WANO)." JCO Clinical Cancer Informatics, no. 7, e2200177, 2023. Available: [https://doi.org/10.1200/CCI.22.00177](https://doi.org/10.1200/CCI.22.00177).
2. U.Baid, et al., "The RSNA-ASNR-MICCAI BraTS 2021 Benchmark on Brain Tumor Segmentation and Radiogenomic Classification", arXiv:2107.02314, 2021. [https://arxiv.org/abs/2107.02314](https://arxiv.org/abs/2107.02314)
3. B. H. Menze, A. Jakab, S. Bauer, J. Kalpathy-Cramer, K. Farahani, J. Kirby, et al. "The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS)", IEEE Transactions on Medical Imaging 34(10), 1993-2024 (2015) DOI: [10.1109/TMI.2014.2377694 ](https://ieeexplore.ieee.org/document/6975210)
4. S. Bakas, H. Akbari, A. Sotiras, M. Bilello, M. Rozycki, J.S. Kirby, et al., "Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features", Nature Scientific Data, 4:170117 (2017) DOI: [10.1038/sdata.2017.117](https://www.nature.com/articles/sdata2017117)
5. S. Bakas, H. Akbari, A. Sotiras, M. Bilello, M. Rozycki, J. Kirby, et al., "Segmentation Labels and Radiomic Features for the Pre-operative Scans of the TCGA-GBM collection", The Cancer Imaging Archive, 2017. DOI: [10.7937/K9/TCIA.2017.KLXWJJ1Q](https://www.cancerimagingarchive.net/analysis-result/brats-tcga-gbm/)
6. S. Bakas, H. Akbari, A. Sotiras, M. Bilello, M. Rozycki, J. Kirby, et al.,(opens in a new window) "Segmentation Labels and Radiomic Features for the Pre-operative Scans of the TCGA-LGG collection", The Cancer Imaging Archive, 2017. DOI: [10.7937/K9/TCIA.2017.GJQ7R0EF](https://www.cancerimagingarchive.net/analysis-result/brats-tcga-lgg/)
7. Adam Flanders, Christopher Carr, Evan Calabrese, Felipe Kitamura, Jeffrey Rudie, John Mongan, Julia Elliott, Luciano Prevedello, Michelle Riopel, Spyridon Bakas, and Ujjwal Baid. RSNA-MICCAI Brain Tumor Radiogenomic Classification. [https://kaggle.com/competitions/rsna-miccai-brain-tumor-radiogenomic-classification](https://kaggle.com/competitions/rsna-miccai-brain-tumor-radiogenomic-classification), 2021. Kaggle.

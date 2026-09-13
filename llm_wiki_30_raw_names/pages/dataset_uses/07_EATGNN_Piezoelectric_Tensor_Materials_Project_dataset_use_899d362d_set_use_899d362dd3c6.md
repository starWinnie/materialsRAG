# 07_EATGNN_Piezoelectric_Tensor - Materials Project

## Dataset Use

A publicly accessible database of computed materials properties, containing DFT-calculated piezoelectric tensors for bulk inorganic crystals. In this paper, it provides bulk piezoelectric tensor data (in Voigt notation) used to train and evaluate the EATGNN model; after outlier removal and symmetry validation, 3444 entries were curated for training/test splits (9:1). The dataset supports the core task of learning symmetry-constrained, frame-independent tensor mappings from crystal structures.

## Links

- Paper: [07 EATGNN Piezoelectric Tensor](../papers/07_EATGNN_Piezoelectric_Tensor_paper_527363b91d18.md)
- Task: [task page](../tasks/07_EATGNN_Piezoelectric_Tensor_task_1_task_413133a497b4.md)
- Dataset: [Materials Project](../datasets/Materials_Project_dataset_d55b16e3041b.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting the complete third-rank piezoelectric stress tensor (eᵢⱼₖ) for crystalline materials — including all 18 independent Voigt components — while respecting crystal symmetry, rotational equivariance, and coordinate-frame independence, to enable accurate characterization of longitudinal, transverse, and shear piezoelectric effects across arbitrary crystallographic orientations.

## Metadata

- Dataset use ID: `dataset_use_899d362dd3c6`
- Original dataset title: Materials Project
- Tags: piezoelectric tensor prediction, equivariant learning, crystal symmetry-aware modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

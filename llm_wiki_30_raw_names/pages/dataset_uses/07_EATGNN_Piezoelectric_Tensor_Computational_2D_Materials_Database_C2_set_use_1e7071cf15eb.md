# 07_EATGNN_Piezoelectric_Tensor - Computational 2D Materials Database (C2DB)

## Dataset Use

A high-throughput computational database containing DFT-derived properties—including piezoelectric tensors—for over 4,000 two-dimensional materials. This paper uses 1350 validated 2D piezoelectric tensor entries (after outlier filtering and symmetry enforcement) to train and test EATGNN on low-dimensional systems. It enables the task of predicting the reduced 3×3 piezoelectric stress tensor for 2D crystals while preserving in-plane rotational equivariance and lattice-symmetry compliance.

## Links

- Paper: [07 EATGNN Piezoelectric Tensor](../papers/07_EATGNN_Piezoelectric_Tensor_paper_527363b91d18.md)
- Task: [task page](../tasks/07_EATGNN_Piezoelectric_Tensor_task_1_task_413133a497b4.md)
- Dataset: [Computational 2D Materials Database (C2DB)](../datasets/Computational_2D_Materials_Database_C2DB_dataset_5e75a39f5247.md)
- Dataset URL: https://c2db.fysik.dtu.dk/

## Task Context

Predicting the complete third-rank piezoelectric stress tensor (eᵢⱼₖ) for crystalline materials — including all 18 independent Voigt components — while respecting crystal symmetry, rotational equivariance, and coordinate-frame independence, to enable accurate characterization of longitudinal, transverse, and shear piezoelectric effects across arbitrary crystallographic orientations.

## Metadata

- Dataset use ID: `dataset_use_1e7071cf15eb`
- Original dataset title: Computational 2D Materials Database (C2DB)
- Tags: piezoelectric tensor prediction, equivariant learning, crystal symmetry-aware modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Problem Definition
- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

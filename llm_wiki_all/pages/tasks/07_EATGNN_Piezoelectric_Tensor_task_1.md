# 07_EATGNN_Piezoelectric_Tensor - Task 1

## Task Description

Predicting the complete third-rank piezoelectric stress tensor (eᵢⱼₖ) for crystalline materials — including all 18 independent Voigt components — while respecting crystal symmetry, rotational equivariance, and coordinate-frame independence, to enable accurate characterization of longitudinal, transverse, and shear piezoelectric effects across arbitrary crystallographic orientations.

## Metadata

- Task ID: `task_413133a497b4`
- Source paper: [07 EATGNN Piezoelectric Tensor](../papers/07_EATGNN_Piezoelectric_Tensor.md)
- Tags: piezoelectric tensor prediction, equivariant learning, crystal symmetry-aware modeling

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/07_EATGNN_Piezoelectric_Tensor_Materials_Project_dataset_use_899d362dd3c6.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org

A publicly accessible database of computed materials properties, containing DFT-calculated piezoelectric tensors for bulk inorganic crystals. In this paper, it provides bulk piezoelectric tensor data (in Voigt notation) used to train and evaluate the EATGNN model; after outlier removal and symmetry validation, 3444 entries were curated for training/test splits (9:1). The dataset supports the core task of learning symmetry-constrained, frame-independent tensor mappings from crystal structures.

### [C2DB](../datasets/C2DB.md)

- Usage page: [usage note](../dataset_uses/07_EATGNN_Piezoelectric_Tensor_C2DB_dataset_use_bd8d17f15f63.md)
- Original title in paper: Computational 2D Materials Database (C2DB)
- Link: https://c2db.fysik.dtu.dk/

A high-throughput computational database containing DFT-derived properties—including piezoelectric tensors—for over 4,000 two-dimensional materials. This paper uses 1350 validated 2D piezoelectric tensor entries (after outlier filtering and symmetry enforcement) to train and test EATGNN on low-dimensional systems. It enables the task of predicting the reduced 3×3 piezoelectric stress tensor for 2D crystals while preserving in-plane rotational equivariance and lattice-symmetry compliance.

### [JARVIS Database](../datasets/JARVIS_Database.md)

- Usage page: [usage note](../dataset_uses/07_EATGNN_Piezoelectric_Tensor_JARVIS_Database_dataset_use_98325f79e378.md)
- Original title in paper: JARVIS Database
- Link: https://jarvis.nist.gov/

The Joint Automated Repository for Various Integrated Simulations (JARVIS) is a DFT-based materials database that includes piezoelectric tensor data derived from high-throughput calculations. The paper explicitly states bulk material data was sourced from both the Materials Project and JARVIS; JARVIS contributes additional piezoelectric tensor entries—particularly from the referenced high-throughput study (Choudhary et al., npj Comput. Mater. 6, 64, 2020)—to expand coverage and improve model generalization for bulk crystal tensor prediction.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

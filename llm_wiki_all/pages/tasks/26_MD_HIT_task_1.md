# 26_MD_HIT - Task 1

## Task Description

Designing and applying a dataset redundancy control method to enable objective, realistic evaluation of machine learning models for material property prediction—specifically by preventing overestimated interpolation performance and improving out-of-distribution (OOD) generalization capability on formation energy and band gap prediction tasks.

## Metadata

- Task ID: `task_e55c8a4f2b28`
- Source paper: [26 MD HIT](../papers/26_MD_HIT.md)
- Tags: redundancy reduction, model evaluation, OOD generalization, material property prediction

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/26_MD_HIT_Materials_Project_dataset_use_12a07aebcb53.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org

A large-scale computational materials database containing 125,619 crystal structures (with 89,354 unique compositions), each annotated with DFT-computed properties including formation energy per atom and band gap. The paper uses the full MP dataset to generate composition-based (86,740 unique compositions) and structure-based (123,108–125,619 CIFs) non-redundant subsets via MD-HIT algorithms; these subsets serve as benchmark datasets for training and evaluating ML models (Roost, CrabNet, ALIGNN, DeeperGATGNN) under controlled redundancy conditions for formation energy and band gap prediction.

### [MatScholar embeddings](../datasets/MatScholar_embeddings.md)

- Usage page: [usage note](../dataset_uses/26_MD_HIT_MatScholar_embeddings_dataset_use_ece85bbe823c.md)
- Original title in paper: MatScholar embeddings
- Link: https://doi.org/10.1038/s41586-019-1312-1

A literature-derived word embedding for materials, generated from text mining of materials science publications, producing fixed-dimensional (e.g., 200D) feature vectors that encode periodic table structure and structure–property relationships. In this paper, MatScholar features are used to compute composition similarity (via Euclidean distance) for redundancy control in MD-HIT-composition, to define the MatscholarOOD test set (1000 most distant samples), and to analyze sample density–MAE correlations—supporting the task of identifying and mitigating redundancy-induced overfitting in composition-based property prediction.

### [Mendeleev similarity metrics](../datasets/Mendeleev_similarity_metrics.md)

- Usage page: [usage note](../dataset_uses/26_MD_HIT_Mendeleev_similarity_metrics_dataset_use_e7ae0cd3e5e4.md)
- Original title in paper: Mendeleev similarity metrics
- Link: https://doi.org/10.1021/acs.chemmater.0c02922

A chemically derived composition similarity measure based on elemental properties (e.g., atomic radius, electronegativity) aligned with Mendeleev’s periodic table principles; implemented in the ElMD package. The paper uses Mendeleev distance to filter the Materials Project composition dataset into seven non-redundant subsets (Mendeleev-nr) with thresholds from 0.5 to 3.0, enabling systematic analysis of how chemical similarity–based redundancy control affects Roost and CrabNet performance on formation energy and band gap prediction.

### [XRD features (from Pymatgen)](../datasets/XRD_features_from_Pymatgen.md)

- Usage page: [usage note](../dataset_uses/26_MD_HIT_XRD_features_from_Pymatgen_dataset_use_e39f8b7257a8.md)
- Original title in paper: XRD features (from Pymatgen)
- Link: https://pymatgen.org

X-ray diffraction (XRD) patterns computed from crystal structures using Pymatgen’s XRDCalculator, smoothed with Gaussian kernel and sampled at 900 evenly spaced 2θ angles (0–90°), yielding fixed-length 900D feature vectors. These features are used in MD-HIT-structure to define structural similarity and generate seven XRD-based non-redundant structure datasets (XRD-nr) for evaluating ALIGNN and DeeperGATGNN on formation energy and band gap prediction under controlled structural redundancy.

### [OFM (Orbital Field Matrix) features](../datasets/OFM_Orbital_Field_Matrix_features.md)

- Usage page: [usage note](../dataset_uses/26_MD_HIT_OFM_Orbital_Field_Matrix_features_dataset_use_02aa41f7bc26.md)
- Original title in paper: OFM (Orbital Field Matrix) features
- Link: https://doi.org/10.1038/s41524-022-00822-2

Fixed-dimension (1024D) descriptors encoding electronic structure information—including electron distribution across atomic orbitals—derived from crystal structures. Used in MD-HIT-structure to compute structural distances and generate eight OFM-based non-redundant datasets (OFM-nr); supports the task of assessing how electronic-structure–driven redundancy control impacts OOD generalization in structure-based band gap and formation energy prediction.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

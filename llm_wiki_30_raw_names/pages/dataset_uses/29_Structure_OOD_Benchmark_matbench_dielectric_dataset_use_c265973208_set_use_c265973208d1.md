# 29_Structure_OOD_Benchmark - matbench_dielectric

## Dataset Use

A dataset of 4,764 inorganic crystals from the Materials Project, each with computed refractive index as the target property. It is used in this paper to construct five OOD test sets (LOCO, SparseXsingle, SparseXcluster, SparseYsingle, SparseYcluster) via structure- and property-based clustering in orbital-field matrix (OFM) feature space; these test sets support evaluating GNNs' ability to predict refractive index for outlier materials located in sparsely populated regions of structural or property space.

## Links

- Paper: [29 Structure OOD Benchmark](../papers/29_Structure_OOD_Benchmark_paper_78a37cf3530b.md)
- Task: [task page](../tasks/29_Structure_OOD_Benchmark_task_1_task_76299946d005.md)
- Dataset: [matbench_dielectric](../datasets/matbench_dielectric_dataset_f5fc3794aeae.md)
- Dataset URL: https://matbench.materialsproject.org/

## Task Context

Predicting materials properties for out-of-distribution (OOD) crystal structures that deviate significantly from the training distribution — specifically, predicting refractive index, shear modulus, and formation energy for sparse, outlier, or structurally/property-remote materials not well-represented in standard datasets. The task focuses on evaluating and benchmarking graph neural networks' ability to generalize beyond i.i.d. assumptions to realistic discovery scenarios where target materials are novel, underrepresented, or lie in low-density regions of structural or property space.

## Metadata

- Dataset use ID: `dataset_use_c265973208d1`
- Original dataset title: matbench_dielectric
- Tags: OOD prediction, materials property prediction, generalization benchmark

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

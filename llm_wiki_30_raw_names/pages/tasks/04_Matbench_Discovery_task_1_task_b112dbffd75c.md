# 04_Matbench_Discovery - Task 1

## Task Description

Predicting the thermodynamic stability of hypothetical inorganic crystal structures by estimating their distance above the convex hull (hull distance) from only unrelaxed input structures, to enable efficient pre-screening before costly DFT relaxation and stability validation.

## Metadata

- Task ID: `task_b112dbffd75c`
- Source paper: [04 Matbench Discovery](../papers/04_Matbench_Discovery_paper_a008eb6410ec.md)
- Tags: crystal stability prediction, convex hull distance estimation, pre-screening for DFT validation

## Supporting Datasets

### [Materials Project (MP) v.2022.10.28](../datasets/Materials_Project_MP_v.2022.10.28_dataset_1fa6a732a3e7.md)

- Usage page: [usage note](../dataset_uses/04_Matbench_Discovery_Materials_Project_MP_v.2022.10.28_dataset_use_4_set_use_448e38964fa7.md)
- Original title in paper: Materials Project (MP) v.2022.10.28
- Link: https://materialsproject.org

A high-throughput DFT-computed database of ~154,719 inorganic crystals, providing relaxed and initial structures, full relaxation trajectories (energies, forces, stresses, magnetic moments at each ionic step), and formation energies. Used as the training set for all models in Matbench Discovery to learn mappings from atomic structure to energy-related properties, supporting the core task of predicting hull distance for stability classification.

### [Wang-Botti-Marques (WBM) dataset](../datasets/Wang-Botti-Marques_WBM_dataset_dataset_c103a7259773.md)

- Usage page: [usage note](../dataset_uses/04_Matbench_Discovery_Wang-Botti-Marques_WBM_dataset_dataset_use_4c12_set_use_4c12b3531b62.md)
- Original title in paper: Wang-Botti-Marques (WBM) dataset
- Link: https://figshare.com/articles/dataset/22715158

A prospectively generated test set of 215,488 unique protostructures derived via chemical similarity-based elemental substitution on MP source structures, followed by DFT relaxation and hull distance calculation against the MP convex hull. Contains unrelaxed input structures and their corresponding DFT-relaxed hull distances (target labels). Used exclusively for evaluating model performance on the stability prediction task under realistic discovery conditions — i.e., predicting stability from unrelaxed inputs without access to relaxation information.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

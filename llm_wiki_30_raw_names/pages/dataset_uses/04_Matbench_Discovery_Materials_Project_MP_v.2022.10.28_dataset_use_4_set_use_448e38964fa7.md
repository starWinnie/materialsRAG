# 04_Matbench_Discovery - Materials Project (MP) v.2022.10.28

## Dataset Use

A high-throughput DFT-computed database of ~154,719 inorganic crystals, providing relaxed and initial structures, full relaxation trajectories (energies, forces, stresses, magnetic moments at each ionic step), and formation energies. Used as the training set for all models in Matbench Discovery to learn mappings from atomic structure to energy-related properties, supporting the core task of predicting hull distance for stability classification.

## Links

- Paper: [04 Matbench Discovery](../papers/04_Matbench_Discovery_paper_a008eb6410ec.md)
- Task: [task page](../tasks/04_Matbench_Discovery_task_1_task_b112dbffd75c.md)
- Dataset: [Materials Project (MP) v.2022.10.28](../datasets/Materials_Project_MP_v.2022.10.28_dataset_1fa6a732a3e7.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting the thermodynamic stability of hypothetical inorganic crystal structures by estimating their distance above the convex hull (hull distance) from only unrelaxed input structures, to enable efficient pre-screening before costly DFT relaxation and stability validation.

## Metadata

- Dataset use ID: `dataset_use_448e38964fa7`
- Original dataset title: Materials Project (MP) v.2022.10.28
- Tags: crystal stability prediction, convex hull distance estimation, pre-screening for DFT validation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Problem Definition
- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

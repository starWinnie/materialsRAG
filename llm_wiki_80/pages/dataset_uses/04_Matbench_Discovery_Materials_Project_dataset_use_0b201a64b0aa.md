# 04_Matbench_Discovery - Materials Project

## Dataset Use

A high-throughput DFT-computed database of ~154,719 inorganic crystals, providing relaxed and initial structures, full relaxation trajectories (energies, forces, stresses, magnetic moments at each ionic step), and formation energies. Used as the training set for all models in Matbench Discovery to learn mappings from atomic structure to energy-related properties, supporting the core task of predicting hull distance for stability classification.

## Links

- Paper: [04 Matbench Discovery](../papers/04_Matbench_Discovery.md)
- Task: [task page](../tasks/04_Matbench_Discovery_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting the thermodynamic stability of hypothetical inorganic crystal structures by estimating their distance above the convex hull (hull distance) from only unrelaxed input structures, to enable efficient pre-screening before costly DFT relaxation and stability validation.

## Metadata

- Dataset use ID: `dataset_use_0b201a64b0aa`
- Original dataset title: Materials Project (MP) v.2022.10.28
- Tags: crystal stability prediction, convex hull distance estimation, pre-screening for DFT validation

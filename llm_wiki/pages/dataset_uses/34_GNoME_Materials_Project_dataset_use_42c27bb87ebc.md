# 34_GNoME - Materials Project

## Dataset Use

A curated database of ~69,000 computationally stable inorganic crystals as of March 2021, containing DFT-calculated total energies, structures (lattice, atomic positions, space groups), and formation energies. This dataset served as the initial training set for GNoME structural models and as the foundational reference for computing decomposition energies during active learning and convex hull updates.

## Links

- Paper: [34 GNoME](../papers/34_GNoME.md)
- Task: [task page](../tasks/34_GNoME_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting the thermodynamic stability of inorganic crystal structures by estimating their decomposition energy relative to the convex hull of competing phases, enabling high-throughput screening and discovery of previously unknown stable materials.

## Metadata

- Dataset use ID: `dataset_use_42c27bb87ebc`
- Original dataset title: Materials Project (2021 snapshot)
- Tags: stability prediction, convex hull analysis, materials discovery, decomposition energy estimation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Optimization / Iteration
<!-- RD_STAGES_END -->

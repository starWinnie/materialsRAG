# 40_ALIGNN - Materials Project

## Dataset Use

A high-throughput DFT database containing 69,239 inorganic crystalline materials with computed properties including PBE band gaps and formation energies. The paper uses the time-versioned MP 2018.6.1 snapshot to train and benchmark ALIGNN regression models on solid-state property prediction tasks, enabling direct comparison with prior GNNs (e.g., SchNet, MEGNet, CGCNN).

## Links

- Paper: [40 ALIGNN](../papers/40_ALIGNN.md)
- Task: [task page](../tasks/40_ALIGNN_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting 52 solid-state and molecular properties—including formation energies, band gaps, dielectric constants, piezoelectric coefficients, Seebeck coefficients, exfoliation energies, HOMO/LUMO levels, dipole moments, and thermodynamic energies—using atomistic graph neural networks that explicitly incorporate bond angle information via line graph message passing.

## Metadata

- Dataset use ID: `dataset_use_f1834d449f10`
- Original dataset title: Materials Project
- Tags: property prediction, regression, classification, bond angle modeling, atomistic representation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

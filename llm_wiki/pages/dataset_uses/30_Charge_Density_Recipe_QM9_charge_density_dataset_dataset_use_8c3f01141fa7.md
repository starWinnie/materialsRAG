# 30_Charge_Density_Recipe - QM9 charge density dataset

## Dataset Use

Contains DFT-calculated charge density voxel data (666,462 grid points per molecule on average) for 133,845 small organic molecules, computed using VASP. The dataset includes atomic coordinates, element types, and ground-truth charge density values on a uniform 3D grid. It is used in this paper to train and evaluate the proposed SCDP models for predicting charge density, with standard train/validation/test splits of 123,835 / 50 / 10,000 samples.

## Links

- Paper: [30 Charge Density Recipe](../papers/30_Charge_Density_Recipe.md)
- Task: [task page](../tasks/30_Charge_Density_Recipe_task_1.md)
- Dataset: [QM9 charge density dataset](../datasets/QM9_charge_density_dataset.md)
- Dataset URL: https://doi.org/10.1038/sdata.2014.22

## Task Context

Predicting the three-dimensional real-space charge density of molecular systems from atomic coordinates and element types, enabling fast and accurate estimation of electronic structure properties without solving the Kohn–Sham equations iteratively.

## Metadata

- Dataset use ID: `dataset_use_8c3f01141fa7`
- Original dataset title: QM9 charge density dataset
- Tags: charge density prediction, electronic structure modeling, DFT acceleration

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

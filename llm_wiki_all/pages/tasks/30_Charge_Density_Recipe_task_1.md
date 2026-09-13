# 30_Charge_Density_Recipe - Task 1

## Task Description

Predicting the three-dimensional real-space charge density of molecular systems from atomic coordinates and element types, enabling fast and accurate estimation of electronic structure properties without solving the Kohn–Sham equations iteratively.

## Metadata

- Task ID: `task_14cc805a3a81`
- Source paper: [30 Charge Density Recipe](../papers/30_Charge_Density_Recipe.md)
- Tags: charge density prediction, electronic structure modeling, DFT acceleration

## Supporting Datasets

### [QM9 charge density dataset](../datasets/QM9_charge_density_dataset.md)

- Usage page: [usage note](../dataset_uses/30_Charge_Density_Recipe_QM9_charge_density_dataset_dataset_use_8c3f01141fa7.md)
- Original title in paper: QM9 charge density dataset
- Link: https://doi.org/10.1038/sdata.2014.22

Contains DFT-calculated charge density voxel data (666,462 grid points per molecule on average) for 133,845 small organic molecules, computed using VASP. The dataset includes atomic coordinates, element types, and ground-truth charge density values on a uniform 3D grid. It is used in this paper to train and evaluate the proposed SCDP models for predicting charge density, with standard train/validation/test splits of 123,835 / 50 / 10,000 samples.

### [MD charge density dataset](../datasets/MD_charge_density_dataset.md)

- Usage page: [usage note](../dataset_uses/30_Charge_Density_Recipe_MD_charge_density_dataset_dataset_use_aa72c2ce7da5.md)
- Original title in paper: MD charge density dataset
- Link: https://doi.org/10.1038/ncomms1572

Contains charge density calculations for six small molecules (ethanol, benzene, phenol, resorcinol, ethane, malonaldehyde) generated via ab initio molecular dynamics simulations. Used in this paper to benchmark SCDP models on dynamic, non-equilibrium molecular structures — specifically to validate generalization beyond static QM9 geometries and assess performance on time-averaged or snapshot charge densities.

### [Cubic charge density dataset](../datasets/Cubic_charge_density_dataset.md)

- Usage page: [usage note](../dataset_uses/30_Charge_Density_Recipe_Cubic_charge_density_dataset_dataset_use_40c7ba65d114.md)
- Original title in paper: Cubic charge density dataset
- Link: https://doi.org/10.1038/s41597-022-00059-9

A large-scale dataset of real-space electronic charge density for 1,000 cubic inorganic materials, computed using DFT. Includes crystalline unit cells, atomic positions, and corresponding 3D charge density grids. In this paper, it is used to evaluate the transferability of the SCDP framework to periodic solids, with virtual nodes placed via Voronoi-based void-filling to adapt the molecular recipe to materials.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->

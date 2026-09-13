# QM9 charge density dataset

## Metadata

- Dataset ID: `dataset_f281b31ea1d7`
- Aliases: QM9 charge density dataset
- Links: https://doi.org/10.1038/sdata.2014.22, https://doi.org/10.11583/DTU.16794500.v1
- Used by papers: 2
- Dataset usage records: 2

## Description Examples

- A dataset of VASP-calculated electron charge densities for 133,845 small organic molecules (with training/validation/test splits of 123,835/50/10,000), derived from the original QM9 molecular database. It contains grid-based charge density values computed at consistent resolution and boundary conditions, and was used to benchmark ChargE3Net’s accuracy on small, isolated molecules — supporting the core task of learning equivariant representations for charge density prediction under molecular symmetry constraints.
- Contains DFT-calculated charge density voxel data (666,462 grid points per molecule on average) for 133,845 small organic molecules, computed using VASP. The dataset includes atomic coordinates, element types, and ground-truth charge density values on a uniform 3D grid. It is used in this paper to train and evaluate the proposed SCDP models for predicting charge density, with standard train/validation/test splits of 123,835 / 50 / 10,000 samples.

## Uses

- [25_ChargE3Net](../dataset_uses/25_ChargE3Net_QM9_charge_density_dataset_dataset_use_91e9b63fe83d.md): [25 ChargE3Net](../papers/25_ChargE3Net.md), [task](../tasks/25_ChargE3Net_task_1.md)
- [30_Charge_Density_Recipe](../dataset_uses/30_Charge_Density_Recipe_QM9_charge_density_dataset_dataset_use_8c3f01141fa7.md): [30 Charge Density Recipe](../papers/30_Charge_Density_Recipe.md), [task](../tasks/30_Charge_Density_Recipe_task_1.md)

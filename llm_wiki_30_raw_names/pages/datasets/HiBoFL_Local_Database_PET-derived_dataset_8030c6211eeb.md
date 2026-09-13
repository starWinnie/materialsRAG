# HiBoFL Local Database (PET-derived)

## Metadata

- Dataset ID: `dataset_8030c6211eeb`
- Aliases: HiBoFL Local Database (PET-derived)
- Links: None
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A custom-built, MongoDB-stored local database containing 661 semiconductors from clusters C1 and C2 (selected via unsupervised learning on the Materials Project data), each annotated with lattice thermal conductivity values (κPET) at 300 K computed using the phonon-elasticity-thermal (PET) empirical model. It includes derived elastic properties (bulk/shear moduli), crystal system, formula type, and elemental composition. This dataset is used to train and validate the supervised CatBoost classifier for ultralow κL prediction (κPET ≤ 2 W/mK), enable statistical analysis of low-κL trends, and prioritize candidates (e.g., Cs2SnSe3, Cs2GeSe3) for first-principles validation.

## Uses

- [08_HiBoFL_Thermal_Conductivity](../dataset_uses/08_HiBoFL_Thermal_Conductivity_HiBoFL_Local_Database_PET-derived_data_set_use_d80d5b12b3a5.md): [08 HiBoFL Thermal Conductivity](../papers/08_HiBoFL_Thermal_Conductivity_paper_cdf2df178098.md), [task](../tasks/08_HiBoFL_Thermal_Conductivity_task_1_task_29d66873e68c.md)

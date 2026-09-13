# 08_HiBoFL_Thermal_Conductivity - HiBoFL Local Database (PET-derived)

## Dataset Use

A custom-built, MongoDB-stored local database containing 661 semiconductors from clusters C1 and C2 (selected via unsupervised learning on the Materials Project data), each annotated with lattice thermal conductivity values (κPET) at 300 K computed using the phonon-elasticity-thermal (PET) empirical model. It includes derived elastic properties (bulk/shear moduli), crystal system, formula type, and elemental composition. This dataset is used to train and validate the supervised CatBoost classifier for ultralow κL prediction (κPET ≤ 2 W/mK), enable statistical analysis of low-κL trends, and prioritize candidates (e.g., Cs2SnSe3, Cs2GeSe3) for first-principles validation.

## Links

- Paper: [08 HiBoFL Thermal Conductivity](../papers/08_HiBoFL_Thermal_Conductivity.md)
- Task: [task page](../tasks/08_HiBoFL_Thermal_Conductivity_task_1.md)
- Dataset: [HiBoFL Local Database (PET-derived)](../datasets/HiBoFL_Local_Database_PET-derived.md)
- Dataset URL: None

## Task Context

Identifying semiconductors with ultralow lattice thermal conductivity (κL) — specifically, screening and classifying candidate materials from a vast chemical space to discover those with κL ≤ 2 W/mK at 300 K for thermoelectric applications, while uncovering interpretable structural and compositional descriptors governing ultralow κL.

## Metadata

- Dataset use ID: `dataset_use_d80d5b12b3a5`
- Original dataset title: HiBoFL Local Database (PET-derived)
- Tags: screening, classifying, discovering, interpreting

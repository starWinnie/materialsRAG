# 08_HiBoFL_Thermal_Conductivity - Task 1

## Task Description

Identifying semiconductors with ultralow lattice thermal conductivity (κL) — specifically, screening and classifying candidate materials from a vast chemical space to discover those with κL ≤ 2 W/mK at 300 K for thermoelectric applications, while uncovering interpretable structural and compositional descriptors governing ultralow κL.

## Metadata

- Task ID: `task_29d66873e68c`
- Source paper: [08 HiBoFL Thermal Conductivity](../papers/08_HiBoFL_Thermal_Conductivity.md)
- Tags: screening, classifying, discovering, interpreting

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/08_HiBoFL_Thermal_Conductivity_Materials_Project_dataset_use_d71c1217c4f4.md)
- Original title in paper: Materials Project (MP) database
- Link: https://next-gen.materialsproject.org/

A publicly available DFT-based high-throughput computational materials database containing over 154,718 entries with thermodynamic, electronic, and structural properties (e.g., formation energy above hull, band gap, crystal structure, unit cell parameters). In this paper, it serves as the primary source for the initial material pool; the authors query it via API and apply thermodynamic stability (Ehull ≤ 0.05 eV/atom), semiconductor band gap (0.1–2 eV), unit cell size (Natoms < 20, Nelements < 4), and elemental constraints (excluding H, lanthanides, actinides) to construct the 2675-material first-level dataset used for unsupervised clustering and feature engineering.

### [HiBoFL Local Database (PET-derived)](../datasets/HiBoFL_Local_Database_PET-derived.md)

- Usage page: [usage note](../dataset_uses/08_HiBoFL_Thermal_Conductivity_HiBoFL_Local_Database_PET-derived_dataset_use_d80d5b12b3a5.md)
- Original title in paper: HiBoFL Local Database (PET-derived)
- Link: None

A custom-built, MongoDB-stored local database containing 661 semiconductors from clusters C1 and C2 (selected via unsupervised learning on the Materials Project data), each annotated with lattice thermal conductivity values (κPET) at 300 K computed using the phonon-elasticity-thermal (PET) empirical model. It includes derived elastic properties (bulk/shear moduli), crystal system, formula type, and elemental composition. This dataset is used to train and validate the supervised CatBoost classifier for ultralow κL prediction (κPET ≤ 2 W/mK), enable statistical analysis of low-κL trends, and prioritize candidates (e.g., Cs2SnSe3, Cs2GeSe3) for first-principles validation.

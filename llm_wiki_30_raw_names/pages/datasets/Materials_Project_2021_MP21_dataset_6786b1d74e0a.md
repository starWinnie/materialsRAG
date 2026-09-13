# Materials Project 2021 (MP21)

## Metadata

- Dataset ID: `dataset_6786b1d74e0a`
- Aliases: Materials Project 2021 (MP21)
- Links: https://materialsproject.org
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A publicly available DFT-computed database of inorganic materials containing 133,785 entries with crystal structures, compositions, and computed physical properties. It provides primary properties (e.g., formation energy per atom, band gap, energy above convex hull, Fermi energy) and secondary properties (e.g., bulk/shear moduli via Voigt-Reuss-Hill approximation, dielectric refractive index, phonon frequencies). In this paper, MP21 is used to train and benchmark the CrysCo model across eight regression tasks—serving as the source for both abundant primary-property data (e.g., ~126k formation energy samples) and scarce secondary-property data (e.g., only ~12k elasticity entries)—and enabling transfer learning from formation energy to mechanical properties.

## Uses

- [13_CrysCo](../dataset_uses/13_CrysCo_Materials_Project_2021_MP21_dataset_use_84fe86fd0bc8_set_use_84fe86fd0bc8.md): [13 CrysCo](../papers/13_CrysCo_paper_f11b018703ad.md), [task](../tasks/13_CrysCo_task_1_task_f54c6e9beff9.md)

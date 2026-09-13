# 35_CHGNet - Task 1

## Task Description

Predicting the potential energy surface of inorganic crystalline materials—including energy, forces, stresses, and magnetic moments—from atomic structure inputs, to enable charge-informed atomistic simulations that capture coupled ionic and electronic degrees of freedom for large-scale, long-time molecular dynamics and thermodynamic modeling.

## Metadata

- Task ID: `task_027f7775466c`
- Source paper: [35 CHGNet](../papers/35_CHGNet.md)
- Tags: potential energy surface prediction, charge-informed simulation, magnetic moment prediction

## Supporting Datasets

### [Materials Project Trajectory Dataset (MPtrj)](../datasets/Materials_Project_Trajectory_Dataset_MPtrj.md)

- Usage page: [usage note](../dataset_uses/35_CHGNet_Materials_Project_Trajectory_Dataset_MPtrj_dataset_use_4c2780d295eb.md)
- Original title in paper: Materials Project Trajectory Dataset (MPtrj)
- Link: https://doi.org/10.6084/m9.figshare.23713842

A dataset comprising 1,580,395 atom configurations sampled from DFT-based structure relaxations and static calculations across ~146,000 inorganic materials, containing corresponding energies, forces (49,295,660), stresses (14,223,555), and magnetic moments (7,944,833). It covers 60 elements with >100,000 occurrences each and includes magmom labels for 76 elements, enabling training of CHGNet to jointly predict energy, forces, stress, and magmoms—thereby supporting the task of learning a universal, charge-aware interatomic potential.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->

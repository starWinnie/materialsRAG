# 35_CHGNet - Materials Project Trajectory Dataset (MPtrj)

## Dataset Use

A dataset comprising 1,580,395 atom configurations sampled from DFT-based structure relaxations and static calculations across ~146,000 inorganic materials, containing corresponding energies, forces (49,295,660), stresses (14,223,555), and magnetic moments (7,944,833). It covers 60 elements with >100,000 occurrences each and includes magmom labels for 76 elements, enabling training of CHGNet to jointly predict energy, forces, stress, and magmoms—thereby supporting the task of learning a universal, charge-aware interatomic potential.

## Links

- Paper: [35 CHGNet](../papers/35_CHGNet.md)
- Task: [task page](../tasks/35_CHGNet_task_1.md)
- Dataset: [Materials Project Trajectory Dataset (MPtrj)](../datasets/Materials_Project_Trajectory_Dataset_MPtrj.md)
- Dataset URL: https://doi.org/10.6084/m9.figshare.23713842

## Task Context

Predicting the potential energy surface of inorganic crystalline materials—including energy, forces, stresses, and magnetic moments—from atomic structure inputs, to enable charge-informed atomistic simulations that capture coupled ionic and electronic degrees of freedom for large-scale, long-time molecular dynamics and thermodynamic modeling.

## Metadata

- Dataset use ID: `dataset_use_4c2780d295eb`
- Original dataset title: Materials Project Trajectory Dataset (MPtrj)
- Tags: potential energy surface prediction, charge-informed simulation, magnetic moment prediction

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

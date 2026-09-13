# 39_M3GNet_Preprint - MPF.2021.2.8

## Dataset Use

A curated dataset derived from structural relaxation trajectories in the Materials Project database, containing 187,687 ionic steps from 62,783 compounds, with corresponding DFT-computed energies (187,687 entries), forces (16,875,138 components), and stresses (1,689,183 components). It spans 89 elements, covers formation energies from −28.7 to 49.6 eV/atom, forces up to ±2570 eV/Å, and stresses up to ±5474 GPa, and includes short interatomic distances (<0.6 Å) critical for learning repulsive interactions. This dataset is used to train the M3GNet interatomic potential to jointly predict energy, force, and stress — essential for physically consistent PES modeling and downstream tasks like structural relaxation and stability screening.

## Links

- Paper: [39 M3GNet Preprint](../papers/39_M3GNet_Preprint.md)
- Task: [task page](../tasks/39_M3GNet_Preprint_task_1.md)
- Dataset: [MPF.2021.2.8](../datasets/MPF.2021.2.8.md)
- Dataset URL: http://doi.org/10.6084/m9.figshare.19470599

## Task Context

Predicting the potential energy surface (PES) of atomic systems—including energies, forces, and stresses—for arbitrary crystalline materials across the entire periodic table, enabling accurate, efficient, and transferable interatomic potentials usable for structural relaxation, molecular dynamics, phonon calculations, and materials discovery without retraining per chemistry.

## Metadata

- Dataset use ID: `dataset_use_e3dc032f25d1`
- Original dataset title: MPF.2021.2.8
- Tags: interatomic potential, energy prediction, force prediction

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

# 39_M3GNet_Preprint - Task 1

## Task Description

Predicting the potential energy surface (PES) of atomic systems—including energies, forces, and stresses—for arbitrary crystalline materials across the entire periodic table, enabling accurate, efficient, and transferable interatomic potentials usable for structural relaxation, molecular dynamics, phonon calculations, and materials discovery without retraining per chemistry.

## Metadata

- Task ID: `task_b799c1746a58`
- Source paper: [39 M3GNet Preprint](../papers/39_M3GNet_Preprint.md)
- Tags: interatomic potential, energy prediction, force prediction

## Supporting Datasets

### [MPF.2021.2.8](../datasets/MPF.2021.2.8.md)

- Usage page: [usage note](../dataset_uses/39_M3GNet_Preprint_MPF.2021.2.8_dataset_use_e3dc032f25d1.md)
- Original title in paper: MPF.2021.2.8
- Link: http://doi.org/10.6084/m9.figshare.19470599

A curated dataset derived from structural relaxation trajectories in the Materials Project database, containing 187,687 ionic steps from 62,783 compounds, with corresponding DFT-computed energies (187,687 entries), forces (16,875,138 components), and stresses (1,689,183 components). It spans 89 elements, covers formation energies from −28.7 to 49.6 eV/atom, forces up to ±2570 eV/Å, and stresses up to ±5474 GPa, and includes short interatomic distances (<0.6 Å) critical for learning repulsive interactions. This dataset is used to train the M3GNet interatomic potential to jointly predict energy, force, and stress — essential for physically consistent PES modeling and downstream tasks like structural relaxation and stability screening.

### [Zuo et al. DFT dataset](../datasets/Zuo_et_al._DFT_dataset.md)

- Usage page: [usage note](../dataset_uses/39_M3GNet_Preprint_Zuo_et_al._DFT_dataset_dataset_use_da81b39a3437.md)
- Original title in paper: Zuo et al. DFT dataset
- Link: None

A benchmark DFT dataset comprising structural relaxations and corresponding energies and forces for six elemental crystals: fcc Ni, fcc Cu, bcc Li, bcc Mo, diamond Si, and diamond Ge. It contains high-fidelity single-point DFT calculations used exclusively for evaluating and comparing the accuracy of the M3GNet interatomic potential against classical (EAM, MEAM) and ML-based (NNP, MTP) potentials — specifically to assess generalization performance on unseen elemental systems not part of the main MPF.2021.2.8 training set.

### [MD17 and MD17-CCSD(T)](../datasets/MD17_and_MD17-CCSD_T.md)

- Usage page: [usage note](../dataset_uses/39_M3GNet_Preprint_MD17_and_MD17-CCSD_T_dataset_use_b132784419e7.md)
- Original title in paper: MD17 and MD17-CCSD(T)
- Link: None

Two molecular dynamics benchmark datasets containing DFT- and quantum-chemical (CCSD/CCSD(T))-level energies and forces for small organic molecules (e.g., aspirin, benzene, ethanol) along their MD trajectories. These datasets contain thousands of conformational snapshots and are used to evaluate M3GNet’s transferability as a molecular force field — specifically to test whether the same architecture, trained on bulk crystals, can accurately predict molecular PES without retraining, supporting its use beyond solids into molecular simulation.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

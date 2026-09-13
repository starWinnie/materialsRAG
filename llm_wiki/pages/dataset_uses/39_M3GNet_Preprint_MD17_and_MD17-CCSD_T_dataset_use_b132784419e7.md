# 39_M3GNet_Preprint - MD17 and MD17-CCSD(T)

## Dataset Use

Two molecular dynamics benchmark datasets containing DFT- and quantum-chemical (CCSD/CCSD(T))-level energies and forces for small organic molecules (e.g., aspirin, benzene, ethanol) along their MD trajectories. These datasets contain thousands of conformational snapshots and are used to evaluate M3GNet’s transferability as a molecular force field — specifically to test whether the same architecture, trained on bulk crystals, can accurately predict molecular PES without retraining, supporting its use beyond solids into molecular simulation.

## Links

- Paper: [39 M3GNet Preprint](../papers/39_M3GNet_Preprint.md)
- Task: [task page](../tasks/39_M3GNet_Preprint_task_1.md)
- Dataset: [MD17 and MD17-CCSD(T)](../datasets/MD17_and_MD17-CCSD_T.md)
- Dataset URL: None

## Task Context

Predicting the potential energy surface (PES) of atomic systems—including energies, forces, and stresses—for arbitrary crystalline materials across the entire periodic table, enabling accurate, efficient, and transferable interatomic potentials usable for structural relaxation, molecular dynamics, phonon calculations, and materials discovery without retraining per chemistry.

## Metadata

- Dataset use ID: `dataset_use_b132784419e7`
- Original dataset title: MD17 and MD17-CCSD(T)
- Tags: interatomic potential, energy prediction, force prediction

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

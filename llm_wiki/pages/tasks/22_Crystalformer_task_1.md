# 22_Crystalformer - Task 1

## Task Description

Predicting multiple physical properties of crystalline materials—including formation energy, bandgap, bulk modulus, shear modulus, total energy, and energy above hull—from their periodic crystal structures represented as unit cells with atomic positions, species, and lattice vectors.

## Metadata

- Task ID: `task_862fa2410163`
- Source paper: [22 Crystalformer](../papers/22_Crystalformer.md)
- Tags: property prediction, crystal structure encoding, regression

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/22_Crystalformer_Materials_Project_dataset_use_d310d33bda1b.md)
- Original title in paper: Materials Project (MEGNet)
- Link: https://materialsproject.org/

A collection of 69,239 DFT-calculated crystalline materials from the Materials Project database, curated by Chen et al. (2019). It contains crystal structures (unit cell coordinates, species, lattice vectors) and associated quantum-mechanically computed properties: formation energy, bandgap, bulk modulus, and shear modulus. In this paper, it is used to train and evaluate Crystalformer for regression on these four properties using consistent train/validation/test splits.

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/22_Crystalformer_JARVIS-DFT_dataset_use_394c5b165816.md)
- Original title in paper: JARVIS-DFT (3D 2021)
- Link: https://jarvis.nist.gov/

A dataset of 55,723 DFT-computed crystalline materials compiled by Choudhary et al. (2020), available via the JARVIS platform. It includes unit-cell structural data (atomic positions, species, lattice vectors) and properties: formation energy, total energy, bandgap (computed with two functionals: OPT and MBJ), and energy above hull (E_hull). The paper uses it for regression benchmarking across five property prediction tasks, following standardized splits established in prior work (e.g., Yan et al., 2022).

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->

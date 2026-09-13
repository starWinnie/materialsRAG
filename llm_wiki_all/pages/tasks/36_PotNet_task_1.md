# 36_PotNet - Task 1

## Task Description

Predicting crystal material properties—specifically total energy, formation energy, band gap, bulk moduli, shear moduli, and Ehull—from atomic-scale crystal structures, with a focus on accurately modeling infinite-range interatomic interactions arising from periodic lattice repetitions.

## Metadata

- Task ID: `task_434ddf370594`
- Source paper: [36 PotNet](../papers/36_PotNet.md)
- Tags: crystal property prediction, interatomic potential modeling, infinite-range interaction prediction

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/36_PotNet_Materials_Project_dataset_use_b0e828c3c53b.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org/

A large-scale computational materials database containing 69,239 crystal structures with DFT-calculated properties including formation energy, band gap, bulk moduli, and shear moduli. In this paper, it is used to train and evaluate PotNet for crystal property prediction, specifically to benchmark performance improvements from using physics-principled interatomic potentials and complete (infinite) potential summations.

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/36_PotNet_JARVIS-DFT_dataset_use_945acdb92eb2.md)
- Original title in paper: JARVIS-DFT
- Link: https://jarvis.nist.gov/

The Joint Automated Repository for Various Integrated Simulations (JARVIS) DFT-2021.8.18 3D dataset, comprising 55,722 crystal structures with DFT-computed properties including formation energy, bandgap (OPT and MBJ), total energy, and Ehull. It is used alongside Materials Project for comprehensive evaluation, ablation studies, and efficiency analysis—serving as the primary testbed for validating PotNet’s ability to capture long-range interactions via complete interatomic potentials.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->

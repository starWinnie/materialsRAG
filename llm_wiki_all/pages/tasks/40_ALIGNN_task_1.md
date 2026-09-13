# 40_ALIGNN - Task 1

## Task Description

Predicting 52 solid-state and molecular properties—including formation energies, band gaps, dielectric constants, piezoelectric coefficients, Seebeck coefficients, exfoliation energies, HOMO/LUMO levels, dipole moments, and thermodynamic energies—using atomistic graph neural networks that explicitly incorporate bond angle information via line graph message passing.

## Metadata

- Task ID: `task_720bfa28c9e0`
- Source paper: [40 ALIGNN](../papers/40_ALIGNN.md)
- Tags: property prediction, regression, classification, bond angle modeling, atomistic representation

## Supporting Datasets

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/40_ALIGNN_JARVIS-DFT_dataset_use_2fedbd6f2004.md)
- Original title in paper: JARVIS-DFT
- Link: https://figshare.com/collections/JARVIS-DFT/4301672

A curated DFT-computed dataset of 55,722 crystalline materials containing 29+ properties including OptB88vdW and TBmBJ band gaps, formation energies, dielectric constants (with/without ionic contributions), bulk/shear moduli, magnetic moments, exfoliation energies for 2D materials, piezoelectric stress/strain coefficients, Seebeck coefficients, power factors, spin-orbit spillage, electric field gradients, and spectroscopic limited maximum efficiency (SLME). Used in this paper to train and evaluate ALIGNN regression and classification models for solid-state property prediction.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/40_ALIGNN_Materials_Project_dataset_use_f1834d449f10.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org

A high-throughput DFT database containing 69,239 inorganic crystalline materials with computed properties including PBE band gaps and formation energies. The paper uses the time-versioned MP 2018.6.1 snapshot to train and benchmark ALIGNN regression models on solid-state property prediction tasks, enabling direct comparison with prior GNNs (e.g., SchNet, MEGNet, CGCNN).

### [QM9](../datasets/QM9.md)

- Usage page: [usage note](../dataset_uses/40_ALIGNN_QM9_dataset_use_e9d1bfae4b5f.md)
- Original title in paper: QM9
- Link: https://doi.org/10.6084/m9.figshare.c.978962

A quantum-chemical dataset of 130,829 small organic molecules with DFT-calculated properties including HOMO/LUMO energies, energy gap, zero-point vibrational energy (ZPVE), dipole moment, isotropic polarizability, electronic spatial extent, and thermodynamic energies (U0, U, H, G) at 0 K and 298 K. Used in this paper to train and evaluate ALIGNN regression models for molecular property prediction, demonstrating generalization across material classes.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
<!-- RD_STAGES_END -->

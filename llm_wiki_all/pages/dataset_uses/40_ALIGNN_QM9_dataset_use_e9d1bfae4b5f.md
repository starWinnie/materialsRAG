# 40_ALIGNN - QM9

## Dataset Use

A quantum-chemical dataset of 130,829 small organic molecules with DFT-calculated properties including HOMO/LUMO energies, energy gap, zero-point vibrational energy (ZPVE), dipole moment, isotropic polarizability, electronic spatial extent, and thermodynamic energies (U0, U, H, G) at 0 K and 298 K. Used in this paper to train and evaluate ALIGNN regression models for molecular property prediction, demonstrating generalization across material classes.

## Links

- Paper: [40 ALIGNN](../papers/40_ALIGNN.md)
- Task: [task page](../tasks/40_ALIGNN_task_1.md)
- Dataset: [QM9](../datasets/QM9.md)
- Dataset URL: https://doi.org/10.6084/m9.figshare.c.978962

## Task Context

Predicting 52 solid-state and molecular properties—including formation energies, band gaps, dielectric constants, piezoelectric coefficients, Seebeck coefficients, exfoliation energies, HOMO/LUMO levels, dipole moments, and thermodynamic energies—using atomistic graph neural networks that explicitly incorporate bond angle information via line graph message passing.

## Metadata

- Dataset use ID: `dataset_use_e9d1bfae4b5f`
- Original dataset title: QM9
- Tags: property prediction, regression, classification, bond angle modeling, atomistic representation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

# 40_ALIGNN - JARVIS-DFT

## Dataset Use

A curated DFT-computed dataset of 55,722 crystalline materials containing 29+ properties including OptB88vdW and TBmBJ band gaps, formation energies, dielectric constants (with/without ionic contributions), bulk/shear moduli, magnetic moments, exfoliation energies for 2D materials, piezoelectric stress/strain coefficients, Seebeck coefficients, power factors, spin-orbit spillage, electric field gradients, and spectroscopic limited maximum efficiency (SLME). Used in this paper to train and evaluate ALIGNN regression and classification models for solid-state property prediction.

## Links

- Paper: [40 ALIGNN](../papers/40_ALIGNN.md)
- Task: [task page](../tasks/40_ALIGNN_task_1.md)
- Dataset: [JARVIS-DFT](../datasets/JARVIS-DFT.md)
- Dataset URL: https://figshare.com/collections/JARVIS-DFT/4301672

## Task Context

Predicting 52 solid-state and molecular properties—including formation energies, band gaps, dielectric constants, piezoelectric coefficients, Seebeck coefficients, exfoliation energies, HOMO/LUMO levels, dipole moments, and thermodynamic energies—using atomistic graph neural networks that explicitly incorporate bond angle information via line graph message passing.

## Metadata

- Dataset use ID: `dataset_use_2fedbd6f2004`
- Original dataset title: JARVIS-DFT
- Tags: property prediction, regression, classification, bond angle modeling, atomistic representation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

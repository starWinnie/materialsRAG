# 02_CFT_Space_Group_Invariance - Materials Project

## Dataset Use

A large-scale computational database of crystalline materials containing over 150,000 entries with calculated properties including total energy (eV/atom), band gap (eV), bulk modulus (log GPa), and shear modulus (log GPa). Each entry includes atomic numbers, fractional atomic coordinates within the unit cell, 3×3 lattice vectors, and space group identifier (1–230). The dataset is used in this paper to train and evaluate the Crystal Fourier Transformer for material property prediction and zero-shot generalization across space groups.

## Links

- Paper: [02 CFT Space Group Invariance](../papers/02_CFT_Space_Group_Invariance.md)
- Task: [task page](../tasks/02_CFT_Space_Group_Invariance_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting key material properties—including total energy, band gap, bulk modulus, and shear modulus—from crystal structures represented by atomic positions, lattice vectors, and space group identifiers, while enforcing exact invariance to the input crystallographic space group without requiring group-specific model architectures.

## Metadata

- Dataset use ID: `dataset_use_2f4d93fd1a7c`
- Original dataset title: Materials Project
- Tags: material property prediction, crystal structure modeling, group-invariant regression

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
<!-- RD_STAGES_END -->

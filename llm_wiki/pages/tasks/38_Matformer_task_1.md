# 38_Matformer - Task 1

## Task Description

Predicting multiple physical and electronic properties of crystalline materials from their atomic structure, including formation energy, band gap, bulk modulus, and shear modulus, using periodic graph representations that respect crystal symmetry and repeating lattice patterns.

## Metadata

- Task ID: `task_9aac42496e6e`
- Source paper: [38 Matformer](../papers/38_Matformer.md)
- Tags: crystal property prediction, materials property prediction, periodic graph learning

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/38_Matformer_Materials_Project_dataset_use_aa99276321ad.md)
- Original title in paper: The Materials Project
- Link: https://materialsproject.org/

A large-scale computational database containing over 130,000+ calculated material structures and properties, derived from density functional theory (DFT) simulations. In this paper, the Materials Project-2018.6.1 subset with 69,239 crystals is used specifically for training and evaluating property predictors on formation energy, band gap, bulk modulus, and shear modulus. The dataset provides unit cell geometry (atomic positions, lattice vectors), composition, and computed scalar properties — and is used to train and benchmark the Matformer model's ability to predict these target properties from periodic crystal graphs.

### [JARVIS Database](../datasets/JARVIS_Database.md)

- Usage page: [usage note](../dataset_uses/38_Matformer_JARVIS_Database_dataset_use_eb07f6f8d169.md)
- Original title in paper: JARVIS (Joint Automated Repository for Various Integrated Simulations)
- Link: https://jarvis.nist.gov/

A curated, DFT-computed materials database containing structural and property data for ~100,000 materials, designed for data-driven materials discovery. In this paper, the JARVIS dataset is used to evaluate Matformer on five tasks: formation energy, optical band gap (OPT), total energy, energy above hull (Ehull), and modified Becke–Johnson (MBJ) band gap. It provides standardized crystal structures (including lattice matrices and atomic coordinates) and associated property labels, supporting validation of periodic invariance and pattern encoding in crystal representation learning.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
<!-- RD_STAGES_END -->

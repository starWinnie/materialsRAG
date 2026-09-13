# 38_Matformer - Materials Project

## Dataset Use

A large-scale computational database containing over 130,000+ calculated material structures and properties, derived from density functional theory (DFT) simulations. In this paper, the Materials Project-2018.6.1 subset with 69,239 crystals is used specifically for training and evaluating property predictors on formation energy, band gap, bulk modulus, and shear modulus. The dataset provides unit cell geometry (atomic positions, lattice vectors), composition, and computed scalar properties — and is used to train and benchmark the Matformer model's ability to predict these target properties from periodic crystal graphs.

## Links

- Paper: [38 Matformer](../papers/38_Matformer.md)
- Task: [task page](../tasks/38_Matformer_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Predicting multiple physical and electronic properties of crystalline materials from their atomic structure, including formation energy, band gap, bulk modulus, and shear modulus, using periodic graph representations that respect crystal symmetry and repeating lattice patterns.

## Metadata

- Dataset use ID: `dataset_use_aa99276321ad`
- Original dataset title: The Materials Project
- Tags: crystal property prediction, materials property prediction, periodic graph learning

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

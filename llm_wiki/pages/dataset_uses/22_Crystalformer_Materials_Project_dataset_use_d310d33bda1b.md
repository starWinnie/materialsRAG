# 22_Crystalformer - Materials Project

## Dataset Use

A collection of 69,239 DFT-calculated crystalline materials from the Materials Project database, curated by Chen et al. (2019). It contains crystal structures (unit cell coordinates, species, lattice vectors) and associated quantum-mechanically computed properties: formation energy, bandgap, bulk modulus, and shear modulus. In this paper, it is used to train and evaluate Crystalformer for regression on these four properties using consistent train/validation/test splits.

## Links

- Paper: [22 Crystalformer](../papers/22_Crystalformer.md)
- Task: [task page](../tasks/22_Crystalformer_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Predicting multiple physical properties of crystalline materials—including formation energy, bandgap, bulk modulus, shear modulus, total energy, and energy above hull—from their periodic crystal structures represented as unit cells with atomic positions, species, and lattice vectors.

## Metadata

- Dataset use ID: `dataset_use_d310d33bda1b`
- Original dataset title: Materials Project (MEGNet)
- Tags: property prediction, crystal structure encoding, regression

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
<!-- RD_STAGES_END -->

# 12_PDDFormer - Materials Project

## Dataset Use

A large-scale computational database containing DFT-calculated structural and property data for over 100,000 inorganic crystalline materials. It includes atomic positions, lattice parameters, space groups, and computed properties such as formation energy, band gap, bulk modulus, and shear modulus. In this paper, it is used to train and evaluate WPDDFormer and UPDDFormer for multi-task crystal property prediction, with reported results on formation energy, band gap, bulk modulus, and shear modulus using log-scaled and linear metrics.

## Links

- Paper: [12 PDDFormer](../papers/12_PDDFormer.md)
- Task: [task page](../tasks/12_PDDFormer_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting multiple physical and electronic properties of crystalline materials—including formation energy, band gap (both OPT and MBJ), total energy, energy above hull (Ehull), bulk modulus, and shear modulus—using machine learning models that operate on crystal structure representations robust to atomic position perturbations and measurement noise.

## Metadata

- Dataset use ID: `dataset_use_248531b22245`
- Original dataset title: Materials Project
- Tags: property prediction, crystal structure representation, robust modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

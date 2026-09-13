# 12_PDDFormer - Task 1

## Task Description

Predicting multiple physical and electronic properties of crystalline materials—including formation energy, band gap (both OPT and MBJ), total energy, energy above hull (Ehull), bulk modulus, and shear modulus—using machine learning models that operate on crystal structure representations robust to atomic position perturbations and measurement noise.

## Metadata

- Task ID: `task_502a51c697a5`
- Source paper: [12 PDDFormer](../papers/12_PDDFormer.md)
- Tags: property prediction, crystal structure representation, robust modeling

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/12_PDDFormer_Materials_Project_dataset_use_248531b22245.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org

A large-scale computational database containing DFT-calculated structural and property data for over 100,000 inorganic crystalline materials. It includes atomic positions, lattice parameters, space groups, and computed properties such as formation energy, band gap, bulk modulus, and shear modulus. In this paper, it is used to train and evaluate WPDDFormer and UPDDFormer for multi-task crystal property prediction, with reported results on formation energy, band gap, bulk modulus, and shear modulus using log-scaled and linear metrics.

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/12_PDDFormer_JARVIS-DFT_dataset_use_f5d6c5ee4833.md)
- Original title in paper: JARVIS-DFT
- Link: https://jarvis.nist.gov

The Joint Automated Repository for Various Integrated Simulations (JARVIS) dataset, which provides DFT-computed properties for ~67,000 experimentally synthesized and hypothetical crystals, including formation energy, band gap (OPT and MBJ), total energy, energy above hull (Ehull), bulk modulus, and shear modulus. The dataset includes Cartesian atomic coordinates, lattice vectors, and symmetry information. In this paper, JARVIS-DFT serves as a benchmark for evaluating predictive accuracy across seven property prediction tasks under identical experimental protocols.

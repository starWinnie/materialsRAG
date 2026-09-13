# 48_Crystal Structure Prediction by Joint Equivariant Diffusion - Carbon-24

## Dataset Use

A dataset of 10,153 carbon-based materials containing 6–24 atoms per unit cell, generated via ab initio random structure searching (AIRSS) at 10 GPa. It includes stable crystal structures (lattice, fractional coordinates, atom types) and is used in this paper to evaluate DiffCSP’s ability to predict complex, variable-size carbon allotropes—serving as a challenging test case for the CSP task due to structural diversity and lack of compositional variation (all carbon).

## Links

- Paper: [48 Crystal Structure Prediction by Joint Equivariant Diffusion](../papers/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion.md)
- Task: [task page](../tasks/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion_task_1.md)
- Dataset: [Carbon-24](../datasets/Carbon-24.md)
- Dataset URL: None

## Task Context

Predicting the stable 3D crystal structure—including the lattice matrix and fractional atomic coordinates—for a given chemical composition, by learning the conditional distribution p(L, F | A) from known stable crystals.

## Metadata

- Dataset use ID: `dataset_use_a536e0f45dd2`
- Original dataset title: Carbon-24
- Tags: Crystal Structure Prediction, Structure Generation, Conditional Generation

# 55_Equivariant Diffusion for Crystal Structure Prediction - Carbon-24

## Dataset Use

A dataset of 10,153 carbon allotropes containing 6–24 atoms per unit cell, featuring multiple metastable structures per composition; used in ab initio generation experiments to evaluate EquiCSP’s ability to sample diverse, physically valid structures from scratch (i.e., without ground-truth reference), supporting the one-to-many structure generation task beyond stable prediction.

## Links

- Paper: [55 Equivariant Diffusion for Crystal Structure Prediction](../papers/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction.md)
- Task: [task page](../tasks/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction_task_1.md)
- Dataset: [Carbon-24](../datasets/Carbon-24.md)
- Dataset URL: https://doi.org/10.5281/zenodo.3727277

## Task Context

Predicting the lattice parameters and fractional atomic coordinates of a crystal structure given its chemical composition, i.e., learning the conditional distribution p(C, F | A) to generate physically valid, stable crystal structures from elemental formulas without relying on expensive DFT-based energy minimization.

## Metadata

- Dataset use ID: `dataset_use_7f9eb73dede4`
- Original dataset title: Carbon-24
- Tags: crystal structure prediction, generative modeling, lattice parameter prediction, fractional coordinate prediction

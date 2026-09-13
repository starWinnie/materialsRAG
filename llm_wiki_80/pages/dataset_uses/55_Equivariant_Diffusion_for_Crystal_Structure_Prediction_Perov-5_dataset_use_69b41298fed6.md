# 55_Equivariant Diffusion for Crystal Structure Prediction - Perov-5

## Dataset Use

A dataset of 18,928 perovskite materials, each with a unit cell containing exactly 5 atoms and analogous structural configurations; used in this paper to train and evaluate EquiCSP on stable structure prediction, with a 60-20-20 train-validation-test split; supports the core CSP task by providing ground-truth (A, C, F) triples for learning the conditional distribution p(C, F | A).

## Links

- Paper: [55 Equivariant Diffusion for Crystal Structure Prediction](../papers/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction.md)
- Task: [task page](../tasks/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction_task_1.md)
- Dataset: [Perov-5](../datasets/Perov-5.md)
- Dataset URL: https://doi.org/10.1039/C2EE22742E

## Task Context

Predicting the lattice parameters and fractional atomic coordinates of a crystal structure given its chemical composition, i.e., learning the conditional distribution p(C, F | A) to generate physically valid, stable crystal structures from elemental formulas without relying on expensive DFT-based energy minimization.

## Metadata

- Dataset use ID: `dataset_use_69b41298fed6`
- Original dataset title: Perov-5
- Tags: crystal structure prediction, generative modeling, lattice parameter prediction, fractional coordinate prediction

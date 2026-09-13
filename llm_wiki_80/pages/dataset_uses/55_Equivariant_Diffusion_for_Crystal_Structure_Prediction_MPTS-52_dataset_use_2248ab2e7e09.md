# 55_Equivariant Diffusion for Crystal Structure Prediction - MPTS-52

## Dataset Use

An extension of MP-20 containing 40,476 crystal structures with up to 52 atoms per unit cell, ordered chronologically by earliest publication year; used as a more challenging benchmark for stable structure prediction, with 27,380 training, 5,000 validation, and 8,096 test entries; tests the scalability and robustness of EquiCSP’s equivariant diffusion framework on larger, more complex crystals.

## Links

- Paper: [55 Equivariant Diffusion for Crystal Structure Prediction](../papers/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction.md)
- Task: [task page](../tasks/55_Equivariant_Diffusion_for_Crystal_Structure_Prediction_task_1.md)
- Dataset: [MPTS-52](../datasets/MPTS-52.md)
- Dataset URL: None

## Task Context

Predicting the lattice parameters and fractional atomic coordinates of a crystal structure given its chemical composition, i.e., learning the conditional distribution p(C, F | A) to generate physically valid, stable crystal structures from elemental formulas without relying on expensive DFT-based energy minimization.

## Metadata

- Dataset use ID: `dataset_use_2248ab2e7e09`
- Original dataset title: MPTS-52
- Tags: crystal structure prediction, generative modeling, lattice parameter prediction, fractional coordinate prediction

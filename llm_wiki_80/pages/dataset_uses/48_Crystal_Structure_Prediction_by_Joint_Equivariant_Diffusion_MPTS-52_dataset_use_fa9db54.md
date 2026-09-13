# 48_Crystal Structure Prediction by Joint Equivariant Diffusion - MPTS-52

## Dataset Use

An extension of MP-20 containing 40,476 crystal structures with up to 52 atoms per unit cell, sorted chronologically by first publication date to enable time-based train/val/test splits. It serves as a more scalable and challenging CSP benchmark in this paper, used to stress-test DiffCSP’s generalization to large-unit-cell systems and validate robustness under increased structural complexity.

## Links

- Paper: [48 Crystal Structure Prediction by Joint Equivariant Diffusion](../papers/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion.md)
- Task: [task page](../tasks/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion_task_1.md)
- Dataset: [MPTS-52](../datasets/MPTS-52.md)
- Dataset URL: https://github.com/sparks-baird/mp-time-split

## Task Context

Predicting the stable 3D crystal structure—including the lattice matrix and fractional atomic coordinates—for a given chemical composition, by learning the conditional distribution p(L, F | A) from known stable crystals.

## Metadata

- Dataset use ID: `dataset_use_fa9db542af22`
- Original dataset title: MPTS-52
- Tags: Crystal Structure Prediction, Structure Generation, Conditional Generation

# 48_Crystal Structure Prediction by Joint Equivariant Diffusion - MP-20

## Dataset Use

A subset of 45,231 stable inorganic materials from the Materials Project database, filtered to include only those with ≤20 atoms per unit cell and experimentally validated or DFT-stable structures. It provides ground-truth crystal structures (lattice, fractional coordinates, composition) and is used in this paper as the primary benchmark for training and evaluating DiffCSP on general inorganic CSP, enabling comparison against DFT-based and learning-based baselines.

## Links

- Paper: [48 Crystal Structure Prediction by Joint Equivariant Diffusion](../papers/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion.md)
- Task: [task page](../tasks/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion_task_1.md)
- Dataset: [MP-20](../datasets/MP-20.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting the stable 3D crystal structure—including the lattice matrix and fractional atomic coordinates—for a given chemical composition, by learning the conditional distribution p(L, F | A) from known stable crystals.

## Metadata

- Dataset use ID: `dataset_use_10056cf71589`
- Original dataset title: MP-20
- Tags: Crystal Structure Prediction, Structure Generation, Conditional Generation

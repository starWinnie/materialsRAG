# 48_Crystal Structure Prediction by Joint Equivariant Diffusion - Perov-5

## Dataset Use

A dataset of 18,928 perovskite materials, each with exactly 5 atoms in the unit cell. It contains stable crystal structures (lattice matrices, fractional coordinates, and atom types) curated from computational screening of perovskite metal oxides. In this paper, it is used to train and evaluate the DiffCSP model for the crystal structure prediction task, specifically to assess performance on compositions with highly symmetric, small-unit-cell structures.

## Links

- Paper: [48 Crystal Structure Prediction by Joint Equivariant Diffusion](../papers/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion.md)
- Task: [task page](../tasks/48_Crystal_Structure_Prediction_by_Joint_Equivariant_Diffusion_task_1.md)
- Dataset: [Perov-5](../datasets/Perov-5.md)
- Dataset URL: None

## Task Context

Predicting the stable 3D crystal structure—including the lattice matrix and fractional atomic coordinates—for a given chemical composition, by learning the conditional distribution p(L, F | A) from known stable crystals.

## Metadata

- Dataset use ID: `dataset_use_278dd7150dc8`
- Original dataset title: Perov-5
- Tags: Crystal Structure Prediction, Structure Generation, Conditional Generation

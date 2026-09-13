# 45_Crystal Diffusion Variational Autoencoder for Periodic Material Generation - Perov-5

## Dataset Use

A curated dataset of 18,928 perovskite materials (ABX₃-type) obtained from DFT-relaxed structures in an open database for water splitting research; all entries share the same structural motif but vary in composition across 56 elements, with exactly 5 atoms per unit cell. It is used to train and evaluate the CDVAE model for reconstructing input structures, generating valid/diverse materials, and optimizing target properties—particularly to assess performance on compositionally diverse yet structurally constrained materials.

## Links

- Paper: [45 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](../papers/45_Crystal_Diffusion_Variational_Autoencoder_for_Periodic_Material_Generation.md)
- Task: [task page](../tasks/45_Crystal_Diffusion_Variational_Autoencoder_for_Periodic_Material_Generation_task_1.md)
- Dataset: [Perov-5](../datasets/Perov-5.md)
- Dataset URL: https://archive.materialscloud.org/record/2012.0001/v1

## Task Context

Generating novel, stable periodic materials represented as atom types, coordinates, and lattice vectors that satisfy quantum-mechanical local energy minima and global bonding preferences—i.e., producing chemically and physically plausible crystal structures de novo without relying on intermediate representations like graphs or voxels.

## Metadata

- Dataset use ID: `dataset_use_844bbc51a505`
- Original dataset title: Perov-5
- Tags: material generation, crystal structure generation, stable material design, de novo crystal synthesis

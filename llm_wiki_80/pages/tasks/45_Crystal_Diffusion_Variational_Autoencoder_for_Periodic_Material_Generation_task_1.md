# 45_Crystal Diffusion Variational Autoencoder for Periodic Material Generation - Task 1

## Task Description

Generating novel, stable periodic materials represented as atom types, coordinates, and lattice vectors that satisfy quantum-mechanical local energy minima and global bonding preferences—i.e., producing chemically and physically plausible crystal structures de novo without relying on intermediate representations like graphs or voxels.

## Metadata

- Task ID: `task_31479bfc0861`
- Source paper: [45 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](../papers/45_Crystal_Diffusion_Variational_Autoencoder_for_Periodic_Material_Generation.md)
- Tags: material generation, crystal structure generation, stable material design, de novo crystal synthesis

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/45_Crystal_Diffusion_Variational_Autoencoder_for_Periodic_Material_Generation_Perov-5_data.md)
- Original title in paper: Perov-5
- Link: https://archive.materialscloud.org/record/2012.0001/v1

A curated dataset of 18,928 perovskite materials (ABX₃-type) obtained from DFT-relaxed structures in an open database for water splitting research; all entries share the same structural motif but vary in composition across 56 elements, with exactly 5 atoms per unit cell. It is used to train and evaluate the CDVAE model for reconstructing input structures, generating valid/diverse materials, and optimizing target properties—particularly to assess performance on compositionally diverse yet structurally constrained materials.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/45_Crystal_Diffusion_Variational_Autoencoder_for_Periodic_Material_Generation_Carbon-24_da.md)
- Original title in paper: Carbon-24
- Link: https://archive.materialscloud.org/record/2020.0026/v1

A dataset of 10,153 carbon-only crystal structures generated via ab initio random structure searching (AIRSS) at 10 GPa and relaxed using DFT; structures contain 6–24 carbon atoms per unit cell and exhibit diverse 3D topologies (e.g., diamond, graphite analogs). It supports evaluation of the model’s ability to generate structurally complex, element-homogeneous materials while respecting bonding preferences and periodic stability constraints.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/45_Crystal_Diffusion_Variational_Autoencoder_for_Periodic_Material_Generation_MP-20_datase.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org

A subset of the Materials Project database containing 45,231 experimentally validated inorganic materials (primarily from ICSD), each with ≤20 atoms per unit cell, spanning 89 elements; structures are DFT-relaxed and filtered for thermodynamic stability (energy above hull < 0.08 eV/atom, formation energy < 2 eV/atom). It serves as the most realistic benchmark for generating synthesizable materials and is used for reconstruction, validity/diversity assessment, and property optimization tasks.

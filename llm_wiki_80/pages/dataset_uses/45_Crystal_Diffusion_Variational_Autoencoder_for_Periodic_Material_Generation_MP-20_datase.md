# 45_Crystal Diffusion Variational Autoencoder for Periodic Material Generation - MP-20

## Dataset Use

A subset of the Materials Project database containing 45,231 experimentally validated inorganic materials (primarily from ICSD), each with ≤20 atoms per unit cell, spanning 89 elements; structures are DFT-relaxed and filtered for thermodynamic stability (energy above hull < 0.08 eV/atom, formation energy < 2 eV/atom). It serves as the most realistic benchmark for generating synthesizable materials and is used for reconstruction, validity/diversity assessment, and property optimization tasks.

## Links

- Paper: [45 Crystal Diffusion Variational Autoencoder for Periodic Material Generation](../papers/45_Crystal_Diffusion_Variational_Autoencoder_for_Periodic_Material_Generation.md)
- Task: [task page](../tasks/45_Crystal_Diffusion_Variational_Autoencoder_for_Periodic_Material_Generation_task_1.md)
- Dataset: [MP-20](../datasets/MP-20.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating novel, stable periodic materials represented as atom types, coordinates, and lattice vectors that satisfy quantum-mechanical local energy minima and global bonding preferences—i.e., producing chemically and physically plausible crystal structures de novo without relying on intermediate representations like graphs or voxels.

## Metadata

- Dataset use ID: `dataset_use_e59ae14c3862`
- Original dataset title: MP-20
- Tags: material generation, crystal structure generation, stable material design, de novo crystal synthesis

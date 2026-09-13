# 49_Towards Symmetry-Aware Generation of Periodic Materials - Task 1

## Task Description

Generating novel periodic material structures with atom types, lattice parameters, and atomic coordinates that satisfy physical symmetry invariances (permutation, rotation, translation, and periodic transformations), enabling downstream applications such as property optimization and inverse design of materials with target characteristics like low energy.

## Metadata

- Task ID: `task_21b0cab6ffdd`
- Source paper: [49 Towards Symmetry-Aware Generation of Periodic Materials](../papers/49_Towards_Symmetry-Aware_Generation_of_Periodic_Materials.md)
- Tags: periodic material generation, symmetry-aware generation, 3D crystal structure generation

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/49_Towards_Symmetry-Aware_Generation_of_Periodic_Materials_Perov-5_dataset_use_2e01c035803.md)
- Original title in paper: Perov-5
- Link: None

A benchmark dataset of 18,928 perovskite materials curated by Xie et al., each conforming to the ABX₃ chemical formula with exactly 5 atoms per unit cell. It contains full 3D crystal structures (atom types, fractional coordinates, and lattice matrices) obtained via DFT simulation. In this paper, Perov-5 is used to train and evaluate SyMat’s ability to generate chemically valid, symmetry-invariant periodic structures — specifically for random generation (validity, distribution matching) and property optimization (energy minimization) tasks.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/49_Towards_Symmetry-Aware_Generation_of_Periodic_Materials_Carbon-24_dataset_use_5bc09e92b.md)
- Original title in paper: Carbon-24
- Link: https://archive.materialscloud.org/record/2020.0026/v1

A dataset of 10,153 carbon-only crystalline structures, each containing 6–24 atoms per unit cell, with 3D atomic coordinates and lattice parameters derived from DFT simulations. All structures consist exclusively of carbon atoms, making composition validity trivial but enabling rigorous evaluation of coordinate and lattice generation fidelity. This dataset supports SyMat’s training and evaluation on symmetry-aware coordinate generation and structural diversity under elemental homogeneity constraints.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/49_Towards_Symmetry-Aware_Generation_of_Periodic_Materials_MP-20_dataset_use_7378a5bbba14.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org

A subset of 45,231 diverse inorganic crystalline materials extracted from the Materials Project database, limited to structures with at most 20 atoms per unit cell. It includes varied compositions, crystal systems, and experimentally or computationally validated 3D structures (lattice matrices, atom types, and coordinates). MP-20 serves as a broad-spectrum benchmark to assess SyMat’s generalizability in symmetry-aware generation across heterogeneous chemical spaces, particularly for random generation quality and property optimization success rates.

# 84_Kinetic Langevin Diffusion for Crystalline Materials Generation - Task 1

## Task Description

Generating novel crystalline materials by predicting atomic fractional coordinates, lattice vectors, and chemical compositions that correspond to physically stable and plausible crystal structures, with explicit handling of periodic translation symmetry inherent in fractional coordinates on a hypertorus.

## Metadata

- Task ID: `task_ac432e5b3a0f`
- Source paper: [84 Kinetic Langevin Diffusion for Crystalline Materials Generation](../papers/84_Kinetic_Langevin_Diffusion_for_Crystalline_Materials_Generation.md)
- Tags: crystal structure generation, fractional coordinate prediction, periodic symmetry modeling

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/84_Kinetic_Langevin_Diffusion_for_Crystalline_Materials_Generation_PEROV-5_dataset_use_89e.md)
- Original title in paper: PEROV-5
- Link: https://doi.org/10.1039/C2EE22746D

A dataset of perovskite materials (ABX3) with exactly 5 atoms per unit cell, all sharing the same crystal structure but differing in chemical composition. It contains 18,928 samples and is used to evaluate Crystal Structure Prediction (CSP) performance—specifically for conditional generation of fractional coordinates and lattice parameters given fixed atomic composition—and to benchmark model robustness on a structurally homogeneous yet compositionally diverse subset of crystalline materials.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/84_Kinetic_Langevin_Diffusion_for_Crystalline_Materials_Generation_MP-20_dataset_use_73adb.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org

A subset of the Materials Project database containing experimentally stable crystalline materials with at most 20 atoms per unit cell. It includes 45,231 samples and is used for both Crystal Structure Prediction (CSP) and De-novo Generation (DNG) tasks: for CSP, it trains and evaluates conditional models p(f, l | a); for DNG, it trains unconditional generative models p(f, l, a), and generated samples are assessed for stability, RMSD, and energy above the convex hull using MATTERGEN’s pipeline and MatterSim-v1-1M.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/84_Kinetic_Langevin_Diffusion_for_Crystalline_Materials_Generation_MPTS-52_dataset_use_674.md)
- Original title in paper: MPTS-52
- Link: https://materialsproject.org

Another Materials Project-derived dataset containing crystalline materials with up to 52 atoms per unit cell (40,476 samples), designed to test scalability and generalization on larger, more complex unit cells. It supports both CSP and DNG evaluation—particularly stressing the model’s ability to handle high-atom-count systems while preserving symmetry-aware diffusion dynamics—and is used to measure match rate (MR) and RMSE in CSP and stability metrics in DNG.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/84_Kinetic_Langevin_Diffusion_for_Crystalline_Materials_Generation_CARBON-24_dataset_use_5.md)
- Original title in paper: CARBON-24
- Link: https://doi.org/10.24435/materialscloud:2020.0026/v1

A dataset of carbon-only crystalline materials with 6–24 atoms per unit cell (10,153 samples), sourced from AirSS random structure searches. It is used to assess CSP performance in a one-to-many compositional setting (where multiple distinct structures satisfy the same C_n formula), enabling evaluation of model diversity and robustness under compositional degeneracy; results are reported for both @1 (best-of-1) and @20 (best-of-20) sampling protocols.

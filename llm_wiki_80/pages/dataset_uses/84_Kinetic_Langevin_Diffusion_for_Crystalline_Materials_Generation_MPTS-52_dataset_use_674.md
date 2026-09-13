# 84_Kinetic Langevin Diffusion for Crystalline Materials Generation - MPTS-52

## Dataset Use

Another Materials Project-derived dataset containing crystalline materials with up to 52 atoms per unit cell (40,476 samples), designed to test scalability and generalization on larger, more complex unit cells. It supports both CSP and DNG evaluation—particularly stressing the model’s ability to handle high-atom-count systems while preserving symmetry-aware diffusion dynamics—and is used to measure match rate (MR) and RMSE in CSP and stability metrics in DNG.

## Links

- Paper: [84 Kinetic Langevin Diffusion for Crystalline Materials Generation](../papers/84_Kinetic_Langevin_Diffusion_for_Crystalline_Materials_Generation.md)
- Task: [task page](../tasks/84_Kinetic_Langevin_Diffusion_for_Crystalline_Materials_Generation_task_1.md)
- Dataset: [MPTS-52](../datasets/MPTS-52.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating novel crystalline materials by predicting atomic fractional coordinates, lattice vectors, and chemical compositions that correspond to physically stable and plausible crystal structures, with explicit handling of periodic translation symmetry inherent in fractional coordinates on a hypertorus.

## Metadata

- Dataset use ID: `dataset_use_6742a9308e45`
- Original dataset title: MPTS-52
- Tags: crystal structure generation, fractional coordinate prediction, periodic symmetry modeling

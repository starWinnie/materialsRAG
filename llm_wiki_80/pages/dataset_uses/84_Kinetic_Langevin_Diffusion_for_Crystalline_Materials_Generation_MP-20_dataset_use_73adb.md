# 84_Kinetic Langevin Diffusion for Crystalline Materials Generation - MP-20

## Dataset Use

A subset of the Materials Project database containing experimentally stable crystalline materials with at most 20 atoms per unit cell. It includes 45,231 samples and is used for both Crystal Structure Prediction (CSP) and De-novo Generation (DNG) tasks: for CSP, it trains and evaluates conditional models p(f, l | a); for DNG, it trains unconditional generative models p(f, l, a), and generated samples are assessed for stability, RMSD, and energy above the convex hull using MATTERGEN’s pipeline and MatterSim-v1-1M.

## Links

- Paper: [84 Kinetic Langevin Diffusion for Crystalline Materials Generation](../papers/84_Kinetic_Langevin_Diffusion_for_Crystalline_Materials_Generation.md)
- Task: [task page](../tasks/84_Kinetic_Langevin_Diffusion_for_Crystalline_Materials_Generation_task_1.md)
- Dataset: [MP-20](../datasets/MP-20.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating novel crystalline materials by predicting atomic fractional coordinates, lattice vectors, and chemical compositions that correspond to physically stable and plausible crystal structures, with explicit handling of periodic translation symmetry inherent in fractional coordinates on a hypertorus.

## Metadata

- Dataset use ID: `dataset_use_73adbad72626`
- Original dataset title: MP-20
- Tags: crystal structure generation, fractional coordinate prediction, periodic symmetry modeling

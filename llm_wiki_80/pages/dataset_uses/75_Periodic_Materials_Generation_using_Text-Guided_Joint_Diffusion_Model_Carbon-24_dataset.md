# 75_Periodic Materials Generation using Text-Guided Joint Diffusion Model - Carbon-24

## Dataset Use

A dataset of 10,153 carbon-only crystal structures, with 6–24 atoms per unit cell, generated via ab initio random structure searching (AIRSS) at 10 GPa. All structures are at local energy minima and share identical composition but vary in geometry. Used in this paper for CSP and Gen tasks to evaluate TGDMat’s text-guided generation fidelity — especially for matching prompts specifying elemental identity (C), crystal system (e.g., orthorhombic), space group number (e.g., 62), and formation energy sign — and to assess structural validity and coverage metrics.

## Links

- Paper: [75 Periodic Materials Generation using Text-Guided Joint Diffusion Model](../papers/75_Periodic_Materials_Generation_using_Text-Guided_Joint_Diffusion_Model.md)
- Task: [task page](../tasks/75_Periodic_Materials_Generation_using_Text-Guided_Joint_Diffusion_Model_task_1.md)
- Dataset: [Carbon-24](../datasets/Carbon-24.md)
- Dataset URL: https://www.materialscloud.org/archive/2020.0026/v1

## Task Context

Generating stable 3D periodic crystal structures (atom types, fractional coordinates, and lattice matrix) that align with user-specified textual descriptions of material properties, composition, symmetry, and structural features — enabling controllable, text-guided inverse design of novel crystalline materials.

## Metadata

- Dataset use ID: `dataset_use_14566cd30a55`
- Original dataset title: Carbon-24
- Tags: crystal structure generation, text-guided generation, inverse materials design

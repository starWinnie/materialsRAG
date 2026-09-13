# 75_Periodic Materials Generation using Text-Guided Joint Diffusion Model - MP-20

## Dataset Use

A subset of 45,231 materials curated from the Materials Project database, each with ≤20 atoms per unit cell and covering diverse chemistries and crystal systems. Includes experimentally known and globally stable inorganic compounds. Used in this paper as the most realistic benchmark for Gen and CSP tasks — to test TGDMat’s ability to generate synthetically plausible structures matching detailed textual prompts (e.g., 'La(NiGe)₂', tetragonal, space group 138, negative formation energy) and to measure correctness against ground-truth global features (formula, space group, band gap).

## Links

- Paper: [75 Periodic Materials Generation using Text-Guided Joint Diffusion Model](../papers/75_Periodic_Materials_Generation_using_Text-Guided_Joint_Diffusion_Model.md)
- Task: [task page](../tasks/75_Periodic_Materials_Generation_using_Text-Guided_Joint_Diffusion_Model_task_1.md)
- Dataset: [MP-20](../datasets/MP-20.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating stable 3D periodic crystal structures (atom types, fractional coordinates, and lattice matrix) that align with user-specified textual descriptions of material properties, composition, symmetry, and structural features — enabling controllable, text-guided inverse design of novel crystalline materials.

## Metadata

- Dataset use ID: `dataset_use_7bca3e7ea62f`
- Original dataset title: MP-20
- Tags: crystal structure generation, text-guided generation, inverse materials design

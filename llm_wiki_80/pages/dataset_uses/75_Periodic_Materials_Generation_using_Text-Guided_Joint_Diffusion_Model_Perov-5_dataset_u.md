# 75_Periodic Materials Generation using Text-Guided Joint Diffusion Model - Perov-5

## Dataset Use

A dataset of 18,928 perovskite materials, each containing exactly 5 atoms in the unit cell and represented as ABX₃ stoichiometries. Structures are derived from quantum mechanical simulations and correspond to local energy minima; most are hypothetical. Used in this paper for both Crystal Structure Prediction (CSP) and Random Material Generation (Gen) tasks — specifically to train and evaluate TGDMat’s ability to generate structures matching textual prompts (e.g., chemical formula, space group 227, cubic system) and to benchmark validity, coverage, and property statistics.

## Links

- Paper: [75 Periodic Materials Generation using Text-Guided Joint Diffusion Model](../papers/75_Periodic_Materials_Generation_using_Text-Guided_Joint_Diffusion_Model.md)
- Task: [task page](../tasks/75_Periodic_Materials_Generation_using_Text-Guided_Joint_Diffusion_Model_task_1.md)
- Dataset: [Perov-5](../datasets/Perov-5.md)
- Dataset URL: https://doi.org/10.1039/C2EE22462J

## Task Context

Generating stable 3D periodic crystal structures (atom types, fractional coordinates, and lattice matrix) that align with user-specified textual descriptions of material properties, composition, symmetry, and structural features — enabling controllable, text-guided inverse design of novel crystalline materials.

## Metadata

- Dataset use ID: `dataset_use_fe438a9ef9ff`
- Original dataset title: Perov-5
- Tags: crystal structure generation, text-guided generation, inverse materials design

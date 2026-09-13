# 85_WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry - Wang-Botti-Marques (WBM) dataset

## Dataset Use

A dataset of 257,000 crystalline materials created by element substitution in structures from the Materials Project; used as the primary training and evaluation set for WYCKOFFDIFF. It provides protostructure-level representations (space group, Wyckoff positions, elemental assignments) required to train the discrete diffusion model to generate symmetry-respecting protostructures and to compute metrics like Fréchet Wrenformer Distance (FWD), novelty, and uniqueness.

## Links

- Paper: [85 WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry](../papers/85_WyckoffDiff_--_A_Generative_Diffusion_Model_for_Crystal_Symmetry.md)
- Task: [task page](../tasks/85_WyckoffDiff_--_A_Generative_Diffusion_Model_for_Crystal_Symmetry_task_1.md)
- Dataset: [Wang-Botti-Marques (WBM) dataset](../datasets/Wang-Botti-Marques_WBM_dataset.md)
- Dataset URL: https://doi.org/10.1038/s41524-020-00481-6

## Task Context

Generating novel, symmetry-compliant crystal protostructures that are thermodynamically stable or lie on/below the convex hull of known stable materials, by modeling Wyckoff position occupancy (element types and counts) conditioned on space group symmetry.

## Metadata

- Dataset use ID: `dataset_use_8694b2c28b01`
- Original dataset title: WBM dataset
- Tags: crystal generation, protostructure design, symmetry-aware generation, materials discovery

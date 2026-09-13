# 85_WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry - Task 1

## Task Description

Generating novel, symmetry-compliant crystal protostructures that are thermodynamically stable or lie on/below the convex hull of known stable materials, by modeling Wyckoff position occupancy (element types and counts) conditioned on space group symmetry.

## Metadata

- Task ID: `task_f62838778e4c`
- Source paper: [85 WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry](../papers/85_WyckoffDiff_--_A_Generative_Diffusion_Model_for_Crystal_Symmetry.md)
- Tags: crystal generation, protostructure design, symmetry-aware generation, materials discovery

## Supporting Datasets

### [Wang-Botti-Marques (WBM) dataset](../datasets/Wang-Botti-Marques_WBM_dataset.md)

- Usage page: [usage note](../dataset_uses/85_WyckoffDiff_--_A_Generative_Diffusion_Model_for_Crystal_Symmetry_Wang-Botti-Marques_WBM.md)
- Original title in paper: WBM dataset
- Link: https://doi.org/10.1038/s41524-020-00481-6

A dataset of 257,000 crystalline materials created by element substitution in structures from the Materials Project; used as the primary training and evaluation set for WYCKOFFDIFF. It provides protostructure-level representations (space group, Wyckoff positions, elemental assignments) required to train the discrete diffusion model to generate symmetry-respecting protostructures and to compute metrics like Fréchet Wrenformer Distance (FWD), novelty, and uniqueness.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/85_WyckoffDiff_--_A_Generative_Diffusion_Model_for_Crystal_Symmetry_Materials_Project_data.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org

A publicly accessible database of computed crystal structures and properties; used jointly with WBM to construct the reference convex hull of thermodynamic stability for evaluating generated materials. Its structures provide ground-truth formation energies and phase diagrams against which the stability (energy above hull) of WYCKOFFDIFF-generated protostructures is benchmarked after realization and DFT validation.

### [Carbon24](../datasets/Carbon24.md)

- Usage page: [usage note](../dataset_uses/85_WyckoffDiff_--_A_Generative_Diffusion_Model_for_Crystal_Symmetry_Carbon24_dataset_use_5.md)
- Original title in paper: Carbon24
- Link: https://archive.materialscloud.org/record/2020.0026/v1

A specialized dataset containing 24 carbon allotropes at 10 GPa, used for an additional ablation experiment to test generalization beyond multi-element systems. It contains only carbon-based structures, enabling evaluation of prototype-level novelty and model robustness on a single-element, high-symmetry system — supporting the task of assessing whether WYCKOFFDIFF can generate structurally novel protostructures even under extreme compositional constraints.

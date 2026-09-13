# Wang-Botti-Marques (WBM) dataset

## Metadata

- Dataset ID: `dataset_c103a7259773`
- Aliases: WBM dataset, Wang-Botti-Marques (WBM) Dataset, Wang-Botti-Marques (WBM) dataset
- Links: https://doi.org/10.1038/s41524-020-00481-6, https://doi.org/10.1038/s41524-021-00012-7, https://figshare.com/articles/dataset/22715158
- Used by papers: 3
- Dataset usage records: 3

## Description Examples

- A prospectively generated test set of 215,488 unique protostructures derived via chemical similarity-based elemental substitution on MP source structures, followed by DFT relaxation and hull distance calculation against the MP convex hull. Contains unrelaxed input structures and their corresponding DFT-relaxed hull distances (target labels). Used exclusively for evaluating model performance on the stability prediction task under realistic discovery conditions — i.e., predicting stability from unrelaxed inputs without access to relaxation information.
- A dataset of 257,000 crystalline materials created by element substitution in structures from the Materials Project; used as the primary training and evaluation set for WYCKOFFDIFF. It provides protostructure-level representations (space group, Wyckoff positions, elemental assignments) required to train the discrete diffusion model to generate symmetry-respecting protostructures and to compute metrics like Fréchet Wrenformer Distance (FWD), novelty, and uniqueness.
- A dataset of 257,487 structures generated via single-element substitutions on Materials Project entries, based on chemical similarity computed from ICSD. It contains stable structures not present in Materials Project and is used as an external test set to evaluate Matra-Genoa’s ability to recover known stable compounds (e.g., in the Al–Ca–Cu ternary space), thereby validating its generalization and inverse design capability beyond the training distribution.

## Uses

- [04_Matbench_Discovery](../dataset_uses/04_Matbench_Discovery_Wang-Botti-Marques_WBM_dataset_dataset_use_4c12b3531b62.md): [04 Matbench Discovery](../papers/04_Matbench_Discovery.md), [task](../tasks/04_Matbench_Discovery_task_1.md)
- [85_WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry](../dataset_uses/85_WyckoffDiff_--_A_Generative_Diffusion_Model_for_Crystal_Symmetry_Wang-Botti-Marques_WBM.md): [85 WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry](../papers/85_WyckoffDiff_--_A_Generative_Diffusion_Model_for_Crystal_Symmetry.md), [task](../tasks/85_WyckoffDiff_--_A_Generative_Diffusion_Model_for_Crystal_Symmetry_task_1.md)
- [96_A generative material transformer using Wyckoff representation](../dataset_uses/96_A_generative_material_transformer_using_Wyckoff_representation_Wang-Botti-Marques_WBM_d.md): [96 A generative material transformer using Wyckoff representation](../papers/96_A_generative_material_transformer_using_Wyckoff_representation.md), [task](../tasks/96_A_generative_material_transformer_using_Wyckoff_representation_task_1.md)

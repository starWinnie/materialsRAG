# 96_A generative material transformer using Wyckoff representation - Task 1

## Task Description

Generating novel, thermodynamically stable inorganic crystal structures by sampling from a hybrid discrete-continuous action space of Wyckoff positions and atomic coordinates, conditioned on proximity to the convex hull (i.e., low energy above hull), while ensuring structural validity, symmetry, uniqueness, and novelty relative to known databases.

## Metadata

- Task ID: `task_c97114379a08`
- Source paper: [96 A generative material transformer using Wyckoff representation](../papers/96_A_generative_material_transformer_using_Wyckoff_representation.md)
- Tags: crystal structure generation, inverse materials design, thermodynamic stability prediction

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/96_A_generative_material_transformer_using_Wyckoff_representation_Materials_Project_datase.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org

An open-access database of ~115,663 DFT-relaxed crystal structures derived primarily from experimentally known compounds, filtered to exclude structures with more than 15 Wyckoff sites and space group 1. It is used as the primary training dataset for Matra-Genoa-MP and jointly with Alexandria for Matra-Genoa-MPAS, providing ground-truth symmetrized crystal structures with associated energies above the convex hull to train the generative transformer model to learn stable compositional and structural patterns.

### [Alexandria Dataset (AS)](../datasets/Alexandria_Dataset_AS.md)

- Usage page: [usage note](../dataset_uses/96_A_generative_material_transformer_using_Wyckoff_representation_Alexandria_Dataset_AS_da.md)
- Original title in paper: Alexandria Dataset (AS)
- Link: https://alexandria.icams.rub.de/pbe/

An open-access database containing 2,553,057 DFT-relaxed crystal structures—including both experimentally known and machine-learning-generated hypothetical compounds—filtered to include only those within 0.250 eV/atom of the convex hull and with ≤15 Wyckoff sites. It is combined with Materials Project to form the MPAS training set (2,668,720 structures) and serves as the reference convex hull for estimating energy-above-hull during evaluation and filtering of generated structures.

### [Wang-Botti-Marques (WBM) dataset](../datasets/Wang-Botti-Marques_WBM_dataset.md)

- Usage page: [usage note](../dataset_uses/96_A_generative_material_transformer_using_Wyckoff_representation_Wang-Botti-Marques_WBM_d.md)
- Original title in paper: Wang-Botti-Marques (WBM) Dataset
- Link: https://doi.org/10.1038/s41524-021-00012-7

A dataset of 257,487 structures generated via single-element substitutions on Materials Project entries, based on chemical similarity computed from ICSD. It contains stable structures not present in Materials Project and is used as an external test set to evaluate Matra-Genoa’s ability to recover known stable compounds (e.g., in the Al–Ca–Cu ternary space), thereby validating its generalization and inverse design capability beyond the training distribution.

### [ORB Dataset](../datasets/ORB_Dataset.md)

- Usage page: [usage note](../dataset_uses/96_A_generative_material_transformer_using_Wyckoff_representation_ORB_Dataset_dataset_use_.md)
- Original title in paper: ORB Dataset
- Link: https://github.com/orbital-materials/orb

A large-scale database of ~72 million crystal structures optimized with the ORBITAL uMLIP, including compounds from Alexandria, chemically substituted variants, and ~5 million PyXtal-generated random structures. Though not used for training, it serves as the authoritative reference for novelty assessment: generated structures are cross-referenced against ORB to filter duplicates and compute the 'novel' component of the S.U.N. (stable, unique, novel) metric.

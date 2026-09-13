# 96_A generative material transformer using Wyckoff representation - Wang-Botti-Marques (WBM) dataset

## Dataset Use

A dataset of 257,487 structures generated via single-element substitutions on Materials Project entries, based on chemical similarity computed from ICSD. It contains stable structures not present in Materials Project and is used as an external test set to evaluate Matra-Genoa’s ability to recover known stable compounds (e.g., in the Al–Ca–Cu ternary space), thereby validating its generalization and inverse design capability beyond the training distribution.

## Links

- Paper: [96 A generative material transformer using Wyckoff representation](../papers/96_A_generative_material_transformer_using_Wyckoff_representation.md)
- Task: [task page](../tasks/96_A_generative_material_transformer_using_Wyckoff_representation_task_1.md)
- Dataset: [Wang-Botti-Marques (WBM) dataset](../datasets/Wang-Botti-Marques_WBM_dataset.md)
- Dataset URL: https://doi.org/10.1038/s41524-021-00012-7

## Task Context

Generating novel, thermodynamically stable inorganic crystal structures by sampling from a hybrid discrete-continuous action space of Wyckoff positions and atomic coordinates, conditioned on proximity to the convex hull (i.e., low energy above hull), while ensuring structural validity, symmetry, uniqueness, and novelty relative to known databases.

## Metadata

- Dataset use ID: `dataset_use_dc1e480f1cfa`
- Original dataset title: Wang-Botti-Marques (WBM) Dataset
- Tags: crystal structure generation, inverse materials design, thermodynamic stability prediction

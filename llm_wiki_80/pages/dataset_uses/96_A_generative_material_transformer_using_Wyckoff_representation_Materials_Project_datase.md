# 96_A generative material transformer using Wyckoff representation - Materials Project

## Dataset Use

An open-access database of ~115,663 DFT-relaxed crystal structures derived primarily from experimentally known compounds, filtered to exclude structures with more than 15 Wyckoff sites and space group 1. It is used as the primary training dataset for Matra-Genoa-MP and jointly with Alexandria for Matra-Genoa-MPAS, providing ground-truth symmetrized crystal structures with associated energies above the convex hull to train the generative transformer model to learn stable compositional and structural patterns.

## Links

- Paper: [96 A generative material transformer using Wyckoff representation](../papers/96_A_generative_material_transformer_using_Wyckoff_representation.md)
- Task: [task page](../tasks/96_A_generative_material_transformer_using_Wyckoff_representation_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating novel, thermodynamically stable inorganic crystal structures by sampling from a hybrid discrete-continuous action space of Wyckoff positions and atomic coordinates, conditioned on proximity to the convex hull (i.e., low energy above hull), while ensuring structural validity, symmetry, uniqueness, and novelty relative to known databases.

## Metadata

- Dataset use ID: `dataset_use_de6652cdcd52`
- Original dataset title: Materials Project (MP)
- Tags: crystal structure generation, inverse materials design, thermodynamic stability prediction

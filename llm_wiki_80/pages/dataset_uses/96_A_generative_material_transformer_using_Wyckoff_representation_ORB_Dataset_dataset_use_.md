# 96_A generative material transformer using Wyckoff representation - ORB Dataset

## Dataset Use

A large-scale database of ~72 million crystal structures optimized with the ORBITAL uMLIP, including compounds from Alexandria, chemically substituted variants, and ~5 million PyXtal-generated random structures. Though not used for training, it serves as the authoritative reference for novelty assessment: generated structures are cross-referenced against ORB to filter duplicates and compute the 'novel' component of the S.U.N. (stable, unique, novel) metric.

## Links

- Paper: [96 A generative material transformer using Wyckoff representation](../papers/96_A_generative_material_transformer_using_Wyckoff_representation.md)
- Task: [task page](../tasks/96_A_generative_material_transformer_using_Wyckoff_representation_task_1.md)
- Dataset: [ORB Dataset](../datasets/ORB_Dataset.md)
- Dataset URL: https://github.com/orbital-materials/orb

## Task Context

Generating novel, thermodynamically stable inorganic crystal structures by sampling from a hybrid discrete-continuous action space of Wyckoff positions and atomic coordinates, conditioned on proximity to the convex hull (i.e., low energy above hull), while ensuring structural validity, symmetry, uniqueness, and novelty relative to known databases.

## Metadata

- Dataset use ID: `dataset_use_d4d41e917008`
- Original dataset title: ORB Dataset
- Tags: crystal structure generation, inverse materials design, thermodynamic stability prediction

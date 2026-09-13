# 96_A generative material transformer using Wyckoff representation - Alexandria Dataset (AS)

## Dataset Use

An open-access database containing 2,553,057 DFT-relaxed crystal structures—including both experimentally known and machine-learning-generated hypothetical compounds—filtered to include only those within 0.250 eV/atom of the convex hull and with ≤15 Wyckoff sites. It is combined with Materials Project to form the MPAS training set (2,668,720 structures) and serves as the reference convex hull for estimating energy-above-hull during evaluation and filtering of generated structures.

## Links

- Paper: [96 A generative material transformer using Wyckoff representation](../papers/96_A_generative_material_transformer_using_Wyckoff_representation.md)
- Task: [task page](../tasks/96_A_generative_material_transformer_using_Wyckoff_representation_task_1.md)
- Dataset: [Alexandria Dataset (AS)](../datasets/Alexandria_Dataset_AS.md)
- Dataset URL: https://alexandria.icams.rub.de/pbe/

## Task Context

Generating novel, thermodynamically stable inorganic crystal structures by sampling from a hybrid discrete-continuous action space of Wyckoff positions and atomic coordinates, conditioned on proximity to the convex hull (i.e., low energy above hull), while ensuring structural validity, symmetry, uniqueness, and novelty relative to known databases.

## Metadata

- Dataset use ID: `dataset_use_b092e133b360`
- Original dataset title: Alexandria Dataset (AS)
- Tags: crystal structure generation, inverse materials design, thermodynamic stability prediction

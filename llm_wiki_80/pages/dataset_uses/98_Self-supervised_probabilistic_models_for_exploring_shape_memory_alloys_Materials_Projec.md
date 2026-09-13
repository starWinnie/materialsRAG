# 98_Self-supervised probabilistic models for exploring shape memory alloys - Materials Project

## Dataset Use

A public database containing ~86,913 computed, unlabeled crystal structures (binary, ternary, and quaternary) of inorganic compounds, filtered to include only stable or metastable structures (formation energy < 0 eV) involving 94 chemical elements. In this paper, it is used exclusively for self-supervised pre-training of the SSL-GNN to learn atomic representations and conditional element probabilities (e.g., P(A|B,X,Y)) without labels — enabling unsupervised knowledge extraction from crystallographic symmetry and local atomic environments.

## Links

- Paper: [98 Self-supervised probabilistic models for exploring shape memory alloys](../papers/98_Self-supervised_probabilistic_models_for_exploring_shape_memory_alloys.md)
- Task: [task page](../tasks/98_Self-supervised_probabilistic_models_for_exploring_shape_memory_alloys_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Discovering novel binary shape memory alloys (SMAs) by predicting compositions that are likely to exhibit the shape memory effect, with a focus on compounds adopting B2, D03, or L12 crystal structures — specifically identifying candidates that are both compositionally plausible and structurally stable for the parent phase, and capable of reversible martensitic transformation.

## Metadata

- Dataset use ID: `dataset_use_fa8a492f6ca8`
- Original dataset title: Materials Project (MP)
- Tags: discovering, screening, predicting

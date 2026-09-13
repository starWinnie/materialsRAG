# 98_Self-supervised probabilistic models for exploring shape memory alloys - Task 1

## Task Description

Discovering novel binary shape memory alloys (SMAs) by predicting compositions that are likely to exhibit the shape memory effect, with a focus on compounds adopting B2, D03, or L12 crystal structures — specifically identifying candidates that are both compositionally plausible and structurally stable for the parent phase, and capable of reversible martensitic transformation.

## Metadata

- Task ID: `task_58722041a565`
- Source paper: [98 Self-supervised probabilistic models for exploring shape memory alloys](../papers/98_Self-supervised_probabilistic_models_for_exploring_shape_memory_alloys.md)
- Tags: discovering, screening, predicting

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/98_Self-supervised_probabilistic_models_for_exploring_shape_memory_alloys_Materials_Projec.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org

A public database containing ~86,913 computed, unlabeled crystal structures (binary, ternary, and quaternary) of inorganic compounds, filtered to include only stable or metastable structures (formation energy < 0 eV) involving 94 chemical elements. In this paper, it is used exclusively for self-supervised pre-training of the SSL-GNN to learn atomic representations and conditional element probabilities (e.g., P(A|B,X,Y)) without labels — enabling unsupervised knowledge extraction from crystallographic symmetry and local atomic environments.

### [Custom SMA Binary Classification Dataset](../datasets/Custom_SMA_Binary_Classification_Dataset.md)

- Usage page: [usage note](../dataset_uses/98_Self-supervised_probabilistic_models_for_exploring_shape_memory_alloys_Custom_SMA_Binar.md)
- Original title in paper: Custom SMA Binary Classification Dataset
- Link: None

A manually curated, labeled dataset of 871 binary alloy compositions: 658 experimentally or theoretically confirmed shape memory alloys (SMAs) and 213 non-SMA alloys, compiled from literature sources (e.g., references 41–50). It includes stoichiometric compositions (primarily 1:1 and 1:3) and binary class labels (SMA / not SMA). This dataset is used to train and evaluate the downstream composition-only SMA classifier, which leverages SSPM atomic representations to predict SMA candidacy.

### [Inorganic Crystal Structure Database](../datasets/Inorganic_Crystal_Structure_Database.md)

- Usage page: [usage note](../dataset_uses/98_Self-supervised_probabilistic_models_for_exploring_shape_memory_alloys_Inorganic_Crysta.md)
- Original title in paper: ICSD (Inorganic Crystal Structure Database)
- Link: https://icsd.fiz-karlsruhe.de

A repository of experimentally determined crystal structures. In this paper, ICSD is cited as the source of experimentally validated lattice parameters (e.g., for TiNi, CuZr, RuNb in Fig. 5C) used to benchmark the accuracy of SSPM’s predicted lattice parameters p(X|A,B,Y) for B2, D03, and L12 structures. It supports validation of structural predictions but is not used for model training.

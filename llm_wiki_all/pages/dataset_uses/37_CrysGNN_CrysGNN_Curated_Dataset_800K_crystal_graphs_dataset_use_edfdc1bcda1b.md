# 37_CrysGNN - CrysGNN Curated Dataset (800K crystal graphs)

## Dataset Use

An author-curated, unlabeled dataset of 800,000 crystal graphs assembled from OQMD (661K) and Materials Project (139K), represented as multi-graphs with node features (electronegativity, valence electrons, covalent radius), edge features (bond lengths), space group numbers, and crystal system labels. Used exclusively for self-supervised pre-training of CrysGNN via node-level reconstruction (features & connectivity) and graph-level objectives (space group classification and contrastive learning over crystal systems).

## Links

- Paper: [37 CrysGNN](../papers/37_CrysGNN.md)
- Task: [task page](../tasks/37_CrysGNN_task_1.md)
- Dataset: [CrysGNN Curated Dataset (800K crystal graphs)](../datasets/CrysGNN_Curated_Dataset_800K_crystal_graphs.md)
- Dataset URL: https://github.com/kdmsit/crysgnn

## Task Context

Predicting multiple physical and electronic properties of crystalline materials—including formation energy, bandgap, total energy, bulk modulus, shear modulus, Ehull, spillage, SLME, and dielectric-related properties—using graph neural network models enhanced by distilled knowledge from a pre-trained GNN on unlabeled crystal structures.

## Metadata

- Dataset use ID: `dataset_use_edfdc1bcda1b`
- Original dataset title: CrysGNN Curated Dataset (800K crystal graphs)
- Tags: property prediction, crystal structure modeling, knowledge distillation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

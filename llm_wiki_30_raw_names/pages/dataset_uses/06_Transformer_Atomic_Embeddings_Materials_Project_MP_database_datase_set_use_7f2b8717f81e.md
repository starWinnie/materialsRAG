# 06_Transformer_Atomic_Embeddings - Materials Project (MP*) database

## Dataset Use

The 2023.6.23 version contains 134,243 materials with formation energy and PBE bandgap; used as the primary large-scale dataset to pretrain the CrystalTransformer front-end model for generating universal atomic embeddings (ct-UAEs). Split into 80% training, 10% validation, and 10% testing sets, it enables multi-task pretraining (e.g., Ef + Eg, Ef + Eg + total energy + magnetization) and supports the task of learning transferable, physics-informed atomic representations independent of predefined features.

## Links

- Paper: [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings_paper_dd99eeb08a7c.md)
- Task: [task page](../tasks/06_Transformer_Atomic_Embeddings_task_1_task_337f2d813b5e.md)
- Dataset: [Materials Project (MP*) database](../datasets/Materials_Project_MP_database_dataset_87d101d436e7.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating universal atomic embeddings that serve as transferable, task-agnostic atomic fingerprints to improve the accuracy of machine learning models predicting crystal properties—including formation energy, bandgap, total energy, and total magnetization—across diverse material systems and data-scarce domains such as hybrid organic-inorganic perovskites.

## Metadata

- Dataset use ID: `dataset_use_7f2b8717f81e`
- Original dataset title: Materials Project (MP*) database
- Tags: atomic embedding, crystal property prediction, transfer learning

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

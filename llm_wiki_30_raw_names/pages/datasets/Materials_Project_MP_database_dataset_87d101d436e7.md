# Materials Project (MP*) database

## Metadata

- Dataset ID: `dataset_87d101d436e7`
- Aliases: Materials Project (MP*) database
- Links: https://materialsproject.org
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- The 2023.6.23 version contains 134,243 materials with formation energy and PBE bandgap; used as the primary large-scale dataset to pretrain the CrystalTransformer front-end model for generating universal atomic embeddings (ct-UAEs). Split into 80% training, 10% validation, and 10% testing sets, it enables multi-task pretraining (e.g., Ef + Eg, Ef + Eg + total energy + magnetization) and supports the task of learning transferable, physics-informed atomic representations independent of predefined features.

## Uses

- [06_Transformer_Atomic_Embeddings](../dataset_uses/06_Transformer_Atomic_Embeddings_Materials_Project_MP_database_datase_set_use_7f2b8717f81e.md): [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings_paper_dd99eeb08a7c.md), [task](../tasks/06_Transformer_Atomic_Embeddings_task_1_task_337f2d813b5e.md)

# 06_Transformer_Atomic_Embeddings - Task 1

## Task Description

Generating universal atomic embeddings that serve as transferable, task-agnostic atomic fingerprints to improve the accuracy of machine learning models predicting crystal properties—including formation energy, bandgap, total energy, and total magnetization—across diverse material systems and data-scarce domains such as hybrid organic-inorganic perovskites.

## Metadata

- Task ID: `task_337f2d813b5e`
- Source paper: [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings.md)
- Tags: atomic embedding, crystal property prediction, transfer learning

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/06_Transformer_Atomic_Embeddings_Materials_Project_dataset_use_b6c12572d788.md)
- Original title in paper: Materials Project (MP) database
- Link: https://materialsproject.org

The 2018.6.1 version contains 69,239 crystalline materials with computed formation energies (Ef) and PBE bandgaps (Eg); used for training and evaluating back-end models (e.g., CGCNN, ALIGNN, MEGNET) and benchmarking ct-UAE performance on formation energy and bandgap prediction. The dataset is split into 60,000 training, 5,000 validation, and 4,239 test samples. It supports the core task by providing ground-truth labels for supervised pretraining of front-end embeddings and downstream property prediction evaluation.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/06_Transformer_Atomic_Embeddings_Materials_Project_dataset_use_5a2f67a5af9b.md)
- Original title in paper: Materials Project (MP*) database
- Link: https://materialsproject.org

The 2023.6.23 version contains 134,243 materials with formation energy and PBE bandgap; used as the primary large-scale dataset to pretrain the CrystalTransformer front-end model for generating universal atomic embeddings (ct-UAEs). Split into 80% training, 10% validation, and 10% testing sets, it enables multi-task pretraining (e.g., Ef + Eg, Ef + Eg + total energy + magnetization) and supports the task of learning transferable, physics-informed atomic representations independent of predefined features.

### [JARVIS Database](../datasets/JARVIS_Database.md)

- Usage page: [usage note](../dataset_uses/06_Transformer_Atomic_Embeddings_JARVIS_Database_dataset_use_d9081ae49cf6.md)
- Original title in paper: JARVIS dataset
- Link: https://jarvis.nist.gov

A curated collection of ~50,000 materials with formation energies and bandgaps, derived from high-throughput DFT calculations; used to evaluate the transferability of ct-UAEs across independent databases. Specifically employed to test ct-UAE-enhanced CGCNN and MEGNET models on formation energy and bandgap prediction, demonstrating consistent accuracy improvements (e.g., 17.5% MAE reduction for Ef), thereby supporting the task of validating cross-database generalizability of universal atomic embeddings.

### [MC3D dataset](../datasets/MC3D_dataset.md)

- Usage page: [usage note](../dataset_uses/06_Transformer_Atomic_Embeddings_MC3D_dataset_dataset_use_86b751f702ce.md)
- Original title in paper: MC3D dataset
- Link: https://github.com/usnistgov/jarvis/tree/master/jarvis/core

A dataset containing 3D crystal structures and associated total energies (E); used to assess ct-UAE performance on a distinct property (total energy) and in a different materials domain. Applied to enhance CGCNN, MEGNET, and ALIGNN models, yielding MAE reductions (e.g., 3.9% for CGCNN), confirming the task-supporting role of ct-UAEs in broadening applicability beyond formation energy and bandgap to other fundamental crystal properties.

### [HOIP Dataset](../datasets/HOIP_Dataset.md)

- Usage page: [usage note](../dataset_uses/06_Transformer_Atomic_Embeddings_HOIP_Dataset_dataset_use_c9f9564247e0.md)
- Original title in paper: Hybrid Organic-Inorganic Perovskite (HOIP) dataset
- Link: https://doi.org/10.1038/sdata.2017.152

A merged dataset of 2,103 HOIP crystals compiled from two prior sources (Kim et al., 2017 and Nakajima & Sawada, 2017); used to evaluate ct-UAEs in data-scarce regimes where traditional ML models underperform. Supports the task by serving as a low-data target domain for transfer learning—ct-UAEs pretrained on MP* significantly improve formation energy prediction accuracy (e.g., 34% MAE reduction for MEGNET), directly addressing the challenge of data scarcity in complex functional materials.

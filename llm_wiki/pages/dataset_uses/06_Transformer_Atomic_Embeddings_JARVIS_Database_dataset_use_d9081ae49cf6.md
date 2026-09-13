# 06_Transformer_Atomic_Embeddings - JARVIS Database

## Dataset Use

A curated collection of ~50,000 materials with formation energies and bandgaps, derived from high-throughput DFT calculations; used to evaluate the transferability of ct-UAEs across independent databases. Specifically employed to test ct-UAE-enhanced CGCNN and MEGNET models on formation energy and bandgap prediction, demonstrating consistent accuracy improvements (e.g., 17.5% MAE reduction for Ef), thereby supporting the task of validating cross-database generalizability of universal atomic embeddings.

## Links

- Paper: [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings.md)
- Task: [task page](../tasks/06_Transformer_Atomic_Embeddings_task_1.md)
- Dataset: [JARVIS Database](../datasets/JARVIS_Database.md)
- Dataset URL: https://jarvis.nist.gov

## Task Context

Generating universal atomic embeddings that serve as transferable, task-agnostic atomic fingerprints to improve the accuracy of machine learning models predicting crystal properties—including formation energy, bandgap, total energy, and total magnetization—across diverse material systems and data-scarce domains such as hybrid organic-inorganic perovskites.

## Metadata

- Dataset use ID: `dataset_use_d9081ae49cf6`
- Original dataset title: JARVIS dataset
- Tags: atomic embedding, crystal property prediction, transfer learning

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

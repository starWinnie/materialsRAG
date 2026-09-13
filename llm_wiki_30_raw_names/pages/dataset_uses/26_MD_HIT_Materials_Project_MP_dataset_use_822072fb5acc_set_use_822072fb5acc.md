# 26_MD_HIT - Materials Project (MP)

## Dataset Use

A large-scale computational materials database containing 125,619 crystal structures (with 89,354 unique compositions), each annotated with DFT-computed properties including formation energy per atom and band gap. The paper uses the full MP dataset to generate composition-based (86,740 unique compositions) and structure-based (123,108–125,619 CIFs) non-redundant subsets via MD-HIT algorithms; these subsets serve as benchmark datasets for training and evaluating ML models (Roost, CrabNet, ALIGNN, DeeperGATGNN) under controlled redundancy conditions for formation energy and band gap prediction.

## Links

- Paper: [26 MD HIT](../papers/26_MD_HIT_paper_364d763e5978.md)
- Task: [task page](../tasks/26_MD_HIT_task_1_task_e55c8a4f2b28.md)
- Dataset: [Materials Project (MP)](../datasets/Materials_Project_MP_dataset_9b0af3c4a714.md)
- Dataset URL: https://materialsproject.org

## Task Context

Designing and applying a dataset redundancy control method to enable objective, realistic evaluation of machine learning models for material property prediction—specifically by preventing overestimated interpolation performance and improving out-of-distribution (OOD) generalization capability on formation energy and band gap prediction tasks.

## Metadata

- Dataset use ID: `dataset_use_822072fb5acc`
- Original dataset title: Materials Project (MP)
- Tags: redundancy reduction, model evaluation, OOD generalization, material property prediction

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

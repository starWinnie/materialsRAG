# 42_Matbench - Task 1

## Task Description

Predicting diverse physical and chemical properties of inorganic bulk materials—including optical, thermal, electronic, thermodynamic, tensile, and elastic properties—using only input materials primitives (chemical composition and/or crystal structure) as features, under standardized, bias-mitigated evaluation to enable fair, reproducible comparison of supervised machine learning algorithms.

## Metadata

- Task ID: `task_760fddd22570`
- Source paper: [42 Matbench](../papers/42_Matbench.md)
- Tags: property prediction, materials informatics, supervised learning

## Supporting Datasets

### [Matbench](../datasets/Matbench.md)

- Usage page: [usage note](../dataset_uses/42_Matbench_Matbench_dataset_use_cd27b9050483.md)
- Original title in paper: Matbench v0.1
- Link: https://hackingmaterials.lbl.gov/automatminer/datasets.html

Matbench v0.1 is a curated benchmark suite comprising 13 distinct supervised machine learning tasks, sourced from 10 independent datasets totaling 312 to 132,752 samples. Each task contains input materials primitives (composition-only or composition + crystal structure) and a single target property (e.g., band gap, formation energy, bulk modulus, metallicity, exfoliation energy), derived from both experimental measurements and density functional theory (DFT) computations. The datasets are precleaned to remove unphysical or task-irrelevant entries (e.g., negative elastic moduli, noble-gas compounds, misconverged DFT structures) and standardized for consistent ML pipeline ingestion. Matbench is used to train, validate, and rigorously evaluate property prediction models—including Automatminer, CGCNN, MEGNet, and Random Forest—via nested cross-validation, enabling unbiased algorithm comparison across property types, data scales, and input modalities.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

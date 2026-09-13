# 42_Matbench - Matbench

## Dataset Use

Matbench v0.1 is a curated benchmark suite comprising 13 distinct supervised machine learning tasks, sourced from 10 independent datasets totaling 312 to 132,752 samples. Each task contains input materials primitives (composition-only or composition + crystal structure) and a single target property (e.g., band gap, formation energy, bulk modulus, metallicity, exfoliation energy), derived from both experimental measurements and density functional theory (DFT) computations. The datasets are precleaned to remove unphysical or task-irrelevant entries (e.g., negative elastic moduli, noble-gas compounds, misconverged DFT structures) and standardized for consistent ML pipeline ingestion. Matbench is used to train, validate, and rigorously evaluate property prediction models—including Automatminer, CGCNN, MEGNet, and Random Forest—via nested cross-validation, enabling unbiased algorithm comparison across property types, data scales, and input modalities.

## Links

- Paper: [42 Matbench](../papers/42_Matbench.md)
- Task: [task page](../tasks/42_Matbench_task_1.md)
- Dataset: [Matbench](../datasets/Matbench.md)
- Dataset URL: https://hackingmaterials.lbl.gov/automatminer/datasets.html

## Task Context

Predicting diverse physical and chemical properties of inorganic bulk materials—including optical, thermal, electronic, thermodynamic, tensile, and elastic properties—using only input materials primitives (chemical composition and/or crystal structure) as features, under standardized, bias-mitigated evaluation to enable fair, reproducible comparison of supervised machine learning algorithms.

## Metadata

- Dataset use ID: `dataset_use_cd27b9050483`
- Original dataset title: Matbench v0.1
- Tags: property prediction, materials informatics, supervised learning

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Problem Definition
- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

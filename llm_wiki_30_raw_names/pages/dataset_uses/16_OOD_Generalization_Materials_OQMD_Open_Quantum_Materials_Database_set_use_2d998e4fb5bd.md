# 16_OOD_Generalization_Materials - OQMD (Open Quantum Materials Database)

## Dataset Use

A large-scale ab initio database of ~1M predicted stable and metastable inorganic compounds, with formation energies, crystal structures, and elemental compositions. Its scale (~10× larger than MP) enables rigorous scaling analysis: the paper uses it to validate learning curves (training set size and time effects) on representationally OOD tasks (e.g., leave-H-out), confirm domain misidentification biases, and demonstrate adverse scaling behavior where increased data degrades OOD performance.

## Links

- Paper: [16 OOD Generalization Materials](../papers/16_OOD_Generalization_Materials_paper_cd925085a1df.md)
- Task: [task page](../tasks/16_OOD_Generalization_Materials_task_1_task_49a79df78a99.md)
- Dataset: [OQMD (Open Quantum Materials Database)](../datasets/OQMD_Open_Quantum_Materials_Database_dataset_9dcd35cc7ac5.md)
- Dataset URL: https://oqmd.org

## Task Context

Probing and characterizing out-of-distribution (OOD) generalization capabilities of machine learning models for materials property prediction—specifically, identifying which OOD tasks (defined by unseen chemistry or structural symmetries) genuinely challenge models versus those that merely reflect interpolation within the representational training domain, and evaluating how model performance scales with training set size and training time on these tasks.

## Metadata

- Dataset use ID: `dataset_use_2d998e4fb5bd`
- Original dataset title: OQMD (Open Quantum Materials Database)
- Tags: OOD generalization, distributional robustness, materials property prediction, scaling law analysis, domain identification

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

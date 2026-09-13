# 16_OOD_Generalization_Materials - Open Quantum Materials Database

## Dataset Use

A large-scale ab initio database of ~1M predicted stable and metastable inorganic compounds, with formation energies, crystal structures, and elemental compositions. Its scale (~10× larger than MP) enables rigorous scaling analysis: the paper uses it to validate learning curves (training set size and time effects) on representationally OOD tasks (e.g., leave-H-out), confirm domain misidentification biases, and demonstrate adverse scaling behavior where increased data degrades OOD performance.

## Links

- Paper: [16 OOD Generalization Materials](../papers/16_OOD_Generalization_Materials.md)
- Task: [task page](../tasks/16_OOD_Generalization_Materials_task_1.md)
- Dataset: [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)
- Dataset URL: https://oqmd.org

## Task Context

Probing and characterizing out-of-distribution (OOD) generalization capabilities of machine learning models for materials property prediction—specifically, identifying which OOD tasks (defined by unseen chemistry or structural symmetries) genuinely challenge models versus those that merely reflect interpolation within the representational training domain, and evaluating how model performance scales with training set size and training time on these tasks.

## Metadata

- Dataset use ID: `dataset_use_67179fd578bb`
- Original dataset title: OQMD (Open Quantum Materials Database)
- Tags: OOD generalization, distributional robustness, materials property prediction, scaling law analysis, domain identification

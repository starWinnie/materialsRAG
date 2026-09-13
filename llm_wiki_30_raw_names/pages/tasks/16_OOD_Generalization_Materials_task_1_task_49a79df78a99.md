# 16_OOD_Generalization_Materials - Task 1

## Task Description

Probing and characterizing out-of-distribution (OOD) generalization capabilities of machine learning models for materials property prediction—specifically, identifying which OOD tasks (defined by unseen chemistry or structural symmetries) genuinely challenge models versus those that merely reflect interpolation within the representational training domain, and evaluating how model performance scales with training set size and training time on these tasks.

## Metadata

- Task ID: `task_49a79df78a99`
- Source paper: [16 OOD Generalization Materials](../papers/16_OOD_Generalization_Materials_paper_cd925085a1df.md)
- Tags: OOD generalization, distributional robustness, materials property prediction, scaling law analysis, domain identification

## Supporting Datasets

### [Materials Project (MP)](../datasets/Materials_Project_MP_dataset_9b0af3c4a714.md)

- Usage page: [usage note](../dataset_uses/16_OOD_Generalization_Materials_Materials_Project_MP_dataset_use_678f_set_use_678f2345f1c3.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org

A database of ~146k ab initio–computed inorganic crystalline materials, containing formation energies, band gaps, bulk moduli, crystal structures (space groups, point groups, crystal systems), and chemical compositions. In this paper, it is used to construct over 700 OOD tasks—including leave-one-element-out, leave-one-period-out, leave-one-group-out, leave-one-space-group-out, and leave-one-crystal-system-out splits—to evaluate ML model generalization on formation energy prediction and assess representational domain coverage via UMAP embedding analysis.

### [JARVIS (Joint Automated Repository for Various Integrated Simulations)](../datasets/JARVIS_Joint_Automated_Repository_for_Various_Integrated_Simulations_dataset_bbdab7ef4ee7.md)

- Usage page: [usage note](../dataset_uses/16_OOD_Generalization_Materials_JARVIS_Joint_Automated_Repository_for_set_use_2052fa873e38.md)
- Original title in paper: JARVIS (Joint Automated Repository for Various Integrated Simulations)
- Link: https://jarvis.nist.gov

A database of ~76k DFT-computed materials properties, including formation energies and crystal structures, curated from multiple sources and standardized for materials informatics. It is used alongside MP and OQMD to ensure robust conclusions across data distributions; specifically, it supports chemistry- and structure-based OOD evaluations (e.g., leave-Mg-out, leave-O-out) and UMAP-based representational domain analysis for formation energy prediction.

### [OQMD (Open Quantum Materials Database)](../datasets/OQMD_Open_Quantum_Materials_Database_dataset_9dcd35cc7ac5.md)

- Usage page: [usage note](../dataset_uses/16_OOD_Generalization_Materials_OQMD_Open_Quantum_Materials_Database_set_use_2d998e4fb5bd.md)
- Original title in paper: OQMD (Open Quantum Materials Database)
- Link: https://oqmd.org

A large-scale ab initio database of ~1M predicted stable and metastable inorganic compounds, with formation energies, crystal structures, and elemental compositions. Its scale (~10× larger than MP) enables rigorous scaling analysis: the paper uses it to validate learning curves (training set size and time effects) on representationally OOD tasks (e.g., leave-H-out), confirm domain misidentification biases, and demonstrate adverse scaling behavior where increased data degrades OOD performance.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

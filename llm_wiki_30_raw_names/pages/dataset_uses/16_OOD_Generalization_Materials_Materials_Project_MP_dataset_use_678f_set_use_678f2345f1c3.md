# 16_OOD_Generalization_Materials - Materials Project (MP)

## Dataset Use

A database of ~146k ab initio–computed inorganic crystalline materials, containing formation energies, band gaps, bulk moduli, crystal structures (space groups, point groups, crystal systems), and chemical compositions. In this paper, it is used to construct over 700 OOD tasks—including leave-one-element-out, leave-one-period-out, leave-one-group-out, leave-one-space-group-out, and leave-one-crystal-system-out splits—to evaluate ML model generalization on formation energy prediction and assess representational domain coverage via UMAP embedding analysis.

## Links

- Paper: [16 OOD Generalization Materials](../papers/16_OOD_Generalization_Materials_paper_cd925085a1df.md)
- Task: [task page](../tasks/16_OOD_Generalization_Materials_task_1_task_49a79df78a99.md)
- Dataset: [Materials Project (MP)](../datasets/Materials_Project_MP_dataset_9b0af3c4a714.md)
- Dataset URL: https://materialsproject.org

## Task Context

Probing and characterizing out-of-distribution (OOD) generalization capabilities of machine learning models for materials property prediction—specifically, identifying which OOD tasks (defined by unseen chemistry or structural symmetries) genuinely challenge models versus those that merely reflect interpolation within the representational training domain, and evaluating how model performance scales with training set size and training time on these tasks.

## Metadata

- Dataset use ID: `dataset_use_678f2345f1c3`
- Original dataset title: Materials Project (MP)
- Tags: OOD generalization, distributional robustness, materials property prediction, scaling law analysis, domain identification

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

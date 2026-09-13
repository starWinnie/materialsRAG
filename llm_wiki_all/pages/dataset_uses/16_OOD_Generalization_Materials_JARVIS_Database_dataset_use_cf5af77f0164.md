# 16_OOD_Generalization_Materials - JARVIS Database

## Dataset Use

A database of ~76k DFT-computed materials properties, including formation energies and crystal structures, curated from multiple sources and standardized for materials informatics. It is used alongside MP and OQMD to ensure robust conclusions across data distributions; specifically, it supports chemistry- and structure-based OOD evaluations (e.g., leave-Mg-out, leave-O-out) and UMAP-based representational domain analysis for formation energy prediction.

## Links

- Paper: [16 OOD Generalization Materials](../papers/16_OOD_Generalization_Materials.md)
- Task: [task page](../tasks/16_OOD_Generalization_Materials_task_1.md)
- Dataset: [JARVIS Database](../datasets/JARVIS_Database.md)
- Dataset URL: https://jarvis.nist.gov

## Task Context

Probing and characterizing out-of-distribution (OOD) generalization capabilities of machine learning models for materials property prediction—specifically, identifying which OOD tasks (defined by unseen chemistry or structural symmetries) genuinely challenge models versus those that merely reflect interpolation within the representational training domain, and evaluating how model performance scales with training set size and training time on these tasks.

## Metadata

- Dataset use ID: `dataset_use_cf5af77f0164`
- Original dataset title: JARVIS (Joint Automated Repository for Various Integrated Simulations)
- Tags: OOD generalization, distributional robustness, materials property prediction, scaling law analysis, domain identification

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

# 09_LLM_Prop - Materials Project

## Dataset Use

A publicly available computational materials database providing DFT-calculated structural and energetic properties for over 145,000 inorganic crystalline compounds. The authors collected crystal structures (CIF files), IDs, and six target properties (band gap, formation energy per atom, energy above hull, unit cell volume, energy per atom, and direct/indirect band gap label) from Materials Project via its free API as of November 1, 2022. This raw data served as the source for generating TextEdge and was used to ensure ground-truth labels for all prediction tasks.

## Links

- Paper: [09 LLM Prop](../papers/09_LLM_Prop_paper_ff6e0dbcf294.md)
- Task: [task page](../tasks/09_LLM_Prop_task_1_task_dbae0fb23b52.md)
- Dataset: [Materials Project](../datasets/Materials_Project_dataset_d55b16e3041b.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Predicting six key physical and electronic properties of crystalline materials—including band gap (eV), formation energy per atom (eV/atom), energy above hull (eV/atom), unit cell volume (Å³/cell), energy per atom (eV/atom), and binary classification of whether the band gap is direct or indirect—from natural language text descriptions of crystal structures.

## Metadata

- Dataset use ID: `dataset_use_48b1eb2b5f32`
- Original dataset title: Materials Project
- Tags: property prediction, crystal property prediction, regression, classification, materials informatics

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->

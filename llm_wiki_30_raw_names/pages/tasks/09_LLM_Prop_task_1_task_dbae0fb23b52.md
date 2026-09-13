# 09_LLM_Prop - Task 1

## Task Description

Predicting six key physical and electronic properties of crystalline materials—including band gap (eV), formation energy per atom (eV/atom), energy above hull (eV/atom), unit cell volume (Å³/cell), energy per atom (eV/atom), and binary classification of whether the band gap is direct or indirect—from natural language text descriptions of crystal structures.

## Metadata

- Task ID: `task_dbae0fb23b52`
- Source paper: [09 LLM Prop](../papers/09_LLM_Prop_paper_ff6e0dbcf294.md)
- Tags: property prediction, crystal property prediction, regression, classification, materials informatics

## Supporting Datasets

### [TextEdge](../datasets/TextEdge_dataset_da938cf04999.md)

- Usage page: [usage note](../dataset_uses/09_LLM_Prop_TextEdge_dataset_use_1b2203043e7c_set_use_1b2203043e7c.md)
- Original title in paper: TextEdge
- Link: https://drive.google.com/drive/folders/1YCDBzwjwNRIc1FRkB662G3Y5AOWaokUG

TextEdge is a benchmark dataset curated by the authors, containing ~144,931 crystal structure-description pairs derived from the Materials Project database. Each entry includes a human-readable, Robocrystallographer-generated text description (e.g., space group, bonding geometry, Wyckoff sites, stoichiometry) and six labeled properties: band gap, formation energy per atom, energy above hull, unit cell volume, energy per atom, and direct/indirect band gap indicator. It is used to train and evaluate LLM-Prop for property prediction from text input, enabling fair comparison against GNN baselines on identical splits (125,098 train / 9,945 val / 9,888 test samples).

### [Materials Project](../datasets/Materials_Project_dataset_d55b16e3041b.md)

- Usage page: [usage note](../dataset_uses/09_LLM_Prop_Materials_Project_dataset_use_48b1eb2b5f32_set_use_48b1eb2b5f32.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org/

A publicly available computational materials database providing DFT-calculated structural and energetic properties for over 145,000 inorganic crystalline compounds. The authors collected crystal structures (CIF files), IDs, and six target properties (band gap, formation energy per atom, energy above hull, unit cell volume, energy per atom, and direct/indirect band gap label) from Materials Project via its free API as of November 1, 2022. This raw data served as the source for generating TextEdge and was used to ensure ground-truth labels for all prediction tasks.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->

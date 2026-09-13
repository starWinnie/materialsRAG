# 09_LLM_Prop - TextEdge

## Dataset Use

TextEdge is a benchmark dataset curated by the authors, containing ~144,931 crystal structure-description pairs derived from the Materials Project database. Each entry includes a human-readable, Robocrystallographer-generated text description (e.g., space group, bonding geometry, Wyckoff sites, stoichiometry) and six labeled properties: band gap, formation energy per atom, energy above hull, unit cell volume, energy per atom, and direct/indirect band gap indicator. It is used to train and evaluate LLM-Prop for property prediction from text input, enabling fair comparison against GNN baselines on identical splits (125,098 train / 9,945 val / 9,888 test samples).

## Links

- Paper: [09 LLM Prop](../papers/09_LLM_Prop_paper_ff6e0dbcf294.md)
- Task: [task page](../tasks/09_LLM_Prop_task_1_task_dbae0fb23b52.md)
- Dataset: [TextEdge](../datasets/TextEdge_dataset_da938cf04999.md)
- Dataset URL: https://drive.google.com/drive/folders/1YCDBzwjwNRIc1FRkB662G3Y5AOWaokUG

## Task Context

Predicting six key physical and electronic properties of crystalline materials—including band gap (eV), formation energy per atom (eV/atom), energy above hull (eV/atom), unit cell volume (Å³/cell), energy per atom (eV/atom), and binary classification of whether the band gap is direct or indirect—from natural language text descriptions of crystal structures.

## Metadata

- Dataset use ID: `dataset_use_1b2203043e7c`
- Original dataset title: TextEdge
- Tags: property prediction, crystal property prediction, regression, classification, materials informatics

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

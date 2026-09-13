# TextEdge

## Metadata

- Dataset ID: `dataset_da938cf04999`
- Aliases: TextEdge
- Links: https://drive.google.com/drive/folders/1YCDBzwjwNRIc1FRkB662G3Y5AOWaokUG
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- TextEdge is a benchmark dataset curated by the authors, containing ~144,931 crystal structure-description pairs derived from the Materials Project database. Each entry includes a human-readable, Robocrystallographer-generated text description (e.g., space group, bonding geometry, Wyckoff sites, stoichiometry) and six labeled properties: band gap, formation energy per atom, energy above hull, unit cell volume, energy per atom, and direct/indirect band gap indicator. It is used to train and evaluate LLM-Prop for property prediction from text input, enabling fair comparison against GNN baselines on identical splits (125,098 train / 9,945 val / 9,888 test samples).

## Uses

- [09_LLM_Prop](../dataset_uses/09_LLM_Prop_TextEdge_dataset_use_1b2203043e7c_set_use_1b2203043e7c.md): [09 LLM Prop](../papers/09_LLM_Prop_paper_ff6e0dbcf294.md), [task](../tasks/09_LLM_Prop_task_1_task_dbae0fb23b52.md)

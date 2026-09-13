# Text-mined Inorganic Solid-State Synthesis Database

## Metadata

- Dataset ID: `dataset_b1d76b106c72`
- Aliases: Text-mined Inorganic Solid-State Synthesis Database
- Links: https://doi.org/10.1038/s41524-024-01474-5
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A publicly released dataset of inorganic solid-state synthesis recipes, text-mined from scientific literature using NLP and rule-based extraction, containing experimentally reported calcination and sintering temperatures. After preprocessing (filtering to 200–2000 °C, averaging repeated entries, selecting final heating steps), it yielded 12,228 calcination and 12,296 sintering temperature records—exclusively for oxides. This dataset was used to train the synthesis-condition predictor models (random forest with Magpie features), enabling reward assignment for synthesis objectives during RL training and evaluation.

## Uses

- [82_Deep reinforcement learning for inverse inorganic materials design](../dataset_uses/82_Deep_reinforcement_learning_for_inverse_inorganic_materials_design_Text-mined_Inorganic.md): [82 Deep reinforcement learning for inverse inorganic materials design](../papers/82_Deep_reinforcement_learning_for_inverse_inorganic_materials_design.md), [task](../tasks/82_Deep_reinforcement_learning_for_inverse_inorganic_materials_design_task_1.md)

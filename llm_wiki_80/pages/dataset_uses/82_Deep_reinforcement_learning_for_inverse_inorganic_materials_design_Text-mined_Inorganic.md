# 82_Deep reinforcement learning for inverse inorganic materials design - Text-mined Inorganic Solid-State Synthesis Database

## Dataset Use

A publicly released dataset of inorganic solid-state synthesis recipes, text-mined from scientific literature using NLP and rule-based extraction, containing experimentally reported calcination and sintering temperatures. After preprocessing (filtering to 200–2000 °C, averaging repeated entries, selecting final heating steps), it yielded 12,228 calcination and 12,296 sintering temperature records—exclusively for oxides. This dataset was used to train the synthesis-condition predictor models (random forest with Magpie features), enabling reward assignment for synthesis objectives during RL training and evaluation.

## Links

- Paper: [82 Deep reinforcement learning for inverse inorganic materials design](../papers/82_Deep_reinforcement_learning_for_inverse_inorganic_materials_design.md)
- Task: [task page](../tasks/82_Deep_reinforcement_learning_for_inverse_inorganic_materials_design_task_1.md)
- Dataset: [Text-mined Inorganic Solid-State Synthesis Database](../datasets/Text-mined_Inorganic_Solid-State_Synthesis_Database.md)
- Dataset URL: https://doi.org/10.1038/s41524-024-01474-5

## Task Context

Generating novel inorganic oxide compositions that simultaneously satisfy multiple target objectives—including materials properties (band gap, formation energy, bulk modulus, shear modulus) and synthesis conditions (sintering temperature, calcination temperature)—via inverse design, where the goal is to discover chemically valid, stable, and synthetically feasible compounds without exhaustive enumeration.

## Metadata

- Dataset use ID: `dataset_use_ff18f129af28`
- Original dataset title: Text-mined Inorganic Solid-State Synthesis Database
- Tags: inverse materials design, multi-objective optimization, composition generation

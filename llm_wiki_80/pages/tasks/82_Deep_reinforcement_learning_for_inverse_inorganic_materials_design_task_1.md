# 82_Deep reinforcement learning for inverse inorganic materials design - Task 1

## Task Description

Generating novel inorganic oxide compositions that simultaneously satisfy multiple target objectives—including materials properties (band gap, formation energy, bulk modulus, shear modulus) and synthesis conditions (sintering temperature, calcination temperature)—via inverse design, where the goal is to discover chemically valid, stable, and synthetically feasible compounds without exhaustive enumeration.

## Metadata

- Task ID: `task_1beb1a89afc8`
- Source paper: [82 Deep reinforcement learning for inverse inorganic materials design](../papers/82_Deep_reinforcement_learning_for_inverse_inorganic_materials_design.md)
- Tags: inverse materials design, multi-objective optimization, composition generation

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/82_Deep_reinforcement_learning_for_inverse_inorganic_materials_design_Materials_Project_da.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org

A high-throughput quantum-mechanics-derived database containing crystal structures and computed properties (formation energy, band gap, bulk modulus, shear modulus) for over 100,000 inorganic compounds. In this paper, a preprocessed subset of 22,555 oxide compounds (for formation energy and band gap) and 9,888 oxides (for bulk/shear modulus) was used to train both the RL generator models (via pretraining for PGN) and the supervised property predictor models (Roost for properties; random forest for synthesis temperatures). It directly supports the task by providing ground-truth property labels needed to compute rewards during RL training and to evaluate generated compositions.

### [Text-mined Inorganic Solid-State Synthesis Database](../datasets/Text-mined_Inorganic_Solid-State_Synthesis_Database.md)

- Usage page: [usage note](../dataset_uses/82_Deep_reinforcement_learning_for_inverse_inorganic_materials_design_Text-mined_Inorganic.md)
- Original title in paper: Text-mined Inorganic Solid-State Synthesis Database
- Link: https://doi.org/10.1038/s41524-024-01474-5

A publicly released dataset of inorganic solid-state synthesis recipes, text-mined from scientific literature using NLP and rule-based extraction, containing experimentally reported calcination and sintering temperatures. After preprocessing (filtering to 200–2000 °C, averaging repeated entries, selecting final heating steps), it yielded 12,228 calcination and 12,296 sintering temperature records—exclusively for oxides. This dataset was used to train the synthesis-condition predictor models (random forest with Magpie features), enabling reward assignment for synthesis objectives during RL training and evaluation.

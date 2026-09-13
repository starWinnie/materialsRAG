# 82_Deep reinforcement learning for inverse inorganic materials design - Materials Project

## Dataset Use

A high-throughput quantum-mechanics-derived database containing crystal structures and computed properties (formation energy, band gap, bulk modulus, shear modulus) for over 100,000 inorganic compounds. In this paper, a preprocessed subset of 22,555 oxide compounds (for formation energy and band gap) and 9,888 oxides (for bulk/shear modulus) was used to train both the RL generator models (via pretraining for PGN) and the supervised property predictor models (Roost for properties; random forest for synthesis temperatures). It directly supports the task by providing ground-truth property labels needed to compute rewards during RL training and to evaluate generated compositions.

## Links

- Paper: [82 Deep reinforcement learning for inverse inorganic materials design](../papers/82_Deep_reinforcement_learning_for_inverse_inorganic_materials_design.md)
- Task: [task page](../tasks/82_Deep_reinforcement_learning_for_inverse_inorganic_materials_design_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating novel inorganic oxide compositions that simultaneously satisfy multiple target objectives—including materials properties (band gap, formation energy, bulk modulus, shear modulus) and synthesis conditions (sintering temperature, calcination temperature)—via inverse design, where the goal is to discover chemically valid, stable, and synthetically feasible compounds without exhaustive enumeration.

## Metadata

- Dataset use ID: `dataset_use_5d12dfc8e6da`
- Original dataset title: Materials Project
- Tags: inverse materials design, multi-objective optimization, composition generation

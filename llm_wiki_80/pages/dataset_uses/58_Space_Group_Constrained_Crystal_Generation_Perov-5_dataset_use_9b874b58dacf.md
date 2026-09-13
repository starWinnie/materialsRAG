# 58_Space Group Constrained Crystal Generation - Perov-5

## Dataset Use

A dataset of 18,928 perovskite crystal structures, each containing exactly 5 atoms in the unit cell, with diverse chemical compositions but similar structural motifs. It is used to train and evaluate DiffCSP++ on crystal structure prediction and ab initio generation tasks under space group constraints, specifically to assess match rate and RMSE against ground truth structures when generating from given compositions or templates.

## Links

- Paper: [58 Space Group Constrained Crystal Generation](../papers/58_Space_Group_Constrained_Crystal_Generation.md)
- Task: [task page](../tasks/58_Space_Group_Constrained_Crystal_Generation_task_1.md)
- Dataset: [Perov-5](../datasets/Perov-5.md)
- Dataset URL: https://doi.org/10.1039/C2EE22174E

## Task Context

Generating crystal structures that strictly satisfy user-specified space group symmetry constraints, including both lattice geometry (crystal family) and atomic positional constraints (Wyckoff positions), for applications in controllable ab initio crystal design and crystal structure prediction.

## Metadata

- Dataset use ID: `dataset_use_9b874b58dacf`
- Original dataset title: Perov-5
- Tags: crystal generation, space group constraint, controllable generation

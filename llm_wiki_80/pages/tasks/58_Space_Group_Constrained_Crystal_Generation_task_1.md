# 58_Space Group Constrained Crystal Generation - Task 1

## Task Description

Generating crystal structures that strictly satisfy user-specified space group symmetry constraints, including both lattice geometry (crystal family) and atomic positional constraints (Wyckoff positions), for applications in controllable ab initio crystal design and crystal structure prediction.

## Metadata

- Task ID: `task_a0299547be82`
- Source paper: [58 Space Group Constrained Crystal Generation](../papers/58_Space_Group_Constrained_Crystal_Generation.md)
- Tags: crystal generation, space group constraint, controllable generation

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/58_Space_Group_Constrained_Crystal_Generation_Perov-5_dataset_use_9b874b58dacf.md)
- Original title in paper: Perov-5
- Link: https://doi.org/10.1039/C2EE22174E

A dataset of 18,928 perovskite crystal structures, each containing exactly 5 atoms in the unit cell, with diverse chemical compositions but similar structural motifs. It is used to train and evaluate DiffCSP++ on crystal structure prediction and ab initio generation tasks under space group constraints, specifically to assess match rate and RMSE against ground truth structures when generating from given compositions or templates.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/58_Space_Group_Constrained_Crystal_Generation_Carbon-24_dataset_use_15165d6324b2.md)
- Original title in paper: Carbon-24
- Link: https://airss.ac.uk/data/carbon

A dataset of 10,153 carbon-only crystal structures, with unit cells containing between 6 and 24 atoms, exhibiting high structural diversity. It is used to evaluate DiffCSP++'s ab initio generation capability—assessing validity (structural and compositional), coverage (COV-R/COV-P), and property distribution fidelity (density, formation energy, element count)—without crystal structure prediction due to lack of one-to-one composition–structure mapping.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/58_Space_Group_Constrained_Crystal_Generation_MP-20_dataset_use_82bcf308d869.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org

A subset of the Materials Project database containing 45,231 experimentally realized inorganic crystal structures, each with ≤20 atoms per unit cell and diverse compositions and space groups. It serves as a primary benchmark for both crystal structure prediction (with match rate and RMSE metrics) and ab initio generation (validity, coverage, property statistics), enabling evaluation of DiffCSP++'s generalization across broad chemical and symmetry space.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/58_Space_Group_Constrained_Crystal_Generation_MPTS-52_dataset_use_3960dc24aca9.md)
- Original title in paper: MPTS-52
- Link: None

An extended, more challenging variant of MP-20 containing 40,476 crystal structures with up to 52 atoms per unit cell, designed to test scalability and robustness of space group–constrained generation on larger, more complex unit cells. It is used for crystal structure prediction evaluation (match rate, RMSE) with chronological train/validation/test splits, highlighting DiffCSP++'s performance on computationally demanding cases.

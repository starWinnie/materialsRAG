# 92_Predicting symmetric structures of large crystals with GPU-based Ising machines - CRYSIM random generation (RG) training dataset

## Dataset Use

An author-curated dataset of 1000 initial crystal structures generated via the paper’s custom Random Generation (RG) algorithm, tailored to the input chemical composition and constrained by statistical bounds derived from the Materials Project. Each structure is encoded into a binary vector and paired with its M3GNet-predicted potential energy (without relaxation), forming the initial training set D = {(x_l, y_l) | l = 1,…,1000} for the Factorization Machine regressor. This dataset directly supports the task of learning an accurate, symmetry-informed surrogate energy model to guide Ising-based optimization.

## Links

- Paper: [92 Predicting symmetric structures of large crystals with GPU-based Ising machines](../papers/92_Predicting_symmetric_structures_of_large_crystals_with_GPU-based_Ising_machines.md)
- Task: [task page](../tasks/92_Predicting_symmetric_structures_of_large_crystals_with_GPU-based_Ising_machines_task_1.md)
- Dataset: [CRYSIM random generation (RG) training dataset](../datasets/CRYSIM_random_generation_RG_training_dataset.md)
- Dataset URL: None

## Task Context

Predicting the most thermodynamically stable crystal structure (i.e., global minimum on the potential energy surface) for a given chemical composition, with explicit handling of space group symmetry, Wyckoff position combinations, and atomic coordinates — especially for large crystals containing over 150 atoms per unit cell.

## Metadata

- Dataset use ID: `dataset_use_9cebd36e8569`
- Original dataset title: CRYSIM random generation (RG) training dataset
- Tags: crystal structure prediction, symmetry-aware optimization, large-system CSP, ground-state structure discovery

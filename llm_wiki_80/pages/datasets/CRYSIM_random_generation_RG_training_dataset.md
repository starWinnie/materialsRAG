# CRYSIM random generation (RG) training dataset

## Metadata

- Dataset ID: `dataset_3ab813321ec9`
- Aliases: CRYSIM random generation (RG) training dataset
- Links: None
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- An author-curated dataset of 1000 initial crystal structures generated via the paper’s custom Random Generation (RG) algorithm, tailored to the input chemical composition and constrained by statistical bounds derived from the Materials Project. Each structure is encoded into a binary vector and paired with its M3GNet-predicted potential energy (without relaxation), forming the initial training set D = {(x_l, y_l) | l = 1,…,1000} for the Factorization Machine regressor. This dataset directly supports the task of learning an accurate, symmetry-informed surrogate energy model to guide Ising-based optimization.

## Uses

- [92_Predicting symmetric structures of large crystals with GPU-based Ising machines](../dataset_uses/92_Predicting_symmetric_structures_of_large_crystals_with_GPU-based_Ising_machines_CRYSIM_.md): [92 Predicting symmetric structures of large crystals with GPU-based Ising machines](../papers/92_Predicting_symmetric_structures_of_large_crystals_with_GPU-based_Ising_machines.md), [task](../tasks/92_Predicting_symmetric_structures_of_large_crystals_with_GPU-based_Ising_machines_task_1.md)

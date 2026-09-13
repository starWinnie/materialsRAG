# 92_Predicting symmetric structures of large crystals with GPU-based Ising machines - Task 1

## Task Description

Predicting the most thermodynamically stable crystal structure (i.e., global minimum on the potential energy surface) for a given chemical composition, with explicit handling of space group symmetry, Wyckoff position combinations, and atomic coordinates — especially for large crystals containing over 150 atoms per unit cell.

## Metadata

- Task ID: `task_a83024ec17f2`
- Source paper: [92 Predicting symmetric structures of large crystals with GPU-based Ising machines](../papers/92_Predicting_symmetric_structures_of_large_crystals_with_GPU-based_Ising_machines.md)
- Tags: crystal structure prediction, symmetry-aware optimization, large-system CSP, ground-state structure discovery

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/92_Predicting_symmetric_structures_of_large_crystals_with_GPU-based_Ising_machines_Materia.md)
- Original title in paper: Materials Project (MP) database
- Link: https://materialsproject.org

A public, web-accessible database containing experimentally validated and computationally derived crystal structures, along with their calculated properties (e.g., formation energies, stability above hull, relaxed geometries). In this paper, MP is used to obtain ground-truth reference structures (e.g., mp-11277, mp-1672, mp-31235, mp-755253, mp-1211008, mp-1106140, mp-6008, mp-1200292) for benchmarking CRYSIM’s predictions; it provides the target structures against which predicted configurations are matched using pymatgen’s StructureMatcher. It supports the core task of evaluating whether CRYSIM successfully discovers the known stable phase.

### [CRYSIM random generation (RG) training dataset](../datasets/CRYSIM_random_generation_RG_training_dataset.md)

- Usage page: [usage note](../dataset_uses/92_Predicting_symmetric_structures_of_large_crystals_with_GPU-based_Ising_machines_CRYSIM_.md)
- Original title in paper: CRYSIM random generation (RG) training dataset
- Link: None

An author-curated dataset of 1000 initial crystal structures generated via the paper’s custom Random Generation (RG) algorithm, tailored to the input chemical composition and constrained by statistical bounds derived from the Materials Project. Each structure is encoded into a binary vector and paired with its M3GNet-predicted potential energy (without relaxation), forming the initial training set D = {(x_l, y_l) | l = 1,…,1000} for the Factorization Machine regressor. This dataset directly supports the task of learning an accurate, symmetry-informed surrogate energy model to guide Ising-based optimization.

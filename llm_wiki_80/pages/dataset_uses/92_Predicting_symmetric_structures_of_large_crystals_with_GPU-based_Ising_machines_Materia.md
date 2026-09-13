# 92_Predicting symmetric structures of large crystals with GPU-based Ising machines - Materials Project

## Dataset Use

A public, web-accessible database containing experimentally validated and computationally derived crystal structures, along with their calculated properties (e.g., formation energies, stability above hull, relaxed geometries). In this paper, MP is used to obtain ground-truth reference structures (e.g., mp-11277, mp-1672, mp-31235, mp-755253, mp-1211008, mp-1106140, mp-6008, mp-1200292) for benchmarking CRYSIM’s predictions; it provides the target structures against which predicted configurations are matched using pymatgen’s StructureMatcher. It supports the core task of evaluating whether CRYSIM successfully discovers the known stable phase.

## Links

- Paper: [92 Predicting symmetric structures of large crystals with GPU-based Ising machines](../papers/92_Predicting_symmetric_structures_of_large_crystals_with_GPU-based_Ising_machines.md)
- Task: [task page](../tasks/92_Predicting_symmetric_structures_of_large_crystals_with_GPU-based_Ising_machines_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting the most thermodynamically stable crystal structure (i.e., global minimum on the potential energy surface) for a given chemical composition, with explicit handling of space group symmetry, Wyckoff position combinations, and atomic coordinates — especially for large crystals containing over 150 atoms per unit cell.

## Metadata

- Dataset use ID: `dataset_use_5a9620636a32`
- Original dataset title: Materials Project (MP) database
- Tags: crystal structure prediction, symmetry-aware optimization, large-system CSP, ground-state structure discovery

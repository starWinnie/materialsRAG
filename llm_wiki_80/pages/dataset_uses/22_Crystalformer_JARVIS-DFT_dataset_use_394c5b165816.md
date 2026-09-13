# 22_Crystalformer - JARVIS-DFT

## Dataset Use

A dataset of 55,723 DFT-computed crystalline materials compiled by Choudhary et al. (2020), available via the JARVIS platform. It includes unit-cell structural data (atomic positions, species, lattice vectors) and properties: formation energy, total energy, bandgap (computed with two functionals: OPT and MBJ), and energy above hull (E_hull). The paper uses it for regression benchmarking across five property prediction tasks, following standardized splits established in prior work (e.g., Yan et al., 2022).

## Links

- Paper: [22 Crystalformer](../papers/22_Crystalformer.md)
- Task: [task page](../tasks/22_Crystalformer_task_1.md)
- Dataset: [JARVIS-DFT](../datasets/JARVIS-DFT.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Predicting multiple physical properties of crystalline materials—including formation energy, bandgap, bulk modulus, shear modulus, total energy, and energy above hull—from their periodic crystal structures represented as unit cells with atomic positions, species, and lattice vectors.

## Metadata

- Dataset use ID: `dataset_use_394c5b165816`
- Original dataset title: JARVIS-DFT (3D 2021)
- Tags: property prediction, crystal structure encoding, regression

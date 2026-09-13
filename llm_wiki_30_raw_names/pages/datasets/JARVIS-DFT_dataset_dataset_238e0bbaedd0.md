# JARVIS-DFT dataset

## Metadata

- Dataset ID: `dataset_238e0bbaedd0`
- Aliases: JARVIS-DFT dataset
- Links: https://jarvis.nist.gov/
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A curated collection of DFT-computed crystal tensor properties sourced from the JARVIS-DFT database, containing 4,713 dielectric tensors (unitless relative dielectric constants), 4,998 piezoelectric tensors (in C/m²), and 14,220 elastic tensors (in GPa), each paired with its corresponding crystal structure (atomic positions, lattice vectors, and elemental features). The dataset is constructed by extracting both tensor values and structures directly from consistent DFT calculation files to guarantee alignment between structural symmetry and tensor symmetry constraints, and is used to train and evaluate GMTNet’s ability to predict symmetry-respecting tensors.

## Uses

- [20_GMTNet](../dataset_uses/20_GMTNet_JARVIS-DFT_dataset_dataset_use_9b85d07df46a_set_use_9b85d07df46a.md): [20 GMTNet](../papers/20_GMTNet_paper_e25217f4266d.md), [task](../tasks/20_GMTNet_task_1_task_78314418eccc.md)

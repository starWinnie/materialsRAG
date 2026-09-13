# 67_Generative Hierarchical Materials Search - Materials Project

## Dataset Use

A publicly accessible database containing computed properties and crystal structures for over 140,000 inorganic materials, including CIF files, space groups, formation energies, and chemical formulae. In this paper, it is used to (1) provide formula-to-structure pairs (Dlo) for training the diffusion model πlo, (2) serve as a reference set for match rate evaluation via pymatgen's StructureMatcher, (3) assess uniqueness by checking whether generated formulae exist in its collection, and (4) supply DFT-computed formation energies for GNN pretraining and validation.

## Links

- Paper: [67 Generative Hierarchical Materials Search](../papers/67_Generative_Hierarchical_Materials_Search.md)
- Task: [task page](../tasks/67_Generative_Hierarchical_Materials_Search_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating novel, physically viable crystal structures that satisfy user-specified constraints expressed in natural language (e.g., 'a stable chalcogenide with atom ratio 1:1:2 that is not on ICSD'), by jointly optimizing for instruction compliance, structural validity, low formation energy, and uniqueness — without requiring pre-existing language-to-structure paired data.

## Metadata

- Dataset use ID: `dataset_use_80a2b088a4b4`
- Original dataset title: Materials Project
- Tags: crystal structure generation, language-guided materials design, controllable generative modeling

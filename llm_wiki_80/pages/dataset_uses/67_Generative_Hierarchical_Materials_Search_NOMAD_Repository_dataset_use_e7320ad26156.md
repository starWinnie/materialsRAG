# 67_Generative Hierarchical Materials Search - NOMAD Repository

## Dataset Use

A large-scale, FAIR-compliant repository of materials science data, including DFT-calculated crystal structures, energies, and metadata from published studies and automated workflows. In this paper, it is explicitly listed (alongside Materials Project and OQMD) as one of the sources used to train the diffusion model πlo for crystal structure generation, contributing formula-to-structure pairs (Dlo) and enabling broader compositional and structural diversity in training.

## Links

- Paper: [67 Generative Hierarchical Materials Search](../papers/67_Generative_Hierarchical_Materials_Search.md)
- Task: [task page](../tasks/67_Generative_Hierarchical_Materials_Search_task_1.md)
- Dataset: [NOMAD Repository](../datasets/NOMAD_Repository.md)
- Dataset URL: https://nomad-lab.eu

## Task Context

Generating novel, physically viable crystal structures that satisfy user-specified constraints expressed in natural language (e.g., 'a stable chalcogenide with atom ratio 1:1:2 that is not on ICSD'), by jointly optimizing for instruction compliance, structural validity, low formation energy, and uniqueness — without requiring pre-existing language-to-structure paired data.

## Metadata

- Dataset use ID: `dataset_use_e7320ad26156`
- Original dataset title: NOMAD Repository
- Tags: crystal structure generation, language-guided materials design, controllable generative modeling

# 67_Generative Hierarchical Materials Search - Inorganic Crystal Structure Database

## Dataset Use

A curated collection of experimentally determined inorganic crystal structures, containing over 200,000 entries with detailed structural information (atomic positions, lattice parameters, space groups) and chemical formulae. In this paper, it is used to (1) define uniqueness by filtering out generated formulae already present in ICSD, (2) support the high-level heuristic Rhi via a uniqueness checker against known structures, and (3) form part of the reference set for match rate evaluation alongside Materials Project.

## Links

- Paper: [67 Generative Hierarchical Materials Search](../papers/67_Generative_Hierarchical_Materials_Search.md)
- Task: [task page](../tasks/67_Generative_Hierarchical_Materials_Search_task_1.md)
- Dataset: [Inorganic Crystal Structure Database](../datasets/Inorganic_Crystal_Structure_Database.md)
- Dataset URL: https://icsd.fiz-karlsruhe.de

## Task Context

Generating novel, physically viable crystal structures that satisfy user-specified constraints expressed in natural language (e.g., 'a stable chalcogenide with atom ratio 1:1:2 that is not on ICSD'), by jointly optimizing for instruction compliance, structural validity, low formation energy, and uniqueness — without requiring pre-existing language-to-structure paired data.

## Metadata

- Dataset use ID: `dataset_use_3bb1e0060ae5`
- Original dataset title: Inorganic Crystal Structure Database (ICSD)
- Tags: crystal structure generation, language-guided materials design, controllable generative modeling

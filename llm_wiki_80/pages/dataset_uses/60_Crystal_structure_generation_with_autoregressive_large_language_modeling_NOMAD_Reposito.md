# 60_Crystal structure generation with autoregressive large language modeling - NOMAD Repository

## Dataset Use

A large-scale repository of computational materials science data, including DFT-optimized crystal structures. Structures were downloaded from NOMAD in April 2023 and integrated into the unified ~3.6 million structure dataset. NOMAD contributed additional structural diversity—especially for less common stoichiometries and element combinations—which helped improve CrystaLLM’s ability to generate valid structures for underrepresented classes (e.g., intermetallics, mixed-anion compounds) during both training and challenge-set evaluation.

## Links

- Paper: [60 Crystal structure generation with autoregressive large language modeling](../papers/60_Crystal_structure_generation_with_autoregressive_large_language_modeling.md)
- Task: [task page](../tasks/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_task_1.md)
- Dataset: [NOMAD Repository](../datasets/NOMAD_Repository.md)
- Dataset URL: https://nomad-lab.eu/

## Task Context

Generating plausible, physically valid crystal structures for inorganic compounds given only their chemical composition (and optionally space group), with the goal of producing candidates suitable for downstream crystal structure prediction (CSP) and materials discovery workflows.

## Metadata

- Dataset use ID: `dataset_use_c78370fe6397`
- Original dataset title: NOMAD Repository
- Tags: crystal structure generation, inorganic materials design, CSP candidate generation

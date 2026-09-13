# 60_Crystal structure generation with autoregressive large language modeling - Open Quantum Materials Database

## Dataset Use

A high-throughput DFT database of predicted inorganic materials, contributing to the combined ~3.6 million structure dataset. Specifically, version 1.5 (released October 2021) was used. The OQMD structures—particularly many pyrochlores used in validation—provided diverse, computationally generated crystal structures that expanded coverage beyond experimentally reported entries, enabling CrystaLLM to learn broader structural patterns and support generalization to unseen compositions and space groups during training and benchmarking.

## Links

- Paper: [60 Crystal structure generation with autoregressive large language modeling](../papers/60_Crystal_structure_generation_with_autoregressive_large_language_modeling.md)
- Task: [task page](../tasks/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_task_1.md)
- Dataset: [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)
- Dataset URL: https://oqmd.org/

## Task Context

Generating plausible, physically valid crystal structures for inorganic compounds given only their chemical composition (and optionally space group), with the goal of producing candidates suitable for downstream crystal structure prediction (CSP) and materials discovery workflows.

## Metadata

- Dataset use ID: `dataset_use_9a067b8c1c08`
- Original dataset title: Open Quantum Materials Database (OQMD)
- Tags: crystal structure generation, inorganic materials design, CSP candidate generation

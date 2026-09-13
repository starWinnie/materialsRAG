# 60_Crystal structure generation with autoregressive large language modeling - MPTS-52

## Dataset Use

A challenging benchmark dataset of 40,476 inorganic materials, notable for containing structures with up to 52 atoms per unit cell—making it the most complex benchmark used. It was split into 27,380/5,000/8,096 train/validation/test sets (matching DiffCSP’s protocol) and used to rigorously test CrystaLLM’s ability to generate large, complex structures under composition-only conditioning. This dataset directly supports the task of evaluating scalability and robustness in high-atom-count CSP scenarios.

## Links

- Paper: [60 Crystal structure generation with autoregressive large language modeling](../papers/60_Crystal_structure_generation_with_autoregressive_large_language_modeling.md)
- Task: [task page](../tasks/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_task_1.md)
- Dataset: [MPTS-52](../datasets/MPTS-52.md)
- Dataset URL: https://github.com/sparks-baird/mp-time-split

## Task Context

Generating plausible, physically valid crystal structures for inorganic compounds given only their chemical composition (and optionally space group), with the goal of producing candidates suitable for downstream crystal structure prediction (CSP) and materials discovery workflows.

## Metadata

- Dataset use ID: `dataset_use_8366e1e949c1`
- Original dataset title: MPTS-52
- Tags: crystal structure generation, inorganic materials design, CSP candidate generation

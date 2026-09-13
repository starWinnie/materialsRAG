# 60_Crystal structure generation with autoregressive large language modeling - Perov-5

## Dataset Use

A benchmark dataset of 18,928 perovskite structures used to evaluate CrystaLLM’s conditional generation performance (i.e., predicting structures given composition). It was split into train/validation/test sets (60-20-20) and used to train and benchmark CrystaLLM variants specifically for perovskite CSP tasks. The dataset supports the task of assessing how well CrystaLLM recovers known ground-state perovskite structures from cell composition alone, measured via match rate and RMSE against ground truth.

## Links

- Paper: [60 Crystal structure generation with autoregressive large language modeling](../papers/60_Crystal_structure_generation_with_autoregressive_large_language_modeling.md)
- Task: [task page](../tasks/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_task_1.md)
- Dataset: [Perov-5](../datasets/Perov-5.md)
- Dataset URL: https://archive.materialscloud.org/record/2020.0026/v1

## Task Context

Generating plausible, physically valid crystal structures for inorganic compounds given only their chemical composition (and optionally space group), with the goal of producing candidates suitable for downstream crystal structure prediction (CSP) and materials discovery workflows.

## Metadata

- Dataset use ID: `dataset_use_de6fa12105f7`
- Original dataset title: Perov-5
- Tags: crystal structure generation, inorganic materials design, CSP candidate generation

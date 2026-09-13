# 44_Synthesizability_Crystalline_Inorganic - Task 1

## Task Description

Predicting the synthesizability of crystalline inorganic materials solely from their chemical composition (i.e., elemental identity and stoichiometric ratios), without requiring crystal structure information, to identify which hypothetical compositions are likely to be experimentally realizable using current synthetic capabilities.

## Metadata

- Task ID: `task_9894db87334b`
- Source paper: [44 Synthesizability Crystalline Inorganic](../papers/44_Synthesizability_Crystalline_Inorganic.md)
- Tags: synthesizability prediction, composition-based classification, materials discovery

## Supporting Datasets

### [Inorganic Crystal Structure Database](../datasets/Inorganic_Crystal_Structure_Database.md)

- Usage page: [usage note](../dataset_uses/44_Synthesizability_Crystalline_Inorganic_Inorganic_Crystal_Structure_Database_dataset_use.md)
- Original title in paper: Inorganic Crystal Structure Database (ICSD)
- Link: https://doi.org/10.18434/M32147

A curated repository of experimentally synthesized and structurally characterized inorganic crystalline materials. The paper uses 53,594 unique binary, ternary, and quaternary compositions (8,194 binaries, 26,218 ternaries, 19,182 quaternaries) with integer stoichiometric coefficients, extracted from ICSD in October 2020. These serve as positive labeled examples (‘synthesized’) for training and evaluating the SynthNN model’s ability to predict synthesizability.

### [Synthesizability Dataset (author-curated)](../datasets/Synthesizability_Dataset_author-curated.md)

- Usage page: [usage note](../dataset_uses/44_Synthesizability_Crystalline_Inorganic_Synthesizability_Dataset_author-curated_dataset_.md)
- Original title in paper: Synthesizability Dataset (author-curated)
- Link: None

A custom dataset constructed by augmenting the ICSD-derived positive examples with artificially generated unsynthesized chemical formulas. Unsynthesized formulas are sampled to match the elemental abundance and distribution of compound types (binary/ternary/quaternary) in the ICSD subset; atomic coefficients are uniformly drawn from 1–20, and duplicates or multiples of known formulas are excluded. This dataset supports semi-supervised positive-unlabeled (PU) learning to train SynthNN as a synthesizability classifier, enabling robust generalization beyond known materials.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

# 44_Synthesizability_Crystalline_Inorganic - Synthesizability Dataset (author-curated)

## Dataset Use

A custom dataset constructed by augmenting the ICSD-derived positive examples with artificially generated unsynthesized chemical formulas. Unsynthesized formulas are sampled to match the elemental abundance and distribution of compound types (binary/ternary/quaternary) in the ICSD subset; atomic coefficients are uniformly drawn from 1–20, and duplicates or multiples of known formulas are excluded. This dataset supports semi-supervised positive-unlabeled (PU) learning to train SynthNN as a synthesizability classifier, enabling robust generalization beyond known materials.

## Links

- Paper: [44 Synthesizability Crystalline Inorganic](../papers/44_Synthesizability_Crystalline_Inorganic.md)
- Task: [task page](../tasks/44_Synthesizability_Crystalline_Inorganic_task_1.md)
- Dataset: [Synthesizability Dataset (author-curated)](../datasets/Synthesizability_Dataset_author-curated.md)
- Dataset URL: None

## Task Context

Predicting the synthesizability of crystalline inorganic materials solely from their chemical composition (i.e., elemental identity and stoichiometric ratios), without requiring crystal structure information, to identify which hypothetical compositions are likely to be experimentally realizable using current synthetic capabilities.

## Metadata

- Dataset use ID: `dataset_use_a310f3746d06`
- Original dataset title: Synthesizability Dataset (author-curated)
- Tags: synthesizability prediction, composition-based classification, materials discovery

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

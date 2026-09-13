# 61_Deep learning generative model for crystal structure prediction - CALYPSO dataset

## Dataset Use

A collection of crystal structures generated through prior CSP simulations using the CALYPSO code, contributed by the global CALYPSO user community; these structures are predominantly high-pressure configurations, DFT-relaxed under varied pressure conditions, and cover complex systems like superhydrides and superhard materials. In this paper, 571,736 structures were selected (after duplicate removal and filtering based on interatomic distance, cell volume, and energy ranking) to form the high-pressure component of the MP60-CALYPSO dataset, enabling the model to learn pressure-dependent structural motifs and lattice responses.

## Links

- Paper: [61 Deep learning generative model for crystal structure prediction](../papers/61_Deep_learning_generative_model_for_crystal_structure_prediction.md)
- Task: [task page](../tasks/61_Deep_learning_generative_model_for_crystal_structure_prediction_task_1.md)
- Dataset: [CALYPSO dataset](../datasets/CALYPSO_dataset.md)
- Dataset URL: http://www.calypso.cn

## Task Context

Predicting physically plausible crystal structures for a given chemical composition and external pressure condition, without requiring post-generation local optimization, to accelerate crystal structure prediction (CSP) — specifically, generating candidate structures that closely approximate local energy minima on the potential energy surface for subsequent validation or property evaluation.

## Metadata

- Dataset use ID: `dataset_use_1f87911c47ae`
- Original dataset title: CALYPSO dataset
- Tags: crystal structure prediction, conditional generation, pressure-aware structure generation

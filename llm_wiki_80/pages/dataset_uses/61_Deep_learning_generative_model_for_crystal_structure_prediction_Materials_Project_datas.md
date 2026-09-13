# 61_Deep learning generative model for crystal structure prediction - Materials Project

## Dataset Use

A public database containing nearly all experimentally stable inorganic crystal structures sourced from the Inorganic Crystal Structure Database (ICSD), supplemented by computationally predicted structures; structures are DFT-relaxed at ambient pressure and include metadata such as formation energy and energy above hull. In this work, MP contributes ~99,243 structures (with ≤60 atoms/unit cell, negative formation energy, and energy above hull ≤0.2 eV/atom) to the MP60-CALYPSO dataset, providing broad chemical diversity and serving as the ambient-pressure anchor for training the pressure-conditional generative model.

## Links

- Paper: [61 Deep learning generative model for crystal structure prediction](../papers/61_Deep_learning_generative_model_for_crystal_structure_prediction.md)
- Task: [task page](../tasks/61_Deep_learning_generative_model_for_crystal_structure_prediction_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting physically plausible crystal structures for a given chemical composition and external pressure condition, without requiring post-generation local optimization, to accelerate crystal structure prediction (CSP) — specifically, generating candidate structures that closely approximate local energy minima on the potential energy surface for subsequent validation or property evaluation.

## Metadata

- Dataset use ID: `dataset_use_41aef073409d`
- Original dataset title: Materials Project (MP) database
- Tags: crystal structure prediction, conditional generation, pressure-aware structure generation

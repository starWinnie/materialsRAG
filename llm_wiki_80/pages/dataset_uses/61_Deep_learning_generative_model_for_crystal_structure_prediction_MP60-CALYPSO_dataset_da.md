# 61_Deep learning generative model for crystal structure prediction - MP60-CALYPSO dataset

## Dataset Use

A curated, combined dataset of 670,979 locally stable crystal structures spanning 86 elements, 85,824 chemical compositions, and 114,733 structural prototypes; it integrates ambient-pressure experimental and theoretical structures from the Materials Project (MP) database (up to 60 atoms per unit cell) with high-pressure structures generated via CALYPSO-based CSP simulations by the broader CALYPSO user community. The dataset includes diverse hydrogen- and boron-rich phases (146,245 and 217,263 instances, respectively), all pre-relaxed using DFT, and is used to train and validate the conditional generative model (Cond-CDVAE) for composition- and pressure-conditioned crystal structure generation.

## Links

- Paper: [61 Deep learning generative model for crystal structure prediction](../papers/61_Deep_learning_generative_model_for_crystal_structure_prediction.md)
- Task: [task page](../tasks/61_Deep_learning_generative_model_for_crystal_structure_prediction_task_1.md)
- Dataset: [MP60-CALYPSO dataset](../datasets/MP60-CALYPSO_dataset.md)
- Dataset URL: None

## Task Context

Predicting physically plausible crystal structures for a given chemical composition and external pressure condition, without requiring post-generation local optimization, to accelerate crystal structure prediction (CSP) — specifically, generating candidate structures that closely approximate local energy minima on the potential energy surface for subsequent validation or property evaluation.

## Metadata

- Dataset use ID: `dataset_use_f24ca40f8dbe`
- Original dataset title: MP60-CALYPSO dataset
- Tags: crystal structure prediction, conditional generation, pressure-aware structure generation

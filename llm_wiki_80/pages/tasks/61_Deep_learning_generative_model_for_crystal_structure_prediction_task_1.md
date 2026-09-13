# 61_Deep learning generative model for crystal structure prediction - Task 1

## Task Description

Predicting physically plausible crystal structures for a given chemical composition and external pressure condition, without requiring post-generation local optimization, to accelerate crystal structure prediction (CSP) — specifically, generating candidate structures that closely approximate local energy minima on the potential energy surface for subsequent validation or property evaluation.

## Metadata

- Task ID: `task_39aecdbec872`
- Source paper: [61 Deep learning generative model for crystal structure prediction](../papers/61_Deep_learning_generative_model_for_crystal_structure_prediction.md)
- Tags: crystal structure prediction, conditional generation, pressure-aware structure generation

## Supporting Datasets

### [MP60-CALYPSO dataset](../datasets/MP60-CALYPSO_dataset.md)

- Usage page: [usage note](../dataset_uses/61_Deep_learning_generative_model_for_crystal_structure_prediction_MP60-CALYPSO_dataset_da.md)
- Original title in paper: MP60-CALYPSO dataset
- Link: None

A curated, combined dataset of 670,979 locally stable crystal structures spanning 86 elements, 85,824 chemical compositions, and 114,733 structural prototypes; it integrates ambient-pressure experimental and theoretical structures from the Materials Project (MP) database (up to 60 atoms per unit cell) with high-pressure structures generated via CALYPSO-based CSP simulations by the broader CALYPSO user community. The dataset includes diverse hydrogen- and boron-rich phases (146,245 and 217,263 instances, respectively), all pre-relaxed using DFT, and is used to train and validate the conditional generative model (Cond-CDVAE) for composition- and pressure-conditioned crystal structure generation.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/61_Deep_learning_generative_model_for_crystal_structure_prediction_Materials_Project_datas.md)
- Original title in paper: Materials Project (MP) database
- Link: https://materialsproject.org

A public database containing nearly all experimentally stable inorganic crystal structures sourced from the Inorganic Crystal Structure Database (ICSD), supplemented by computationally predicted structures; structures are DFT-relaxed at ambient pressure and include metadata such as formation energy and energy above hull. In this work, MP contributes ~99,243 structures (with ≤60 atoms/unit cell, negative formation energy, and energy above hull ≤0.2 eV/atom) to the MP60-CALYPSO dataset, providing broad chemical diversity and serving as the ambient-pressure anchor for training the pressure-conditional generative model.

### [CALYPSO dataset](../datasets/CALYPSO_dataset.md)

- Usage page: [usage note](../dataset_uses/61_Deep_learning_generative_model_for_crystal_structure_prediction_CALYPSO_dataset_dataset.md)
- Original title in paper: CALYPSO dataset
- Link: http://www.calypso.cn

A collection of crystal structures generated through prior CSP simulations using the CALYPSO code, contributed by the global CALYPSO user community; these structures are predominantly high-pressure configurations, DFT-relaxed under varied pressure conditions, and cover complex systems like superhydrides and superhard materials. In this paper, 571,736 structures were selected (after duplicate removal and filtering based on interatomic distance, cell volume, and energy ranking) to form the high-pressure component of the MP60-CALYPSO dataset, enabling the model to learn pressure-dependent structural motifs and lattice responses.

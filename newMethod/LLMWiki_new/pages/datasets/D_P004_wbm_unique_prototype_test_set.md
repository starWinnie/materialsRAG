# Dataset: WBM unique prototype test set

- Dataset ID: `D_P004_wbm_unique_prototype_test_set`
- Dataset type: `derived_subset`
- Source dataset: `D_wang_botti_marques_dataset`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- WBM unique prototype test set
- unique prototype test set
- cleaned WBM unique prototype test set

## Observed material scopes

- inorganic crystals

## Observed research tasks

- ML-guided materials discovery

## Observed research stages

- data_preparation
- label_generation
- model_evaluation
- candidate_screening

## Observed properties

- unrelaxed structures
- PBE formation energies of relaxed counterparts
- convex hull distances
- protostructures

## Observed fields

- unrelaxed structures
- PBE formation energies
- convex hull distances
- protostructures

## Usage evidence

- P004 (A framework to evaluate machine learning crystal stability predictions): test in Clean and filter WBM test set by protostructure matching — Serve as the cleaned, leakage-free test set for model evaluation
- P004 (A framework to evaluate machine learning crystal stability predictions): label_source in Compute convex hull distance labels for WBM structures — Compute convex hull distance labels for stability classification
- P004 (A framework to evaluate machine learning crystal stability predictions): test in Evaluate models on WBM test set using classification metrics — Evaluate model performance using classification metrics (F1, DAF, precision, recall) and regression metrics (MAE, RMSE, R2)
- P004 (A framework to evaluate machine learning crystal stability predictions): candidate_pool in Rank candidates by predicted hull distance for discovery campaigns — Rank candidates by predicted hull distance for discovery campaigns

## Dataset evidence

- P004, PDF page 8, Article: "To control for the potential adverse effects of leakage between the MP training set and the WBM test set, we cleaned the WBM test set based on protostructure matching. We refer to the combination of a materials prototype and the elemental assignment of its wyckoff positions as a protostructure following ref. 62. First we removed 524 pathological structures in WBM based on formation energies being larger than 5 eV per atom or smaller than −5 eV per atom. We then removed from the WBM test set all examples where the final protostructure of a WBM material matched the final protostructure of an MP material. In total, 11,175 materials were cleaned using this filter. We further removed all duplicated protostructures within WBM, keeping the lowest energy structure in each instance, leaving 215,488 structures in the unique prototype test set."

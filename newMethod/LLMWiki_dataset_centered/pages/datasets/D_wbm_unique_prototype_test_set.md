# Dataset: WBM unique prototype test set

- Dataset ID: `D_wbm_unique_prototype_test_set`
- Dataset type: `derived_subset`
- Source dataset: `D_wang_botti_marques_wbm_dataset`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- WBM unique prototype test set
- unique prototype test set
- unique protostructure subset

## Observed material scopes

- inorganic crystals

## Observed research tasks

- ML-guided materials discovery

## Observed research stages

- model_evaluation
- candidate_screening

## Observed properties

- unrelaxed structures
- DFT formation energies of corresponding DFT-relaxed structures
- convex hull distance

## Observed fields

- unrelaxed structures
- DFT formation energies
- convex hull distance

## Usage evidence

- P004 (A framework to evaluate machine learning crystal stability predictions): test in Evaluation of models on WBM test set using classification and regression metrics — Evaluation of models on WBM test set using classification and regression metrics.
- P004 (A framework to evaluate machine learning crystal stability predictions): candidate_pool in Ranking and screening of hypothetical materials by predicted hull distance — Ranking and screening of hypothetical materials by predicted hull distance.

## Dataset evidence

- P004, PDF page 8, Article: "First we removed 524 pathological structures in WBM based on formation energies being larger than 5 eV per atom or smaller than −5 eV per atom. We then removed from the WBM test set all examples where the final protostructure of a WBM material matched the final protostructure of an MP material. In total, 11,175 materials were cleaned using this filter. We further removed all duplicated protostructures within WBM, keeping the lowest energy structure in each instance, leaving 215,488 structures in the unique prototype test set."
- P004, PDF page 3, Results: "Table 1 shows performance metrics for all models included in the initial release of Matbench Discovery reported on the unique protostructure subset."

# Dataset: WBM unique protostructure test set

- Dataset ID: `D_P004_wbm_unique_protostructure_test_set`
- Dataset type: `derived_subset`
- Source dataset: `D_wang_botti_marques_wbm_dataset`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- WBM unique protostructure test set
- unique prototype test set

## Observed material scopes

- inorganic crystals

## Observed research tasks

- ML-guided materials discovery

## Observed research stages

- data_preparation
- label_generation
- candidate_generation

## Observed properties

- unrelaxed structures
- DFT-relaxed hull distances
- convex hull distance
- stability labels (EMP hull dist ≤ 0)

## Observed fields

- unrelaxed structures
- DFT-relaxed hull distances
- convex hull distance
- stability labels

## Usage evidence

- P004 (A framework to evaluate machine learning crystal stability predictions): test in cleaning and filtering WBM test set — Using cleaned, non-duplicated, non-leaking unrelaxed structures with DFT-relaxed hull distances for final evaluation
- P004 (A framework to evaluate machine learning crystal stability predictions): label_source in computing convex hull distance labels — Computing ground-truth thermodynamic stability labels (on/below vs. above convex hull) using MP training set convex hull
- P004 (A framework to evaluate machine learning crystal stability predictions): candidate_pool in ranking candidates by predicted hull distance — Ranking all WBM test structures by model-predicted convex hull distance to simulate prioritization in discovery campaign

## Dataset evidence

- P004, PDF page 8, Article: "We cleaned the WBM test set based on protostructure matching... leaving 215,488 structures in the unique prototype test set."
- P004, PDF page 8, Article: "Throughout this work, we define stability as being on or below the convex hull of the MP training set (EMP hull dist ≤ 0). In total, 32,942 of 215,488 materials in the WBM unique prototype test set satisfy this criterion."

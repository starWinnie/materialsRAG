# Dataset Use: WBM unique prototype test set

- DatasetUse ID: `DU_wbm_unique_prototype_test_set`
- Dataset: WBM unique prototype test set (`D_wbm_unique_prototype_test_set`)
- Papers: P004
- Usage records: 2

## Usage roles

- test
- candidate_pool

## Purposes

- Evaluation of models on WBM test set using classification and regression metrics.
- Ranking and screening of hypothetical materials by predicted hull distance.

## Used fields

- unrelaxed structures
- DFT formation energies
- convex hull distance

## Construction methods

- cleaned and deduplicated subset of WBM full dataset

## Filter conditions

- None stated

## Sample counts

- 215488

## Availability

- Dataset: public
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P004_04_wbm_unique_prototype_test_set

- Paper: `P004` — A framework to evaluate machine learning crystal stability predictions
- Task: ML-guided materials discovery (`T_P004_01`)
- Stage: Evaluation of models on WBM test set using classification and regression metrics (`model_evaluation`, `S_P004_04`)
- Usage role: test
- Purpose: Evaluation of models on WBM test set using classification and regression metrics.
- Used fields: unrelaxed structures, DFT formation energies, convex hull distance
- Filter conditions: Not stated
- Construction method: cleaned and deduplicated subset of WBM full dataset
- Sample count: 215488
- Confidence: 1.0

Evidence:
- P004, PDF page 8, Article: "First we removed 524 pathological structures in WBM based on formation energies being larger than 5 eV per atom or smaller than −5 eV per atom. We then removed from the WBM test set all examples where the final protostructure of a WBM material matched the final protostructure of an MP material. In total, 11,175 materials were cleaned using this filter. We further removed all duplicated protostructures within WBM, keeping the lowest energy structure in each instance, leaving 215,488 structures in the unique prototype test set."

### UR_P004_05_wbm_unique_prototype_test_set

- Paper: `P004` — A framework to evaluate machine learning crystal stability predictions
- Task: ML-guided materials discovery (`T_P004_01`)
- Stage: Ranking and screening of hypothetical materials by predicted hull distance (`candidate_screening`, `S_P004_05`)
- Usage role: candidate_pool
- Purpose: Ranking and screening of hypothetical materials by predicted hull distance.
- Used fields: unrelaxed structures
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P004, PDF page 5, Article: "A typical discovery campaign will rank hypothetical materials by model-predicted hull distance from most to least stable and validate the most stable predictions first."

## Aggregated evidence

- , PDF page 8, Article: "First we removed 524 pathological structures in WBM based on formation energies being larger than 5 eV per atom or smaller than −5 eV per atom. We then removed from the WBM test set all examples where the final protostructure of a WBM material matched the final protostructure of an MP material. In total, 11,175 materials were cleaned using this filter. We further removed all duplicated protostructures within WBM, keeping the lowest energy structure in each instance, leaving 215,488 structures in the unique prototype test set."
- , PDF page 5, Article: "A typical discovery campaign will rank hypothetical materials by model-predicted hull distance from most to least stable and validate the most stable predictions first."

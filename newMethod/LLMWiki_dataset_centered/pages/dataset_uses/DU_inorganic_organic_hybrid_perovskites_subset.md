# Dataset Use: Inorganic-organic hybrid perovskites subset

- DatasetUse ID: `DU_inorganic_organic_hybrid_perovskites_subset`
- Dataset: Inorganic-organic hybrid perovskites subset (`D_inorganic_organic_hybrid_perovskites_subset`)
- Papers: P033
- Usage records: 1

## Usage roles

- test

## Purposes

- Test dataset for hybrid perovskite-specific BPM evaluation

## Used fields

- chemical composition
- bandgap

## Construction methods

- subdivision of experimental_abx3_bandgap_227 based on material scope

## Filter conditions

- inorganic-organic hybrid perovskites

## Sample counts

- None stated

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P033_06_inorganic_organic_hybrid_perovskites_subset

- Paper: `P033` — Study on bandgap predications of ABX3-type perovskites by machine learning
- Task: bandgap prediction of ABX3-type perovskites (`T_P033_01`)
- Stage: selection of best-performing models per perovskite subclass (`candidate_screening`, `S_P033_06`)
- Usage role: test
- Purpose: Test dataset for hybrid perovskite-specific BPM evaluation
- Used fields: chemical composition, bandgap
- Filter conditions: inorganic-organic hybrid perovskites
- Construction method: subdivision of experimental_abx3_bandgap_227 based on material scope
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P033, PDF page 4, four: "Then we use the training dataset of all-inorganic perovskite (Table S3) and the training dataset of Tin-free perovskites (Table S7) to train BPM (algorithm is Xgboost), and the test dataset of organic hybrid (Table S6) to test the BPM (algorithm is Xgboost)."

## Aggregated evidence

- , PDF page 4, four: "Then we use the training dataset of all-inorganic perovskite (Table S3) and the training dataset of Tin-free perovskites (Table S7) to train BPM (algorithm is Xgboost), and the test dataset of organic hybrid (Table S6) to test the BPM (algorithm is Xgboost)."

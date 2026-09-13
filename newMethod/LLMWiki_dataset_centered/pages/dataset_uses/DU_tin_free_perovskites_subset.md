# Dataset Use: Tin-free perovskites subset

- DatasetUse ID: `DU_tin_free_perovskites_subset`
- Dataset: Tin-free perovskites subset (`D_tin_free_perovskites_subset`)
- Papers: P033
- Usage records: 1

## Usage roles

- training

## Purposes

- Training dataset for tin-free perovskite-specific BPM

## Used fields

- chemical composition
- bandgap

## Construction methods

- subdivision of experimental_abx3_bandgap_227 based on material scope

## Filter conditions

- tin-free perovskites

## Sample counts

- None stated

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P033_06_tin_free_perovskites_subset

- Paper: `P033` — Study on bandgap predications of ABX3-type perovskites by machine learning
- Task: bandgap prediction of ABX3-type perovskites (`T_P033_01`)
- Stage: selection of best-performing models per perovskite subclass (`candidate_screening`, `S_P033_06`)
- Usage role: training
- Purpose: Training dataset for tin-free perovskite-specific BPM
- Used fields: chemical composition, bandgap
- Filter conditions: tin-free perovskites
- Construction method: subdivision of experimental_abx3_bandgap_227 based on material scope
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P033, PDF page 4, four: "Then we use the training dataset of all-inorganic perovskite (Table S3) and the training dataset of Tin-free perovskites (Table S7) to train BPM (algorithm is Xgboost)"

## Aggregated evidence

- , PDF page 4, four: "Then we use the training dataset of all-inorganic perovskite (Table S3) and the training dataset of Tin-free perovskites (Table S7) to train BPM (algorithm is Xgboost)"

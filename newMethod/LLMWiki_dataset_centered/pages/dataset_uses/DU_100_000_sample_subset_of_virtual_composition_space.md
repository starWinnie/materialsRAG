# Dataset Use: 100,000-sample subset of virtual composition space

- DatasetUse ID: `DU_100_000_sample_subset_of_virtual_composition_space`
- Dataset: 100,000-sample subset of virtual composition space (`D_100_000_sample_subset_of_virtual_composition_space`)
- Papers: P036
- Usage records: 1

## Usage roles

- screening

## Purposes

- subset of virtual search space used for GBRT-P-based band gap prediction and target range screening

## Used fields

- composition

## Construction methods

- random sampling preserving feature space distribution

## Filter conditions

- not in original hoip_610_dataset
- predicted band gap in 1.3−1.4 eV or 1.7−2.1 eV

## Sample counts

- 100000

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P036_12_100_000_sample_subset_of_virtual_composition_space

- Paper: `P036` — Accelerating the Discovery of Hybrid Perovskites with Targeted Band Gaps via Interpretable Machine Learning
- Task: predicting the experimental band gap values of HOIPs (`T_P036_01`)
- Stage: target band gap screening using GBRT-P (`candidate_screening`, `S_P036_12`)
- Usage role: screening
- Purpose: subset of virtual search space used for GBRT-P-based band gap prediction and target range screening
- Used fields: composition
- Filter conditions: not in original hoip_610_dataset, predicted band gap in 1.3−1.4 eV or 1.7−2.1 eV
- Construction method: random sampling preserving feature space distribution
- Sample count: 100000
- Confidence: 1.0

Evidence:
- P036, PDF page 6, METHODS: "a random selection of 100,000 compositions which has the same feature space distribution as the initial prediction set was made for prediction using GBRT-P. Then, we selected compositions that are not in the original data set and whose band gaps are distributed in the range of 1.3−1.4 and 1.7−2.1 eV."

## Aggregated evidence

- , PDF page 6, METHODS: "a random selection of 100,000 compositions which has the same feature space distribution as the initial prediction set was made for prediction using GBRT-P. Then, we selected compositions that are not in the original data set and whose band gaps are distributed in the range of 1.3−1.4 and 1.7−2.1 eV."

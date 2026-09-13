# Dataset Use: ANI-1x

- DatasetUse ID: `DU_ani_1x`
- Dataset: ANI-1x (`D_ani_1x`)
- Papers: P034
- Usage records: 2

## Usage roles

- training
- test

## Purposes

- training MLIPs with PIWSL loss
- benchmarking models trained with PIWSL

## Used fields

- atomic configurations
- reference energies
- reference atomic forces

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 10000

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P034_01_ani_1x

- Paper: `P034` — Physics-Informed Weakly Supervised Learning for Interatomic Potentials
- Task: training machine-learned interatomic potentials (MLIPs) (`T_P034_01`)
- Stage: training MLIPs with PIWSL loss (`model_training`, `S_P034_01`)
- Usage role: training
- Purpose: training MLIPs with PIWSL loss
- Used fields: atomic configurations, reference energies, reference atomic forces
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P034, PDF page 5, 5.1. Models and Data Sets: "To evaluate the effect and dependency of the physics-informed weakly supervised approach in detail, we performed the training on various data sets: ANI-1x as a heterogeneous molecular data set (Smith et al., 2020)"

### UR_P034_02_ani_1x

- Paper: `P034` — Physics-Informed Weakly Supervised Learning for Interatomic Potentials
- Task: training machine-learned interatomic potentials (MLIPs) (`T_P034_01`)
- Stage: benchmarking models trained with PIWSL (`model_evaluation`, `S_P034_02`)
- Usage role: test
- Purpose: benchmarking models trained with PIWSL
- Used fields: atomic configurations, reference energies, reference atomic forces
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 10000
- Confidence: 1.0

Evidence:
- P034, PDF page 5, 5.2. Benchmark Results: "In the following, all evaluation metrics are computed for the test data set."
- P034, PDF page 14, Splitting Data Sets: "We used 10,000 test configurations for ANI-1x"

## Aggregated evidence

- , PDF page 5, 5.1. Models and Data Sets: "To evaluate the effect and dependency of the physics-informed weakly supervised approach in detail, we performed the training on various data sets: ANI-1x as a heterogeneous molecular data set (Smith et al., 2020)"
- , PDF page 5, 5.2. Benchmark Results: "In the following, all evaluation metrics are computed for the test data set."
- , PDF page 14, Splitting Data Sets: "We used 10,000 test configurations for ANI-1x"

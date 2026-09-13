# Dataset Use: Perovskite Halides Dataset

- DatasetUse ID: `DU_perovskite_halides_dataset`
- Dataset: Perovskite Halides Dataset (`D_perovskite_halides_dataset`)
- Papers: P005
- Usage records: 1

## Usage roles

- test

## Purposes

- Benchmark ECSG in unknown composition space (perovskite halides)

## Used fields

- chemical formula
- stability labels

## Construction methods

- extracted from literature and deduplicated against MP

## Filter conditions

- remove duplicate samples from MP

## Sample counts

- 496

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P005_05_perovskite_halides_dataset

- Paper: `P005` — Predicting thermodynamic stability of inorganic compounds using ensemble machine learning based on electron configuration
- Task: Predicting thermodynamic stability of inorganic compounds (`T_P005_01`)
- Stage: Benchmarking ECSG against state-of-the-art models using multiple metrics (`model_evaluation`, `S_P005_05`)
- Usage role: test
- Purpose: Benchmark ECSG in unknown composition space (perovskite halides)
- Used fields: chemical formula, stability labels
- Filter conditions: remove duplicate samples from MP
- Construction method: extracted from literature and deduplicated against MP
- Sample count: 496
- Confidence: 1.0

Evidence:
- P005, PDF page 8, Prediction in unknown space: "We collected thermodynamic stability data for 496 perovskite halides from the literature. Among these materials, there are 408 materials in the MP database. To ensure the perovskite halide data set is independent of the training set, we remove these duplicate samples from MP."

## Aggregated evidence

- , PDF page 8, Prediction in unknown space: "We collected thermodynamic stability data for 496 perovskite halides from the literature. Among these materials, there are 408 materials in the MP database. To ensure the perovskite halide data set is independent of the training set, we remove these duplicate samples from MP."

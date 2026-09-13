# Dataset: AFLOW

- Dataset ID: `D_aflow`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- AFLOW

## Observed material scopes

- solid-state materials

## Observed research tasks

- Out-of-Distribution Property Prediction

## Observed research stages

- data_acquisition
- label_generation
- candidate_screening
- model_evaluation

## Observed properties

- band gap
- bulk modulus
- Debye temperature
- shear modulus
- thermal conductivity
- thermal expansion

## Observed fields

- material compositions
- property values

## Usage evidence

- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): source in Curating benchmark datasets for solids and molecules — Benchmark for solid materials property prediction covering electronic, mechanical, thermal properties
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): candidate_pool in Defining OOD labels via top/bottom percentile thresholds — Defining OOD labels via top 5% highest property values
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): screening in Screening for top OOD candidates using extrapolative precision — Screening for top OOD candidates by identifying 30% of test samples with highest property values
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): benchmark in Evaluating OOD prediction accuracy and distributional alignment — Evaluating OOD prediction accuracy using mean absolute error (MAE), recall, and kernel density estimation (KDE) overlap

## Dataset evidence

- P017, PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- P017, PDF page 2, Results: "AFLOW contains material property values obtained from high-throughput calculations30."

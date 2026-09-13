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
- data_preparation
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

- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): benchmark in Curating benchmark datasets for solids and molecules — Evaluate extrapolation capability on solid materials property prediction tasks
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): training in Preprocessing representations and splitting datasets into ID/OOD sets — Train predictor models using stoichiometry-based representations for solids
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): screening in Selecting high-performing OOD candidates via top-k prediction — Identify top-performing OOD candidates by selecting the top 30% of test samples with highest predicted property values
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): test in Evaluating OOD prediction accuracy and distributional alignment — Evaluate OOD prediction accuracy and distributional alignment

## Dataset evidence

- P017, PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- P017, PDF page 2, Results: "AFLOW contains material property values obtained from high-throughput calculations30."

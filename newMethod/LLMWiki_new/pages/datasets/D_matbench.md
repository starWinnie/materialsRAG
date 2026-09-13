# Dataset: Matbench

- Dataset ID: `D_matbench`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Matbench

## Observed material scopes

- solid-state materials
- crystalline materials

## Observed research tasks

- Out-of-Distribution Property Prediction
- crystal material property prediction

## Observed research stages

- data_acquisition
- label_generation
- candidate_screening
- model_evaluation

## Observed properties

- band gap
- refractive index
- yield strength
- formation energy
- e form
- jdft2d

## Observed fields

- material compositions
- property values
- crystal structure (A, P, L)

## Usage evidence

- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): source in Curating benchmark datasets for solids and molecules — Benchmark for solid materials property prediction covering electronic, mechanical, thermal properties
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): candidate_pool in Defining OOD labels via top/bottom percentile thresholds — Defining OOD labels via top 5% highest property values
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): screening in Screening for top OOD candidates using extrapolative precision — Screening for top OOD candidates by identifying 30% of test samples with highest property values
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): benchmark in Evaluating OOD prediction accuracy and distributional alignment — Evaluating OOD prediction accuracy using mean absolute error (MAE), recall, and kernel density estimation (KDE) overlap
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): benchmark in using three widely-used crystal benchmarks — evaluate the expressiveness of iComFormer and eComFormer models

## Dataset evidence

- P017, PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- P017, PDF page 2, Results: "Matbench is an automated leaderboard for benchmarking ML algorithms predicting solid material properties12. Matbench contains three composition-based regression tasks: experimentally measured band gap14, experimentally measured yield strength of steels31, calculated formation energy32, and calculated refractive index33."
- P021, PDF page 8, 5 EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."

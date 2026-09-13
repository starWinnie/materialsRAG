# Dataset: Matbench

- Dataset ID: `D_matbench`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Matbench
- MB
- Matbench suite

## Observed material scopes

- crystals
- solid-state materials
- crystalline materials

## Observed research tasks

- Crystal Property Prediction
- Out-of-Distribution Property Prediction
- crystal material property prediction

## Observed research stages

- data_acquisition
- model_evaluation

## Observed properties

- exfoliation energy
- formation energy
- shear modulus
- refractive index
- band gap
- yield strength
- e form
- jdft2d

## Observed fields

- exfoliation energy
- formation energy
- shear modulus
- refractive index
- material composition
- property values
- crystal structure (A, P, L)
- e form
- jdft2d

## Usage evidence

- P001 (BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION): source in Retrieving datasets from official websites — retrieving benchmark dataset for evaluation
- P001 (BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION): test in Evaluating on Materials Project, JARVIS-DFT, and Matbench — evaluating model performance on crystal property prediction tasks
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): source in Dataset collection for solids and molecules — solid materials property prediction benchmark
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): source in using three widely-used crystal benchmarks — acquire crystal structure data and corresponding property labels for training and evaluation
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): benchmark in evaluating predictive accuracy on crystal benchmarks — evaluate the performance of the trained models on held-out test sets using standard metrics

## Dataset evidence

- P001, PDF page 8, EXPERIMENTS: "• Matbench (MB) Suite: We evaluate the models on several tasks from the Matbench suite (Dunn et al., 2020): matbench_jdft2d (636 entries; exfoliation energy), matbench_mp_e_form (132,752 entries; formation energy), matbench_log_gvrh (10,987 entries; shear modulus), and matbench_dielectric (4,764 entries; refractive index)."
- P017, PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- P017, PDF page 2, Results: "Matbench is an automated leaderboard for benchmarking ML algorithms predicting solid material properties12. Matbench contains three composition-based regression tasks: experimentally measured band gap14, experimentally measured yield strength of steels31, calculated formation energy32, and calculated refractive index33."
- P021, PDF page 8, EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."

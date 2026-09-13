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

## Observed material scopes

- crystals
- solid-state materials
- crystalline materials

## Observed research tasks

- Crystal Property Prediction
- Out-of-Distribution Property Prediction

## Observed research stages

- data_acquisition
- model_evaluation
- data_preparation
- candidate_screening

## Observed properties

- exfoliation energy
- formation energy
- shear modulus
- refractive index
- band gap
- yield strength
- bandgap

## Observed fields

- structure
- exfoliation energy
- formation energy
- shear modulus
- refractive index
- material compositions
- property values
- crystal structure (A, P, L)
- property labels

## Usage evidence

- P001 (BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION): source in Retrieving crystal datasets — retrieve crystal structure and property data for benchmarking
- P001 (BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION): test in Evaluating model performance on benchmark datasets — evaluate model performance on crystal property prediction tasks
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): benchmark in Curating benchmark datasets for solids and molecules — Evaluate extrapolation capability on solid materials property prediction tasks
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): training in Preprocessing representations and splitting datasets into ID/OOD sets — Train predictor models using stoichiometry-based representations for solids
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): screening in Selecting high-performing OOD candidates via top-k prediction — Identify top-performing OOD candidates by selecting the top 30% of test samples with highest predicted property values
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): test in Evaluating OOD prediction accuracy and distributional alignment — Evaluate OOD prediction accuracy and distributional alignment
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): benchmark in using three widely-used crystal benchmarks — acquire crystal structure data and corresponding property labels for training and evaluation
- P021 (COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION): benchmark in evaluating ComFormer variants on crystal benchmarks — assess the predictive accuracy of the trained models on various crystal property prediction tasks

## Dataset evidence

- P001, PDF page 8, Datasets: "• Matbench (MB) Suite: We evaluate the models on several tasks from the Matbench suite (Dunn et al., 2020): matbench_jdft2d (636 entries; exfoliation energy), matbench_mp_e_form (132,752 entries; formation energy), matbench_log_gvrh (10,987 entries; shear modulus), and matbench_dielectric (4,764 entries; refractive index)."
- P017, PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- P017, PDF page 2, Results: "Matbench is an automated leaderboard for benchmarking ML algorithms predicting solid material properties12. Matbench contains three composition-based regression tasks: experimentally measured band gap14, experimentally measured yield strength of steels31, calculated formation energy32, and calculated refractive index33."
- P021, PDF page 8, 5 EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."

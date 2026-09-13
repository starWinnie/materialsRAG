# Dataset Use: Matbench

- DatasetUse ID: `DU_matbench`
- Dataset: Matbench (`D_matbench`)
- Papers: P001, P017, P021
- Usage records: 5

## Usage roles

- source
- test
- benchmark

## Purposes

- retrieving benchmark dataset for evaluation
- evaluating model performance on crystal property prediction tasks
- solid materials property prediction benchmark
- acquire crystal structure data and corresponding property labels for training and evaluation
- evaluate the performance of the trained models on held-out test sets using standard metrics

## Used fields

- exfoliation energy
- formation energy
- shear modulus
- refractive index
- material composition
- property values
- crystal structure (A, P, L)
- e form
- jdft2d

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 37217

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P001_01_matbench

- Paper: `P001` — BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION
- Task: Crystal Property Prediction (`T_P001_01`)
- Stage: Retrieving datasets from official websites (`data_acquisition`, `S_P001_01`)
- Usage role: source
- Purpose: retrieving benchmark dataset for evaluation
- Used fields: exfoliation energy, formation energy, shear modulus, refractive index
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P001, PDF page 8, EXPERIMENTS: "• Matbench (MB) Suite: We evaluate the models on several tasks from the Matbench suite (Dunn et al., 2020): matbench_jdft2d (636 entries; exfoliation energy), matbench_mp_e_form (132,752 entries; formation energy), matbench_log_gvrh (10,987 entries; shear modulus), and matbench_dielectric (4,764 entries; refractive index)."

### UR_P001_04_matbench

- Paper: `P001` — BEYOND STRUCTURE: INVARIANT CRYSTAL PROPERTY PREDICTION WITH PSEUDO-PARTICLE RAY DIFFRACTION
- Task: Crystal Property Prediction (`T_P001_01`)
- Stage: Evaluating on Materials Project, JARVIS-DFT, and Matbench (`model_evaluation`, `S_P001_04`)
- Usage role: test
- Purpose: evaluating model performance on crystal property prediction tasks
- Used fields: exfoliation energy, formation energy, shear modulus, refractive index
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P001, PDF page 1, ABSTRACT: "Extensive experiments are conducted on Materials Project, JARVIS-DFT, and MatBench, demonstrating that the proposed model achieves state-of-the-art performance."
- P001, PDF page 8, EXPERIMENTS: "• Matbench (MB) Suite: We evaluate the models on several tasks from the Matbench suite (Dunn et al., 2020): matbench_jdft2d (636 entries; exfoliation energy), matbench_mp_e_form (132,752 entries; formation energy), matbench_log_gvrh (10,987 entries; shear modulus), and matbench_dielectric (4,764 entries; refractive index)."

### UR_P017_01_matbench

- Paper: `P017` — Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules
- Task: Out-of-Distribution Property Prediction (`T_P017_01`)
- Stage: Dataset collection for solids and molecules (`data_acquisition`, `S_P017_01`)
- Usage role: source
- Purpose: solid materials property prediction benchmark
- Used fields: material composition, property values
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 37217
- Confidence: 1.0

Evidence:
- P017, PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- P017, PDF page 2, Results: "The datasets vary in size, ranging from approximately 300 to 14,000 samples."
- P017, PDF page 3, Table 1: "Formation Energy [eV/atom] 37217"

### UR_P021_01_matbench

- Paper: `P021` — COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION
- Task: crystal material property prediction (`T_P021_01`)
- Stage: using three widely-used crystal benchmarks (`data_acquisition`, `S_P021_01`)
- Usage role: source
- Purpose: acquire crystal structure data and corresponding property labels for training and evaluation
- Used fields: crystal structure (A, P, L), e form, jdft2d
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P021, PDF page 8, EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."

### UR_P021_04_matbench

- Paper: `P021` — COMPLETE AND EFFICIENT GRAPH TRANSFORMERS FOR CRYSTAL MATERIAL PROPERTY PREDICTION
- Task: crystal material property prediction (`T_P021_01`)
- Stage: evaluating predictive accuracy on crystal benchmarks (`model_evaluation`, `S_P021_04`)
- Usage role: benchmark
- Purpose: evaluate the performance of the trained models on held-out test sets using standard metrics
- Used fields: e form, jdft2d
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P021, PDF page 8, EXPERIMENTS: "To further evaluate the performances, we use e form with 132752 crystals and jdft2d with only 636 2D crystals in MatBench."

## Aggregated evidence

- , PDF page 8, EXPERIMENTS: "• Matbench (MB) Suite: We evaluate the models on several tasks from the Matbench suite (Dunn et al., 2020): matbench_jdft2d (636 entries; exfoliation energy), matbench_mp_e_form (132,752 entries; formation energy), matbench_log_gvrh (10,987 entries; shear modulus), and matbench_dielectric (4,764 entries; refractive index)."
- , PDF page 1, ABSTRACT: "Extensive experiments are conducted on Materials Project, JARVIS-DFT, and MatBench, demonstrating that the proposed model achieves state-of-the-art performance."
- , PDF page 8, EXPERIMENTS: "• Matbench (MB) Suite: We evaluate the models on several tasks from the Matbench suite (Dunn et al., 2020): matbench_jdft2d (636 entries; exfoliation energy), matbench_mp_e_form (132,752 entries; formation energy), matbench_log_gvrh (10,987 entries; shear modulus), and matbench_dielectric (4,764 entries; refractive index)."
- , PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- , PDF page 2, Results: "The datasets vary in size, ranging from approximately 300 to 14,000 samples."
- , PDF page 3, Table 1: "Formation Energy [eV/atom] 37217"
- , PDF page 8, EXPERIMENTS: "We assess the expressiveness of our iComFormer and eComFormer models by conducting evaluations on three widely-used crystal benchmarks: JARVIS (Choudhary et al., 2020), the Materials Project (Chen et al., 2019), and MatBench (Dunn et al., 2020)."
- , PDF page 8, EXPERIMENTS: "To further evaluate the performances, we use e form with 132752 crystals and jdft2d with only 636 2D crystals in MatBench."

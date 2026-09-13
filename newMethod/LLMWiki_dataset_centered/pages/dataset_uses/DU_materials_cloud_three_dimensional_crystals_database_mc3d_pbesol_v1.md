# Dataset Use: Materials Cloud three-dimensional crystals database (MC3D) PBEsol-v1

- DatasetUse ID: `DU_materials_cloud_three_dimensional_crystals_database_mc3d_pbesol_v1`
- Dataset: Materials Cloud three-dimensional crystals database (MC3D) PBEsol-v1 (`D_materials_cloud_three_dimensional_crystals_database_mc3d_pbesol_v1`)
- Papers: P035
- Usage records: 2

## Usage roles

- source

## Purposes

- Provide DFT formation energies (PBEsol-v1) for cross-validation and baseline comparison against experimental data and other DFT databases.
- Provide source formation energies (PBEsol) for computing target deltas (δ∆HPBEsol_f) in the delta-learning framework.

## Used fields

- formation energy

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 1384

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P035_02_materials_cloud_three_dimensional_crystals_database_mc3d_pbesol_v1

- Paper: `P035` — Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning
- Task: Correcting DFT formation energies towards experimental accuracy (`T_P035_01`)
- Stage: Acquiring DFT formation energy datasets (`data_acquisition`, `S_P035_02`)
- Usage role: source
- Purpose: Provide DFT formation energies (PBEsol-v1) for cross-validation and baseline comparison against experimental data and other DFT databases.
- Used fields: formation energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P035, PDF page 10, METHODS: "In addition to the comparison with experimental data, the MC3D formation energies are compared against the established high-throughput databases Materials Project [7, 8] and Open Quantum Materials Database [10]. We query the OQMD v1.5 (locally hosted) and MP v2023.11.1, and match structures by their ICSD ID."

### UR_P035_04_materials_cloud_three_dimensional_crystals_database_mc3d_pbesol_v1

- Paper: `P035` — Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning
- Task: Correcting DFT formation energies towards experimental accuracy (`T_P035_01`)
- Stage: Training classical ML models in delta-learning framework (`model_training`, `S_P035_04`)
- Usage role: source
- Purpose: Provide source formation energies (PBEsol) for computing target deltas (δ∆HPBEsol_f) in the delta-learning framework.
- Used fields: formation energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 1384
- Confidence: 1.0

Evidence:
- P035, PDF page 5, RESULTS: "The three models from the Methods section (Random Forest (RF) [69], Kernel Ridge Regression (KRR) [70] with a RBF and Laplacian (LAP) kernel, Gaussian Process Regression (GPR) [71]) are trained on two targets: (i) δ∆HPBEsol_f, the difference between PBEsol formation energies and experiment, and (ii) δ∆HMLIP_f, the difference between zero-shot r2SCAN MLIP formation energies (on top of the PBEsol structures) and experiment."
- P035, PDF page 10, METHODS: "The dataset of 1384 structures with experimental references is divided into a 80/20 train-test split."

## Aggregated evidence

- , PDF page 10, METHODS: "In addition to the comparison with experimental data, the MC3D formation energies are compared against the established high-throughput databases Materials Project [7, 8] and Open Quantum Materials Database [10]. We query the OQMD v1.5 (locally hosted) and MP v2023.11.1, and match structures by their ICSD ID."
- , PDF page 5, RESULTS: "The three models from the Methods section (Random Forest (RF) [69], Kernel Ridge Regression (KRR) [70] with a RBF and Laplacian (LAP) kernel, Gaussian Process Regression (GPR) [71]) are trained on two targets: (i) δ∆HPBEsol_f, the difference between PBEsol formation energies and experiment, and (ii) δ∆HMLIP_f, the difference between zero-shot r2SCAN MLIP formation energies (on top of the PBEsol structures) and experiment."
- , PDF page 10, METHODS: "The dataset of 1384 structures with experimental references is divided into a 80/20 train-test split."

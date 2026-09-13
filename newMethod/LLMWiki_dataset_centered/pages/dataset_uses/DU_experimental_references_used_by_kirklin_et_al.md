# Dataset Use: experimental references used by Kirklin et al.

- DatasetUse ID: `DU_experimental_references_used_by_kirklin_et_al`
- Dataset: experimental references used by Kirklin et al. (`D_experimental_references_used_by_kirklin_et_al`)
- Papers: P035
- Usage records: 2

## Usage roles

- label_source

## Purposes

- Serve as ground truth experimental formation enthalpy references for evaluating and correcting DFT formation energies.
- Provide target deltas (δ∆HPBEsol_f and δ∆HMLIP_f) for training classical ML models in the delta-learning framework.

## Used fields

- formation enthalpy

## Construction methods

- delta calculation: difference between PBEsol formation energies and experiment, and difference between zero-shot r2SCAN MLIP formation energies and experiment

## Filter conditions

- compounds not elemental phases
- experimental uncertainty estimate does not exceed 10%
- DFT formation energy (from OQMD) and experimental reference differ by no more than 0.5 eV/atom
- when appearing in both datasets, sources differ by no more than 150 meV/atom

## Sample counts

- 1297
- 2726

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P035_01_experimental_references_used_by_kirklin_et_al

- Paper: `P035` — Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning
- Task: Correcting DFT formation energies towards experimental accuracy (`T_P035_01`)
- Stage: Acquiring experimental formation enthalpy references (`data_acquisition`, `S_P035_01`)
- Usage role: label_source
- Purpose: Serve as ground truth experimental formation enthalpy references for evaluating and correcting DFT formation energies.
- Used fields: formation enthalpy
- Filter conditions: compounds not elemental phases, experimental uncertainty estimate does not exceed 10%, DFT formation energy (from OQMD) and experimental reference differ by no more than 0.5 eV/atom, when appearing in both datasets, sources differ by no more than 150 meV/atom
- Construction method: Not stated
- Sample count: 2726
- Confidence: 1.0

Evidence:
- P035, PDF page 9, METHODS: "To assess the performance of the DFT calculated formation energies, we use the experimental references collected by Wang et al. [43] and published in the matminer package [73] as the expt formation enthalpy kingsbury dataset [43, 81–87]. To increase the amount and diversity of experimental reference data, which is typically the limiting factor in data-driven studies, we combine this with the experimental references used by Kirklin et al. [10], yielding 2726 unique compounds in total."

### UR_P035_04_experimental_references_used_by_kirklin_et_al

- Paper: `P035` — Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning
- Task: Correcting DFT formation energies towards experimental accuracy (`T_P035_01`)
- Stage: Training classical ML models in delta-learning framework (`model_training`, `S_P035_04`)
- Usage role: label_source
- Purpose: Provide target deltas (δ∆HPBEsol_f and δ∆HMLIP_f) for training classical ML models in the delta-learning framework.
- Used fields: formation enthalpy
- Filter conditions: compounds not elemental phases, experimental uncertainty estimate does not exceed 10%, DFT formation energy (from OQMD) and experimental reference differ by no more than 0.5 eV/atom, when appearing in both datasets, sources differ by no more than 150 meV/atom
- Construction method: delta calculation: difference between PBEsol formation energies and experiment, and difference between zero-shot r2SCAN MLIP formation energies and experiment
- Sample count: 1297
- Confidence: 1.0

Evidence:
- P035, PDF page 5, RESULTS: "The three models from the Methods section (Random Forest (RF) [69], Kernel Ridge Regression (KRR) [70] with a RBF and Laplacian (LAP) kernel, Gaussian Process Regression (GPR) [71]) are trained on two targets: (i) δ∆HPBEsol_f, the difference between PBEsol formation energies and experiment, and (ii) δ∆HMLIP_f, the difference between zero-shot r2SCAN MLIP formation energies (on top of the PBEsol structures) and experiment."
- P035, PDF page 9, METHODS: "Since MC3D does not contain all compounds, merging with the experimental references yields 1552 (PBE) and 1384 (PBEsol) compounds, of which 1297 overlap."

## Aggregated evidence

- , PDF page 9, METHODS: "To assess the performance of the DFT calculated formation energies, we use the experimental references collected by Wang et al. [43] and published in the matminer package [73] as the expt formation enthalpy kingsbury dataset [43, 81–87]. To increase the amount and diversity of experimental reference data, which is typically the limiting factor in data-driven studies, we combine this with the experimental references used by Kirklin et al. [10], yielding 2726 unique compounds in total."
- , PDF page 5, RESULTS: "The three models from the Methods section (Random Forest (RF) [69], Kernel Ridge Regression (KRR) [70] with a RBF and Laplacian (LAP) kernel, Gaussian Process Regression (GPR) [71]) are trained on two targets: (i) δ∆HPBEsol_f, the difference between PBEsol formation energies and experiment, and (ii) δ∆HMLIP_f, the difference between zero-shot r2SCAN MLIP formation energies (on top of the PBEsol structures) and experiment."
- , PDF page 9, METHODS: "Since MC3D does not contain all compounds, merging with the experimental references yields 1552 (PBE) and 1384 (PBEsol) compounds, of which 1297 overlap."

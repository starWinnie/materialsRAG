# Dataset Use: revised MD17

- DatasetUse ID: `DU_revised_md17`
- Dataset: revised MD17 (`D_revised_md17`)
- Papers: P034
- Usage records: 3

## Usage roles

- training
- test
- experimental_validation

## Purposes

- training MLIPs with PIWSL loss
- benchmarking models trained with PIWSL
- evaluating robustness during MD simulations

## Used fields

- atomic configurations
- reference energies
- reference atomic forces

## Construction methods

- subset selection

## Filter conditions

- aspirin molecule

## Sample counts

- 10000

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P034_01_revised_md17

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
- P034, PDF page 5, 5.1. Models and Data Sets: "To evaluate the effect and dependency of the physics-informed weakly supervised approach in detail, we performed the training on various data sets: ... the revised MD17 (rMD17) data set containing small molecules with sampled configurational spaces for each (Chmiela et al., 2017; 2018; Christensen & von Lilienfeld, 2020)"

### UR_P034_02_revised_md17

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
- P034, PDF page 14, Splitting Data Sets: "for the rMD17 data set, following (Fu et al., 2023), we used 9000 configurations as a validation data set and another 10,000 for testing."

### UR_P034_03_revised_md17

- Paper: `P034` — Physics-Informed Weakly Supervised Learning for Interatomic Potentials
- Task: training machine-learned interatomic potentials (MLIPs) (`T_P034_01`)
- Stage: evaluating robustness during MD simulations (`experimental_validation`, `S_P034_03`)
- Usage role: experimental_validation
- Purpose: evaluating robustness during MD simulations
- Used fields: atomic configurations
- Filter conditions: aspirin molecule
- Construction method: subset selection
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P034, PDF page 7, 5.3. Qualitative Impact of PIWSL: "To further assess PIWSL’s impact, we evaluate the robustness during MD simulations of the MLIP models trained with and without PIWSL. We consider MD simulations of the aspirin molecule, with corresponding results presented in figure 3."

## Aggregated evidence

- , PDF page 5, 5.1. Models and Data Sets: "To evaluate the effect and dependency of the physics-informed weakly supervised approach in detail, we performed the training on various data sets: ... the revised MD17 (rMD17) data set containing small molecules with sampled configurational spaces for each (Chmiela et al., 2017; 2018; Christensen & von Lilienfeld, 2020)"
- , PDF page 14, Splitting Data Sets: "for the rMD17 data set, following (Fu et al., 2023), we used 9000 configurations as a validation data set and another 10,000 for testing."
- , PDF page 7, 5.3. Qualitative Impact of PIWSL: "To further assess PIWSL’s impact, we evaluate the robustness during MD simulations of the MLIP models trained with and without PIWSL. We consider MD simulations of the aspirin molecule, with corresponding results presented in figure 3."

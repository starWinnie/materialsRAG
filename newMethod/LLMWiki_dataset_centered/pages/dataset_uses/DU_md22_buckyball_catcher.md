# Dataset Use: MD22 buckyball catcher

- DatasetUse ID: `DU_md22_buckyball_catcher`
- Dataset: MD22 buckyball catcher (`D_md22_buckyball_catcher`)
- Papers: P034
- Usage records: 1

## Usage roles

- candidate_pool

## Purposes

- fine-tuning foundation models with PIWSL

## Used fields

- atomic configurations
- reference energies
- reference atomic forces

## Construction methods

- subset selection

## Filter conditions

- buckyball catcher molecule

## Sample counts

- 50

## Availability

- Dataset: public
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P034_04_md22_buckyball_catcher

- Paper: `P034` — Physics-Informed Weakly Supervised Learning for Interatomic Potentials
- Task: training machine-learned interatomic potentials (MLIPs) (`T_P034_01`)
- Stage: fine-tuning foundation models with PIWSL (`candidate_screening`, `S_P034_04`)
- Usage role: candidate_pool
- Purpose: fine-tuning foundation models with PIWSL
- Used fields: atomic configurations, reference energies, reference atomic forces
- Filter conditions: buckyball catcher molecule
- Construction method: subset selection
- Sample count: 50
- Confidence: 1.0

Evidence:
- P034, PDF page 8, 5.4. Fine-Tuning of Foundation Models: "We also evaluate the impact of PIWSL on data sets containing conformations of a single large molecule. For this purpose, we have chosen the buckyball catcher molecule from the MD22 data set (Chmiela et al., 2023) with 148 atoms."
- P034, PDF page 8, 5.4. Fine-Tuning of Foundation Models: "both models were trained using only 50 samples."

## Aggregated evidence

- , PDF page 8, 5.4. Fine-Tuning of Foundation Models: "We also evaluate the impact of PIWSL on data sets containing conformations of a single large molecule. For this purpose, we have chosen the buckyball catcher molecule from the MD22 data set (Chmiela et al., 2023) with 148 atoms."
- , PDF page 8, 5.4. Fine-Tuning of Foundation Models: "both models were trained using only 50 samples."

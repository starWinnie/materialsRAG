# Dataset Use: MD17(CCSD)

- DatasetUse ID: `DU_md17_ccsd`
- Dataset: MD17(CCSD) (`D_md17_ccsd`)
- Papers: P034
- Usage records: 1

## Usage roles

- candidate_pool

## Purposes

- fine-tuning foundation models with PIWSL

## Used fields

- atomic configurations
- reference energies

## Construction methods

- subset selection and label restriction

## Filter conditions

- aspirin data
- without force labels

## Sample counts

- 950

## Availability

- Dataset: public
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P034_04_md17_ccsd

- Paper: `P034` — Physics-Informed Weakly Supervised Learning for Interatomic Potentials
- Task: training machine-learned interatomic potentials (MLIPs) (`T_P034_01`)
- Stage: fine-tuning foundation models with PIWSL (`candidate_screening`, `S_P034_04`)
- Usage role: candidate_pool
- Purpose: fine-tuning foundation models with PIWSL
- Used fields: atomic configurations, reference energies
- Filter conditions: aspirin data, without force labels
- Construction method: subset selection and label restriction
- Sample count: 950
- Confidence: 1.0

Evidence:
- P034, PDF page 8, 5.4. Fine-Tuning of Foundation Models: "Table 3: Results for models trained on the MD17(CCSD) data set without reference atomic forces. All models are trained on aspirin data without force labels."
- P034, PDF page 23, E.5. Training setup for MD17-CCSD(T) Experiments: "The data includes 1500 samples which are splitted into 950/50/500 as train/validation/test datasets."

## Aggregated evidence

- , PDF page 8, 5.4. Fine-Tuning of Foundation Models: "Table 3: Results for models trained on the MD17(CCSD) data set without reference atomic forces. All models are trained on aspirin data without force labels."
- , PDF page 23, E.5. Training setup for MD17-CCSD(T) Experiments: "The data includes 1500 samples which are splitted into 950/50/500 as train/validation/test datasets."

# Dataset Use: DFT-calculated formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems

- DatasetUse ID: `DU_dft_calculated_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems`
- Dataset: DFT-calculated formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems (`D_dft_calculated_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems`)
- Papers: P043
- Usage records: 3

## Usage roles

- source
- training
- test

## Purposes

- Compute enthalpy correction labels Hcorr = HDFT − Hexpt.
- Provide input features (via derived Hcorr labels) for supervised training of the neural network regressor.
- Evaluate model performance via cross-validation on held-out data (to compute Hpred and compare against Hexpt).

## Used fields

- DFT formation enthalpy

## Construction methods

- Subtraction from experimental formation enthalpies.

## Filter conditions

- None stated

## Sample counts

- 25

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

0.94

## Usage records

### UR_P043_03_dft_calculated_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems

- Paper: `P043` — Machine learning for improved density functional theory thermodynamics
- Task: correcting DFT-calculated formation enthalpy errors (`T_P043_01`)
- Stage: calculating enthalpy correction labels (Hcorr) (`label_generation`, `S_P043_03`)
- Usage role: source
- Purpose: Compute enthalpy correction labels Hcorr = HDFT − Hexpt.
- Used fields: DFT formation enthalpy
- Filter conditions: Not stated
- Construction method: Subtraction from experimental formation enthalpies.
- Sample count: Not stated
- Confidence: 0.98

Evidence:
- P043, PDF page 3: "The error inherent in DFT calculations (that has its origin from the approximation used for the exchange and correlation functional) can be quantified as the difference between the experimental and theoretical determined enthalpy of formation. Hence, we introduce the term Hcorr as Hcorr = HDFT − Hexpt,"

### UR_P043_04_dft_calculated_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems

- Paper: `P043` — Machine learning for improved density functional theory thermodynamics
- Task: correcting DFT-calculated formation enthalpy errors (`T_P043_01`)
- Stage: training neural network regressor (`model_training`, `S_P043_04`)
- Usage role: training
- Purpose: Provide input features (via derived Hcorr labels) for supervised training of the neural network regressor.
- Used fields: DFT formation enthalpy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 25
- Confidence: 0.96

Evidence:
- P043, PDF page 4, Results and discussion: "These systems were randomly divided into a ML training set, with approximately 3/4 of the data used for model training, and a test set, consisting of about 1/4 of the data."
- P043, PDF page 5: "With approximately 25 structures in the training set, the RMSE on the prediction set falls down to 10 meV/atom, demonstrating a substantial improvement in predictive accuracy."

### UR_P043_05_dft_calculated_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems

- Paper: `P043` — Machine learning for improved density functional theory thermodynamics
- Task: correcting DFT-calculated formation enthalpy errors (`T_P043_01`)
- Stage: evaluating model performance with cross-validation (`model_evaluation`, `S_P043_05`)
- Usage role: test
- Purpose: Evaluate model performance via cross-validation on held-out data (to compute Hpred and compare against Hexpt).
- Used fields: DFT formation enthalpy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 0.94

Evidence:
- P043, PDF page 4, Results and discussion: "These systems were randomly divided into a ML training set, with approximately 3/4 of the data used for model training, and a test set, consisting of about 1/4 of the data."

## Aggregated evidence

- , PDF page 3: "The error inherent in DFT calculations (that has its origin from the approximation used for the exchange and correlation functional) can be quantified as the difference between the experimental and theoretical determined enthalpy of formation. Hence, we introduce the term Hcorr as Hcorr = HDFT − Hexpt,"
- , PDF page 4, Results and discussion: "These systems were randomly divided into a ML training set, with approximately 3/4 of the data used for model training, and a test set, consisting of about 1/4 of the data."
- , PDF page 5: "With approximately 25 structures in the training set, the RMSE on the prediction set falls down to 10 meV/atom, demonstrating a substantial improvement in predictive accuracy."
- , PDF page 4, Results and discussion: "These systems were randomly divided into a ML training set, with approximately 3/4 of the data used for model training, and a test set, consisting of about 1/4 of the data."

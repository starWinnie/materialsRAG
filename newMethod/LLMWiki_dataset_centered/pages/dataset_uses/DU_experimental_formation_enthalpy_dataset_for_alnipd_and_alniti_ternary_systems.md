# Dataset Use: Experimental formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems

- DatasetUse ID: `DU_experimental_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems`
- Dataset: Experimental formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems (`D_experimental_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems`)
- Papers: P043
- Usage records: 5

## Usage roles

- label_source
- training
- test
- screening

## Purposes

- Serve as ground truth labels for training and evaluation of the ML correction model.
- Compute enthalpy correction labels Hcorr = HDFT − Hexpt.
- Provide target labels (Hcorr) for supervised training of the neural network regressor.
- Evaluate model performance via cross-validation on held-out data.
- Compare linear vs. neural network correction models by computing RMSE against experimental Hcorr.

## Used fields

- enthalpy of formation

## Construction methods

- Filtered to exclude missing or unreliable enthalpy values.
- Subtraction from DFT-calculated formation enthalpies.

## Filter conditions

- exclude missing or unreliable enthalpy values
- only well-defined data points

## Sample counts

- 25
- 34

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

0.93

## Usage records

### UR_P043_01_experimental_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems

- Paper: `P043` — Machine learning for improved density functional theory thermodynamics
- Task: correcting DFT-calculated formation enthalpy errors (`T_P043_01`)
- Stage: acquiring experimental formation enthalpy data (`data_acquisition`, `S_P043_01`)
- Usage role: label_source
- Purpose: Serve as ground truth labels for training and evaluation of the ML correction model.
- Used fields: enthalpy of formation
- Filter conditions: exclude missing or unreliable enthalpy values, only well-defined data points
- Construction method: Filtered to exclude missing or unreliable enthalpy values.
- Sample count: 34
- Confidence: 0.99

Evidence:
- P043, PDF page 3: "A training dataset of reliable experimental values of the enthalphy of formation is initially filtered to exclude missing or unreliable enthalpy values, ensuring that only well-defined data points are used for training of the neural network."
- P043, PDF page 4, Results and discussion: "We have performed DFT calculations, as described above, for all the known enthalpies of formation of the two ternary phase diagrams, for Al–Ni–Pd and Al–Ni–Ti, at ambient conditions, resulting in a total of 34 systems."

### UR_P043_03_experimental_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems

- Paper: `P043` — Machine learning for improved density functional theory thermodynamics
- Task: correcting DFT-calculated formation enthalpy errors (`T_P043_01`)
- Stage: calculating enthalpy correction labels (Hcorr) (`label_generation`, `S_P043_03`)
- Usage role: label_source
- Purpose: Compute enthalpy correction labels Hcorr = HDFT − Hexpt.
- Used fields: enthalpy of formation
- Filter conditions: Not stated
- Construction method: Subtraction from DFT-calculated formation enthalpies.
- Sample count: Not stated
- Confidence: 0.98

Evidence:
- P043, PDF page 3: "The error inherent in DFT calculations (that has its origin from the approximation used for the exchange and correlation functional) can be quantified as the difference between the experimental and theoretical determined enthalpy of formation. Hence, we introduce the term Hcorr as Hcorr = HDFT − Hexpt,"

### UR_P043_04_experimental_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems

- Paper: `P043` — Machine learning for improved density functional theory thermodynamics
- Task: correcting DFT-calculated formation enthalpy errors (`T_P043_01`)
- Stage: training neural network regressor (`model_training`, `S_P043_04`)
- Usage role: training
- Purpose: Provide target labels (Hcorr) for supervised training of the neural network regressor.
- Used fields: enthalpy of formation
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 25
- Confidence: 0.97

Evidence:
- P043, PDF page 4, Results and discussion: "These systems were randomly divided into a ML training set, with approximately 3/4 of the data used for model training, and a test set, consisting of about 1/4 of the data."
- P043, PDF page 5: "With approximately 25 structures in the training set, the RMSE on the prediction set falls down to 10 meV/atom, demonstrating a substantial improvement in predictive accuracy."

### UR_P043_05_experimental_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems

- Paper: `P043` — Machine learning for improved density functional theory thermodynamics
- Task: correcting DFT-calculated formation enthalpy errors (`T_P043_01`)
- Stage: evaluating model performance with cross-validation (`model_evaluation`, `S_P043_05`)
- Usage role: test
- Purpose: Evaluate model performance via cross-validation on held-out data.
- Used fields: enthalpy of formation
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 0.95

Evidence:
- P043, PDF page 4, Results and discussion: "These systems were randomly divided into a ML training set, with approximately 3/4 of the data used for model training, and a test set, consisting of about 1/4 of the data."

### UR_P043_06_experimental_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems

- Paper: `P043` — Machine learning for improved density functional theory thermodynamics
- Task: correcting DFT-calculated formation enthalpy errors (`T_P043_01`)
- Stage: comparing linear vs. neural network correction models (`candidate_screening`, `S_P043_06`)
- Usage role: screening
- Purpose: Compare linear vs. neural network correction models by computing RMSE against experimental Hcorr.
- Used fields: enthalpy of formation
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 0.93

Evidence:
- P043, PDF page 2: "A simple linear correction, based on known enthalpy differences between DFT-calculated and experimentally measured values, provides a visible yet limited improvement. By applying machine learning techniques, specifically neural networks with supervised training, the predictive accuracy is significantly enhanced, enabling a more reliable determination of phase stability."
- P043, PDF page 6: "While the linear model offers some level of correction, its predictive power is ultimately constrained by its functional form. Even with interaction terms such as xAxB and xAxBxC, it cannot fully account for the intricate relationships governing enthalpy corrections. The neural network, in contrast, demonstrates a much greater ability to capture these relationships, leading to a substantial improvement in predictive accuracy."

## Aggregated evidence

- , PDF page 3: "A training dataset of reliable experimental values of the enthalphy of formation is initially filtered to exclude missing or unreliable enthalpy values, ensuring that only well-defined data points are used for training of the neural network."
- , PDF page 4, Results and discussion: "We have performed DFT calculations, as described above, for all the known enthalpies of formation of the two ternary phase diagrams, for Al–Ni–Pd and Al–Ni–Ti, at ambient conditions, resulting in a total of 34 systems."
- , PDF page 3: "The error inherent in DFT calculations (that has its origin from the approximation used for the exchange and correlation functional) can be quantified as the difference between the experimental and theoretical determined enthalpy of formation. Hence, we introduce the term Hcorr as Hcorr = HDFT − Hexpt,"
- , PDF page 4, Results and discussion: "These systems were randomly divided into a ML training set, with approximately 3/4 of the data used for model training, and a test set, consisting of about 1/4 of the data."
- , PDF page 5: "With approximately 25 structures in the training set, the RMSE on the prediction set falls down to 10 meV/atom, demonstrating a substantial improvement in predictive accuracy."
- , PDF page 4, Results and discussion: "These systems were randomly divided into a ML training set, with approximately 3/4 of the data used for model training, and a test set, consisting of about 1/4 of the data."
- , PDF page 2: "A simple linear correction, based on known enthalpy differences between DFT-calculated and experimentally measured values, provides a visible yet limited improvement. By applying machine learning techniques, specifically neural networks with supervised training, the predictive accuracy is significantly enhanced, enabling a more reliable determination of phase stability."
- , PDF page 6: "While the linear model offers some level of correction, its predictive power is ultimately constrained by its functional form. Even with interaction terms such as xAxB and xAxBxC, it cannot fully account for the intricate relationships governing enthalpy corrections. The neural network, in contrast, demonstrates a much greater ability to capture these relationships, leading to a substantial improvement in predictive accuracy."

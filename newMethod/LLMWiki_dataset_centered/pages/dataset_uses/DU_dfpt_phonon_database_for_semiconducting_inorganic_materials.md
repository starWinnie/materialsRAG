# Dataset Use: DFPT phonon database for semiconducting inorganic materials

- DatasetUse ID: `DU_dfpt_phonon_database_for_semiconducting_inorganic_materials`
- Dataset: DFPT phonon database for semiconducting inorganic materials (`D_dfpt_phonon_database_for_semiconducting_inorganic_materials`)
- Papers: P027
- Usage records: 4

## Usage roles

- source
- training
- test

## Purposes

- Source of high-quality ab initio phonon dispersion data for training and validation
- Training set for VGNN models (VVN, MVN, k-MVN) / Test set for VGNN models (VVN, MVN, k-MVN)
- Training data for optimizing neural network parameters via MSE loss minimization
- Test set for evaluating prediction accuracy via loss distribution and correlation plots

## Used fields

- phonon dispersion along highly symmetric paths
- material structures (primitive structure from Materials Project)
- Γ-phonon spectra
- phonon dispersion at high-symmetry points

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 1521

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P027_01_dfpt_phonon_database_for_semiconducting_inorganic_materials

- Paper: `P027` — Virtual Node Graph Neural Network for Full Phonon Prediction
- Task: phonon spectra and bandstructure prediction (`T_P027_01`)
- Stage: acquisition of ab initio phonon data (`data_acquisition`, `S_P027_01`)
- Usage role: source
- Purpose: Source of high-quality ab initio phonon dispersion data for training and validation
- Used fields: phonon dispersion along highly symmetric paths, material structures (primitive structure from Materials Project)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 1521
- Confidence: 1.0

Evidence:
- P027, PDF page 9, Methods: "The data set contains material structures (the same as the primitive structure obtained from the Material Project12), second-order derivatives of energies with respect to atomic perturbations for regular points inside the irreducible zone, and phonon dispersion along highly symmetric paths of 1,521 crystalline inorganic materials."

### UR_P027_02_dfpt_phonon_database_for_semiconducting_inorganic_materials

- Paper: `P027` — Virtual Node Graph Neural Network for Full Phonon Prediction
- Task: phonon spectra and bandstructure prediction (`T_P027_01`)
- Stage: phonon data preparation and splitting (`data_preparation`, `S_P027_02`)
- Usage role: training
- Purpose: Training set for VGNN models (VVN, MVN, k-MVN) / Test set for VGNN models (VVN, MVN, k-MVN)
- Used fields: phonon dispersion along highly symmetric paths, Γ-phonon spectra
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P027, PDF page 9, Methods: "All models randomly split the data into 90% training (1,365 materials), and 10% testing (156 materials) sets."
- P027, PDF page 9, Methods: "All models randomly split the data into 90% training (1,365 materials), and 10% testing (156 materials) sets."

### UR_P027_03_dfpt_phonon_database_for_semiconducting_inorganic_materials

- Paper: `P027` — Virtual Node Graph Neural Network for Full Phonon Prediction
- Task: phonon spectra and bandstructure prediction (`T_P027_01`)
- Stage: training of VGNN models (VVN, MVN, k-MVN) (`model_training`, `S_P027_03`)
- Usage role: training
- Purpose: Training data for optimizing neural network parameters via MSE loss minimization
- Used fields: Γ-phonon spectra, phonon dispersion at high-symmetry points
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P027, PDF page 10, unknown: "The model is optimized by minimizing the mean squared error (MSE) loss function between the phonon of the training data set and the one predicted by the model after normalizing them by the maximum phonon frequency of each material."

### UR_P027_04_dfpt_phonon_database_for_semiconducting_inorganic_materials

- Paper: `P027` — Virtual Node Graph Neural Network for Full Phonon Prediction
- Task: phonon spectra and bandstructure prediction (`T_P027_01`)
- Stage: evaluation of phonon prediction accuracy (`model_evaluation`, `S_P027_04`)
- Usage role: test
- Purpose: Test set for evaluating prediction accuracy via loss distribution and correlation plots
- Used fields: Γ-phonon spectra, phonon dispersion at high-symmetry points
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P027, PDF page 4, unknown: "Evaluation of the test accuracy through the distribution of loss function and correlation plot between ground-truth and predicted average phonon frequencies, respectively."

## Aggregated evidence

- , PDF page 9, Methods: "The data set contains material structures (the same as the primitive structure obtained from the Material Project12), second-order derivatives of energies with respect to atomic perturbations for regular points inside the irreducible zone, and phonon dispersion along highly symmetric paths of 1,521 crystalline inorganic materials."
- , PDF page 9, Methods: "All models randomly split the data into 90% training (1,365 materials), and 10% testing (156 materials) sets."
- , PDF page 9, Methods: "All models randomly split the data into 90% training (1,365 materials), and 10% testing (156 materials) sets."
- , PDF page 10, unknown: "The model is optimized by minimizing the mean squared error (MSE) loss function between the phonon of the training data set and the one predicted by the model after normalizing them by the maximum phonon frequency of each material."
- , PDF page 4, unknown: "Evaluation of the test accuracy through the distribution of loss function and correlation plot between ground-truth and predicted average phonon frequencies, respectively."

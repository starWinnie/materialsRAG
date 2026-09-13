# Dataset: TSENN 1432-material dataset

- Dataset ID: `D_P003_tsenn_1432_material_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- TSENN 1432-material dataset
- dataset of 1432 materials
- 1432 frequency-dependent dielectric tensors
- aforementioned dataset
- 1432 bulk semiconductors

## Observed material scopes

- bulk semiconductors

## Observed research tasks

- prediction of tensorial spectra

## Observed research stages

- data_acquisition
- data_preparation
- model_training
- model_evaluation
- computational_validation

## Observed properties

- frequency-dependent dielectric tensor
- crystal structure
- bandgap
- energy-above-hull

## Observed fields

- dielectric_tensor
- crystal_structure
- bandgap
- energy_above_hull
- symmetry

## Usage evidence

- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): training in dataset selection and ab initio calculation — training data for TSENN model consisting of frequency-dependent dielectric tensors computed via first-principles methods
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): label_source in spherical-harmonics decomposition and basis transformation — source of ground-truth Cartesian dielectric tensors for spherical-harmonics decomposition
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): training in training TSENN with composite loss function — training input for TSENN model after spherical-harmonics decomposition
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): validation in evaluation using MAE and symmetry-preserving metrics — validation set for model evaluation using MAE and symmetry-preserving metrics / test set for final model evaluation and error metric reporting
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): computational_validation in Kramers–Kronig reconstruction and strain-based symmetry breaking tests — computational validation via Kramers–Kronig reconstruction and strain-based symmetry breaking tests

## Dataset evidence

- P003, PDF page 2, Results: "These constraints yielded a dataset of 1432 materials, whose composition is summarized in Fig. 1."
- P003, PDF page 2, Results: "We demonstrate the capabilities of TSENN by considering the frequency-dependent dielectric tensors of a dataset of 1432 nonmagnetic semiconductors calculated via first-principles methods using OpenMX37–40."
- P003, PDF page 2, Results: "By training TSENN on the aforementioned dataset, we achieve a mean absolute error (MAE) of 0.127 in the predicted imaginary part of the dielectric tensor."

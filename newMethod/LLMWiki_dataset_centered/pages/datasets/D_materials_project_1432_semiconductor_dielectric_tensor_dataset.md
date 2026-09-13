# Dataset: Materials Project 1432-semiconductor dielectric tensor dataset

- Dataset ID: `D_materials_project_1432_semiconductor_dielectric_tensor_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- Materials Project 1432-semiconductor dielectric tensor dataset
- dataset of 1432 nonmagnetic semiconductors
- dataset of 1432 materials
- 1432 frequency-dependent dielectric tensors

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

## Observed fields

- crystal structure
- atomic species
- relative atomic positions
- dielectric tensor (real and imaginary parts)
- bandgap
- space group
- energy above hull

## Usage evidence

- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): source in ab initio calculations of dielectric tensors — ab initio calculation of frequency-dependent dielectric tensors via OpenMX and Kubo formula
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): source in spherical-harmonics decomposition of dielectric tensors — spherical-harmonics decomposition of Cartesian dielectric tensors into ℓ=0 and ℓ=2 channels
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): training in training TSENN on spherical-harmonics coefficients — training TSENN to predict ℓ=0 and ℓ=2 spherical-harmonics coefficients from crystal graphs
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): validation in evaluation of dielectric tensor prediction accuracy — evaluation of dielectric tensor prediction accuracy using MAE and other metrics on full-tensor and per-component levels
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): computational_validation in Kramers–Kronig reconstruction and symmetry validation — Kramers–Kronig reconstruction of real parts from predicted imaginary parts and symmetry validation via masking

## Dataset evidence

- P003, PDF page 2, Results: "We demonstrate the capabilities of TSENN by considering the frequency-dependent dielectric tensors of a dataset of 1432 nonmagnetic semiconductors calculated via first-principles methods using OpenMX."
- P003, PDF page 2, Results: "With our focus on small bandgap semiconductors in mind, we selected materials from the Materials Project41 with bandgaps ranging from 0.3 to 3 eV... To maintain structural stability, we imposed an energy-above-hull threshold of 0.02 eV/atom. For computational efficiency, we limited our selection to materials with fewer than three elements and fewer than ten atoms per unit cell. Additionally, we excluded magnetic materials as well as materials containing elements with f electrons..."
- P003, PDF page 2, Results: "The dielectric tensors were computed using the Kubo formula for photon energies ranging from 0 to 30 eV, with an increment of 0.01 eV, resulting in 1432 frequency-dependent dielectric tensors satisfying the symmetry constraints of the crystal systems considered."

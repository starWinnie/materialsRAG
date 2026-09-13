# Dataset: Materials Project 1432-semiconductor dataset

- Dataset ID: `D_P003_materials_project_1432_semiconductor_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- Materials Project 1432-semiconductor dataset
- dataset of 1432 nonmagnetic semiconductors
- 1432 frequency-dependent dielectric tensors
- 1,432 bulk semiconductors

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
- candidate_screening

## Observed properties

- frequency-dependent dielectric tensor
- complex dielectric tensor εαβ(ω) = εαβ₁(ω) + iεαβ₂(ω)

## Observed fields

- Cartesian dielectric tensor components (εxx, εyy, εzz, εxy, εxz, εyz)
- spherical-harmonic coefficients (ℓ=0, ℓ=2)
- photon energy grid (0–30 eV, 0.01 eV increment)

## Usage evidence

- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): source in ab initio calculation of dielectric tensors — Ab initio calculation of frequency-dependent dielectric tensors via OpenMX and Kubo formula
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): label_source in spherical-harmonics decomposition of dielectric tensors — Spherical-harmonics decomposition of Cartesian dielectric tensors to obtain frequency-dependent spherical-harmonic coefficients for training targets
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): training in training TSENN on spherical-harmonic coefficients — Training TSENN to predict spherical-harmonic coefficients (ℓ=0 and ℓ=2) from crystal graphs
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): test in evaluation of dielectric tensor prediction accuracy — Evaluation of dielectric tensor prediction accuracy using MAE and component-wise metrics
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): computational_validation in reconstruction of real dielectric part via Kramers–Kronig relations — Reconstructing real part of dielectric tensor from predicted imaginary part using Kramers–Kronig relations
- P003 (Accurate prediction of tensorial spectra using equivariant graph neural network): screening in symmetry-preserving validation across crystal systems — Symmetry-preserving validation across crystal systems using symmetry-based masking procedure

## Dataset evidence

- P003, PDF page 2, Results: "We demonstrate the capabilities of TSENN by considering the frequency-dependent dielectric tensors of a dataset of 1432 nonmagnetic semiconductors calculated via ﬁrst-principles methods using OpenMX37–40."
- P003, PDF page 1: "Trained on frequency-dependent dielectric tensors of 1,432 bulk semiconductors, the model achieves a mean absolute error of 0.127, demonstrating its potential for efﬁcient and general modeling of optical properties."
- P003, PDF page 2, Results: "With our focus on small bandgap semiconductors in mind, we selected materials from the Materials Project41 with bandgaps ranging from 0.3 to 3 eV (photon wavelengths of 4100 nm (infrared) to 413 nm (violet)) that are appropriate for optoelectronic applications42,43. To maintain structural stability, we imposed an energy-above-hull threshold of 0.02 eV/atom. For computational efﬁciency, we limited our selection to materials with fewer than three elements and fewer than ten atoms per unit cell. Additionally, we excluded magnetic materials as well as materials containing elements with f electrons due to the lack of availability of accurate, predeﬁned pseudo-potential sets. These constraints yielded a dataset of 1432 materials, whose composition is summarized in Fig. 1."

# Dataset Use: MPF.2021.2.8 dataset

- DatasetUse ID: `DU_mpf_2021_2_8_dataset`
- Dataset: MPF.2021.2.8 dataset (`D_mpf_2021_2_8_dataset`)
- Papers: P004
- Usage records: 1

## Usage roles

- training

## Purposes

- Training M3GNet model on energies, forces, and stresses.

## Used fields

- energies
- forces
- stresses

## Construction methods

- down-sampled subset selecting only initial, final and one intermediate structure per material from v.2021.02.08 MP release

## Filter conditions

- None stated

## Sample counts

- 188349

## Availability

- Dataset: public
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P004_03_mpf_2021_2_8_dataset

- Paper: `P004` — A framework to evaluate machine learning crystal stability predictions
- Task: ML-guided materials discovery (`T_P004_01`)
- Stage: Training of ML models on MP data (`model_training`, `S_P004_03`)
- Usage role: training
- Purpose: Training M3GNet model on energies, forces, and stresses.
- Used fields: energies, forces, stresses
- Filter conditions: Not stated
- Construction method: down-sampled subset selecting only initial, final and one intermediate structure per material from v.2021.02.08 MP release
- Sample count: 188349
- Confidence: 1.0

Evidence:
- P004, PDF page 8, Article: "The next is the MPF.2021.2.8 dataset22 curated to train the M3GNet model, which takes a subset of 62,783 materials from the v.2021.02.08 MP release. The curators of the MPF.2021.2.8 dataset down-sampled the v.2021.02.08 release notably to select a subset of calculations that they believed to be most self-consistent. Rather than taking every ionic step from the relaxation trajectory, this dataset opts to select only the initial, final and one intermediate structure for each material to avoid biasing the dataset towards examples where more ionic steps were needed to relax the structure. Consequently the dataset consists of 188,349 structures."

## Aggregated evidence

- , PDF page 8, Article: "The next is the MPF.2021.2.8 dataset22 curated to train the M3GNet model, which takes a subset of 62,783 materials from the v.2021.02.08 MP release. The curators of the MPF.2021.2.8 dataset down-sampled the v.2021.02.08 release notably to select a subset of calculations that they believed to be most self-consistent. Rather than taking every ionic step from the relaxation trajectory, this dataset opts to select only the initial, final and one intermediate structure for each material to avoid biasing the dataset towards examples where more ionic steps were needed to relax the structure. Consequently the dataset consists of 188,349 structures."

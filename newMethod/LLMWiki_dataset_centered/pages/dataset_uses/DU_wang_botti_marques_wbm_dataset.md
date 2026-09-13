# Dataset Use: Wang-Botti-Marques (WBM) dataset

- DatasetUse ID: `DU_wang_botti_marques_wbm_dataset`
- Dataset: Wang-Botti-Marques (WBM) dataset (`D_wang_botti_marques_wbm_dataset`)
- Papers: P004
- Usage records: 1

## Usage roles

- source

## Purposes

- Cleaning and protostructure-based filtering to construct prospective test set without contamination from training set.

## Used fields

- unrelaxed structures
- formation energies

## Construction methods

- protostructure matching and duplication removal

## Filter conditions

- formation energies > 5 eV per atom or < -5 eV per atom
- final protostructure matches MP material's final protostructure
- duplicated protostructures within WBM

## Sample counts

- 215488

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P004_02_wang_botti_marques_wbm_dataset

- Paper: `P004` — A framework to evaluate machine learning crystal stability predictions
- Task: ML-guided materials discovery (`T_P004_01`)
- Stage: Cleaning and protostructure-based filtering of WBM test set (`data_preparation`, `S_P004_02`)
- Usage role: source
- Purpose: Cleaning and protostructure-based filtering to construct prospective test set without contamination from training set.
- Used fields: unrelaxed structures, formation energies
- Filter conditions: formation energies > 5 eV per atom or < -5 eV per atom, final protostructure matches MP material's final protostructure, duplicated protostructures within WBM
- Construction method: protostructure matching and duplication removal
- Sample count: 215488
- Confidence: 1.0

Evidence:
- P004, PDF page 8, Article: "First we removed 524 pathological structures in WBM based on formation energies being larger than 5 eV per atom or smaller than −5 eV per atom. We then removed from the WBM test set all examples where the final protostructure of a WBM material matched the final protostructure of an MP material. In total, 11,175 materials were cleaned using this filter. We further removed all duplicated protostructures within WBM, keeping the lowest energy structure in each instance, leaving 215,488 structures in the unique prototype test set."

## Aggregated evidence

- , PDF page 8, Article: "First we removed 524 pathological structures in WBM based on formation energies being larger than 5 eV per atom or smaller than −5 eV per atom. We then removed from the WBM test set all examples where the final protostructure of a WBM material matched the final protostructure of an MP material. In total, 11,175 materials were cleaned using this filter. We further removed all duplicated protostructures within WBM, keeping the lowest energy structure in each instance, leaving 215,488 structures in the unique prototype test set."

# Dataset Use: DPF Unlabeled Crystal Structures

- DatasetUse ID: `DU_dpf_unlabeled_crystal_structures`
- Dataset: DPF Unlabeled Crystal Structures (`D_dpf_unlabeled_crystal_structures`)
- Papers: P011
- Usage records: 1

## Usage roles

- pretraining

## Purposes

- Pre-training the denoising model on unlabeled crystal structures.

## Used fields

- atom types
- atom positions
- lattice constants

## Construction methods

- Filtered from Merchant et al. (2023) crystal discovery output, excluding duplicates of downstream datasets and physically or chemically irrational structures.

## Filter conditions

- exclusion of repetitive structures
- exclusion of physically or chemically irrational structures
- exclusion of duplicates of downstream datasets

## Sample counts

- 380743

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P011_01_dpf_unlabeled_crystal_structures

- Paper: `P011` — A Denoising Pre-training Framework for Accelerating Novel Material Discovery
- Task: crystal property prediction (`T_P011_01`)
- Stage: acquiring unlabeled crystal structures (`data_acquisition`, `S_P011_01`)
- Usage role: pretraining
- Purpose: Pre-training the denoising model on unlabeled crystal structures.
- Used fields: atom types, atom positions, lattice constants
- Filter conditions: exclusion of repetitive structures, exclusion of physically or chemically irrational structures, exclusion of duplicates of downstream datasets
- Construction method: Filtered from Merchant et al. (2023) crystal discovery output, excluding duplicates of downstream datasets and physically or chemically irrational structures.
- Sample count: 380743
- Confidence: 1.0

Evidence:
- P011, PDF page 3, Crystal Datasets: "After filtering the repetitive and physically or chemically irrational structures, we utilize 380,743 structures to pre-train our model."

## Aggregated evidence

- , PDF page 3, Crystal Datasets: "After filtering the repetitive and physically or chemically irrational structures, we utilize 380,743 structures to pre-train our model."

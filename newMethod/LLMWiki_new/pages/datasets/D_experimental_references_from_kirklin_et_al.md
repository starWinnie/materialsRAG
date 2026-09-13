# Dataset: experimental references from Kirklin et al.

- Dataset ID: `D_experimental_references_from_kirklin_et_al`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- experimental references from Kirklin et al.
- experimental references used by Kirklin et al. [10]

## Observed material scopes

- experimentally known compounds

## Observed research tasks

- Correcting DFT formation energies towards experimental accuracy

## Observed research stages

- model_evaluation
- model_training

## Observed properties

- experimental formation enthalpy

## Observed fields

- None stated

## Usage evidence

- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): label_source in Compare DFT formation energies against experimental formation enthalpies — Provide additional experimental formation enthalpy references to increase dataset size and diversity
- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): label_source in Train classical ML models in delta-learning framework using fMLIP latent features — Provide additional experimental formation enthalpy references to compute delta target (δ∆HMLIP_f = PET-OMATPES r2SCAN formation energy − experimental formation enthalpy)
- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): label_source in Evaluate ML-corrected formation energies against experiment — Provide additional experimental formation enthalpy references for final accuracy quantification (MAE < 50 meV/atom)

## Dataset evidence

- P035, PDF page 9, METHODS: "To increase the amount and diversity of experimental reference data, which is typically the limiting factor in data-driven studies, we combine this with the experimental references used by Kirklin et al. [10], yielding 2726 unique compounds in total."

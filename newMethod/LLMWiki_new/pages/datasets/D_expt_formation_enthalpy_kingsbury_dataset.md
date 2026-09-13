# Dataset: expt formation enthalpy kingsbury dataset

- Dataset ID: `D_expt_formation_enthalpy_kingsbury_dataset`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- expt formation enthalpy kingsbury dataset

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

- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): label_source in Compare DFT formation energies against experimental formation enthalpies — Provide experimental formation enthalpy references for baseline error metrics
- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): label_source in Train classical ML models in delta-learning framework using fMLIP latent features — Provide experimental formation enthalpy references to compute delta target (δ∆HMLIP_f = PET-OMATPES r2SCAN formation energy − experimental formation enthalpy)
- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): label_source in Evaluate ML-corrected formation energies against experiment — Provide experimental formation enthalpy references for final accuracy quantification (MAE < 50 meV/atom)

## Dataset evidence

- P035, PDF page 9, METHODS: "To assess the performance of the DFT calculated formation energies, we use the experimental references collected by Wang et al. [43] and published in the matminer package [73] as the expt formation enthalpy kingsbury dataset [43, 81–87]."

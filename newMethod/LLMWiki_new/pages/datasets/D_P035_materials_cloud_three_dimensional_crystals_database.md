# Dataset: Materials Cloud three-dimensional crystals database

- Dataset ID: `D_P035_materials_cloud_three_dimensional_crystals_database`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- Materials Cloud three-dimensional crystals database
- MC3D

## Observed material scopes

- three-dimensional inorganic crystal structures
- experimentally known compounds

## Observed research tasks

- Correcting DFT formation energies towards experimental accuracy

## Observed research stages

- model_evaluation
- model_training
- candidate_screening

## Observed properties

- formation energy
- energy above the convex hull

## Observed fields

- DFT formation energies (PBE, PBEsol)
- PBE-v1
- PBEsol-v1

## Usage evidence

- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): source in Compare DFT formation energies against experimental formation enthalpies — Provide DFT formation energies (PBE, PBEsol) for comparison against experimental formation enthalpies
- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): source in Evaluate zero-shot fMLIP formation energies on DFT geometries — Provide DFT-relaxed geometries (PBEsol) for zero-shot evaluation of PET-OMATPES r2SCAN MLIP
- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): source in Train classical ML models in delta-learning framework using fMLIP latent features — Provide PET-OMATPES latent features extracted from PBEsol-relaxed geometries as input for delta-learning models
- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): source in Evaluate ML-corrected formation energies against experiment — Provide zero-shot PET-OMATPES r2SCAN formation energies for final evaluation against experiment
- P035 (Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning): candidate_pool in Select optimal model via regularization tuning — Provide candidate structures for stability classification flip analysis during regularization tuning

## Dataset evidence

- P035, PDF page 1, ABSTRACT: "Here, we present the thermodynamic stability of the fully open-source, reproducible, and experimentally focused Materials Cloud three-dimensional crystals database (MC3D)."
- P035, PDF page 9, METHODS: "In this work, we introduce formation energies to the Materials Cloud three-dimensional crystals database [17], a fully reproducible and open-source DFT curated database of three-dimensional inorganic crystal structures with a particular focus on experimentally known compounds."

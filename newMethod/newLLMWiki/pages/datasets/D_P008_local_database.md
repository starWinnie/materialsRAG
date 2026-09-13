# Dataset: local database

- Dataset ID: `D_P008_local_database`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- local database
- 661 materials with κPET values at 300 K
- labeled local database

## Observed material scopes

- semiconductors

## Observed research tasks

- identifying semiconductors with ultralow lattice thermal conductivity

## Observed research stages

- candidate_screening
- computational_validation
- model_training
- model_evaluation

## Observed properties

- κPET
- crystal structure
- chemical composition
- shear modulus
- bulk modulus
- formula type
- crystal system

## Observed fields

- κPET
- structure
- composition
- shear_modulus
- bulk_modulus
- formula_type
- crystal_system

## Usage evidence

- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): screening in statistical analysis and candidate screening from local database — Statistical analysis and candidate screening to identify materials with κPET ≤ 2 W/mK.
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): computational_validation in first-principles validation of κL for selected candidates — Select specific candidates (Cs2SnSe3 and Cs2GeSe3) for first-principles validation.
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): training in training CatBoost classifier for ultralow κL prediction — Train CatBoost classifier for ultralow κL prediction.
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): validation in evaluating CatBoost classifier performance — Evaluate CatBoost classifier performance using stratified tenfold cross-validation.

## Dataset evidence

- P008, PDF page 3: "We use the phonon-elasticity-thermal (PET) model44 to perform low-cost HTC on the materials in the second-level dataset, establishing a local database based on the HTC results."

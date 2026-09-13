# Dataset: MoleculeNet

- Dataset ID: `D_moleculenet`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- MoleculeNet

## Observed material scopes

- molecules

## Observed research tasks

- Out-of-Distribution Property Prediction

## Observed research stages

- data_acquisition
- data_preparation
- candidate_screening
- model_evaluation

## Observed properties

- aqueous solubility
- hydration free energy
- lipophilicity
- binding affinity

## Observed fields

- SMILES representations
- property values

## Usage evidence

- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): benchmark in Curating benchmark datasets for solids and molecules — Evaluate extrapolation capability on molecular graph-to-property prediction tasks
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): training in Preprocessing representations and splitting datasets into ID/OOD sets — Train predictor models using RDKit descriptors for molecules
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): screening in Selecting high-performing OOD candidates via top-k prediction — Identify top-performing OOD candidates by selecting the top 30% of test samples with highest predicted property values
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): test in Evaluating OOD prediction accuracy and distributional alignment — Evaluate OOD prediction accuracy and distributional alignment

## Dataset evidence

- P017, PDF page 3, Molecules: "For molecular systems, we used datasets from MoleculeNet, covering four graph-to-property prediction tasks with dataset sizes ranging from 600 to 4200 samples, and benchmarked our approach against three baseline methods."
- P017, PDF page 3, Molecules: "MoleculeNet includes molecular graphs encoded as SMILES representations35 and their property values derived from high-throughput calculations and experimental trials36."

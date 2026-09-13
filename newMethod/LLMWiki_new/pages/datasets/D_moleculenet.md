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
- label_generation
- candidate_screening
- model_evaluation

## Observed properties

- aqueous solubility
- hydration free energy
- lipophilicity
- binding affinity

## Observed fields

- molecular graphs (SMILES)
- property values

## Usage evidence

- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): source in Curating benchmark datasets for solids and molecules — Benchmark for molecular graph-to-property prediction tasks
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): candidate_pool in Defining OOD labels via top/bottom percentile thresholds — Defining OOD labels via top 5% highest property values
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): screening in Screening for top OOD candidates using extrapolative precision — Screening for top OOD candidates by identifying 30% of test samples with highest property values
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): benchmark in Evaluating OOD prediction accuracy and distributional alignment — Evaluating OOD prediction accuracy using mean absolute error (MAE), recall, and kernel density estimation (KDE) overlap

## Dataset evidence

- P017, PDF page 3, Dataset: "For molecular systems, we used datasets from MoleculeNet, covering four graph-to-property prediction tasks with dataset sizes ranging from 600 to 4200 samples, and benchmarked our approach against three baseline methods."
- P017, PDF page 3, Dataset: "MoleculeNet includes molecular graphs encoded as SMILES representations35 and their property values derived from high-throughput calculations and experimental trials36."

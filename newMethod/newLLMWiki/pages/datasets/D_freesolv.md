# Dataset: FreeSolv

- Dataset ID: `D_freesolv`
- Dataset type: `public_subset`
- Source dataset: `D_moleculenet`
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- FreeSolv

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

- hydration free energy

## Observed fields

- SMILES representations
- property values

## Usage evidence

- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): benchmark in Curating benchmark datasets for solids and molecules — Evaluate extrapolation capability on hydration free energy prediction task
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): training in Preprocessing representations and splitting datasets into ID/OOD sets — Train predictor models using RDKit descriptors for molecules
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): screening in Selecting high-performing OOD candidates via top-k prediction — Identify top-performing OOD candidates by selecting the top 30% of test samples with highest predicted property values
- P017 (Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules): test in Evaluating OOD prediction accuracy and distributional alignment — Evaluate OOD prediction accuracy and distributional alignment

## Dataset evidence

- P017, PDF page 3, Molecules: "The ESOL dataset provides measurements of aqueous solubility for small molecules, FreeSolv contains experimental and calculated hydration free energies for small neutral molecules in water, Lipophilicity reports octanol/water distribution coefﬁcients, and BACE includes binding afﬁnities of small molecules to human β-secretase 1 (BACE-1)."

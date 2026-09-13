# MoleculeNet

## Ontology Type
DatasetUse

## Usage Description
MoleculeNet is a collection of molecular datasets for machine learning, used here for four graph-to-property regression tasks: ESOL (1,128 small molecules with aqueous solubility), FreeSolv (643 molecules with experimental and calculated hydration free energies), Lipophilicity (4,200 molecules with octanol/water distribution coefficients), and BACE (1,513 molecules with binding affinities to human β-secretase 1). These datasets provide SMILES strings and experimentally or computationally derived property values, and are used to train and evaluate the transductive OOD predictor for molecular property extrapolation — specifically to screen for molecules with extreme (top 30%) property values beyond the training support.

## Dataset
- [MoleculeNet](../datasets/moleculenet.md)

## Task
- [17_Known_Unknowns_OOD.pdf](../tasks/17_known_unknowns_ood_pdf.md)

## Paper
- [17 Known Unknowns OOD](../papers/17_known_unknowns_ood.md)

## Provided Representations
- [composition](../representations/composition.md)
- [crystal graph](../representations/crystal_graph.md)
- [SMILES](../representations/smiles.md)
- [descriptor](../representations/descriptor.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Validation](../stages/validation.md)

## Evidence
- MoleculeNet is a collection of molecular datasets for machine learning, used here for four graph-to-property regression tasks: ESOL (1,128 small molecules with aqueous solubility), FreeSolv (643 molecules with experimental and calculated hydration free energies), Lipophilicity (4,200 molecules with octanol/water distribution coefficients), and BACE (1,513 molecules with binding affinities to human β-secretase 1). These datasets provide SMILES strings and experimentally or computationally derived property values, and are used to train and evaluate the transductive OOD predictor for molecular property extrapolation — specifically to screen for molecules with extreme (top 30%) property values beyond the training support.

## Metadata
dataset_use_id: `dataset_use_648bb8665f99`
link: https://moleculenet.org

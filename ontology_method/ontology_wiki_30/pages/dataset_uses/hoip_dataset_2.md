# HOIP Dataset

## Ontology Type
DatasetUse

## Usage Description
A density functional theory (DFT)-calculated dataset containing 1345 perovskite compounds, each composed of organic/inorganic cations (Ge, Sn, Pb) and anions (F, Cl, Br, I), along with computed bandgaps and other properties. It is partitioned into 12 domains based on cation–anion combinations; two extrapolative tasks—HOIP-GeF (excluding Ge+F compounds) and HOIP-PbI (excluding Pb+I compounds)—are defined by withholding entire chemical combinations from training. The dataset supports evaluating extrapolative bandgap prediction when the model must generalize to unseen elemental pairings not present in the support set.

## Dataset
- [HOIP Dataset](../datasets/hoip_dataset.md)

## Task
- [15_Extrapolative_Episodic_Training.pdf](../tasks/15_extrapolative_episodic_training_pdf.md)

## Paper
- [15 Extrapolative Episodic Training](../papers/15_extrapolative_episodic_training.md)

## Provided Representations
- [composition](../representations/composition.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)

## Evidence
- A density functional theory (DFT)-calculated dataset containing 1345 perovskite compounds, each composed of organic/inorganic cations (Ge, Sn, Pb) and anions (F, Cl, Br, I), along with computed bandgaps and other properties. It is partitioned into 12 domains based on cation–anion combinations; two extrapolative tasks—HOIP-GeF (excluding Ge+F compounds) and HOIP-PbI (excluding Pb+I compounds)—are defined by withholding entire chemical combinations from training. The dataset supports evaluating extrapolative bandgap prediction when the model must generalize to unseen elemental pairings not present in the support set.

## Metadata
dataset_use_id: `dataset_use_ed93b5e1b852`
link: https://doi.org/10.5061/dryad.gq3rg

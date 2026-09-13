# GNoME materials dataset (subset)

## Ontology Type
DatasetUse

## Usage Description
A curated subset of 1,924 novel inorganic materials published by Google’s GNoME project, selected to include structures with ≥5 unique elemental species — intentionally out-of-distribution relative to the Materials Project training set. It contains DFT-computed charge densities generated using consistent VASP settings (k-point density, energy cutoff, PAW potentials). This dataset was used to test ChargE3Net’s generalization capability for charge density prediction on previously unseen chemical spaces — directly supporting the task of robust cross-dataset transfer for DFT acceleration beyond the training domain.

## Dataset
- [GNoME materials dataset (subset)](../datasets/gnome_materials_dataset_subset.md)

## Task
- [25_ChargE3Net.pdf](../tasks/25_charge3net_pdf.md)

## Paper
- [25 ChargE3Net](../papers/25_charge3net.md)

## Provided Representations
- [crystal structure](../representations/crystal_structure.md)
- [atomic coordinates](../representations/atomic_coordinates.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)

## Evidence
- A curated subset of 1,924 novel inorganic materials published by Google’s GNoME project, selected to include structures with ≥5 unique elemental species — intentionally out-of-distribution relative to the Materials Project training set. It contains DFT-computed charge densities generated using consistent VASP settings (k-point density, energy cutoff, PAW potentials). This dataset was used to test ChargE3Net’s generalization capability for charge density prediction on previously unseen chemical spaces — directly supporting the task of robust cross-dataset transfer for DFT acceleration beyond the training domain.

## Metadata
dataset_use_id: `dataset_use_eb7d715612ea`
link: https://doi.org/10.1038/s41586-023-06735-9

# SuperCon3D

## Ontology Type
DatasetUse

## Usage Description
SuperCon3D is a newly constructed dataset containing 1,578 experimentally verified superconductors, each with both a 3D crystal structure (ordered or disordered, including substitutional, positional, and combined disorder types) and its experimentally measured superconducting transition temperature (Tc). It was built by matching 11,949 superconductors from the SuperCon database (with chemical formulas and Tc) against 208,425 entries from the ICSD database using chemical composition, space group, and lattice parameters; hydrogen-enriched superconductors were supplemented from literature. This dataset directly supports the Tc prediction task for training and evaluating SODNet and benchmarking other property predictors.

## Dataset
- [SuperCon3D](../datasets/supercon3d.md)

## Task
- [31_Superconductivity_Ordered_Disordered.pdf](../tasks/31_superconductivity_ordered_disordered_pdf.md)

## Paper
- [31 Superconductivity Ordered Disordered](../papers/31_superconductivity_ordered_disordered.md)

## Provided Representations
- [composition](../representations/composition.md)
- [crystal structure](../representations/crystal_structure.md)
- [lattice vectors](../representations/lattice_vectors.md)
- [space group](../representations/space_group.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Validation](../stages/validation.md)
- [Benchmarking / Evaluation](../stages/benchmarking_evaluation.md)

## Evidence
- SuperCon3D is a newly constructed dataset containing 1,578 experimentally verified superconductors, each with both a 3D crystal structure (ordered or disordered, including substitutional, positional, and combined disorder types) and its experimentally measured superconducting transition temperature (Tc). It was built by matching 11,949 superconductors from the SuperCon database (with chemical formulas and Tc) against 208,425 entries from the ICSD database using chemical composition, space group, and lattice parameters; hydrogen-enriched superconductors were supplemented from literature. This dataset directly supports the Tc prediction task for training and evaluating SODNet and benchmarking other property predictors.

## Metadata
dataset_use_id: `dataset_use_1ec550fb8fdf`
link: https://github.com/pincher-chen/SODNet

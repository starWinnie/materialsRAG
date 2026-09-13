# Materials Project

## Ontology Type
DatasetUse

## Usage Description
A publicly available DFT-computed database of inorganic materials containing 133,785 entries with crystal structures, compositions, and computed physical properties. It provides primary properties (e.g., formation energy per atom, band gap, energy above convex hull, Fermi energy) and secondary properties (e.g., bulk/shear moduli via Voigt-Reuss-Hill approximation, dielectric refractive index, phonon frequencies). In this paper, MP21 is used to train and benchmark the CrysCo model across eight regression tasks—serving as the source for both abundant primary-property data (e.g., ~126k formation energy samples) and scarce secondary-property data (e.g., only ~12k elasticity entries)—and enabling transfer learning from formation energy to mechanical properties.

## Dataset
- [Materials Project](../datasets/materials_project.md)

## Task
- [13_CrysCo.pdf](../tasks/13_crysco_pdf.md)

## Paper
- [13 CrysCo](../papers/13_crysco.md)

## Provided Representations
- [composition](../representations/composition.md)
- [crystal structure](../representations/crystal_structure.md)
- [crystal graph](../representations/crystal_graph.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Benchmarking / Evaluation](../stages/benchmarking_evaluation.md)

## Evidence
- A publicly available DFT-computed database of inorganic materials containing 133,785 entries with crystal structures, compositions, and computed physical properties. It provides primary properties (e.g., formation energy per atom, band gap, energy above convex hull, Fermi energy) and secondary properties (e.g., bulk/shear moduli via Voigt-Reuss-Hill approximation, dielectric refractive index, phonon frequencies). In this paper, MP21 is used to train and benchmark the CrysCo model across eight regression tasks—serving as the source for both abundant primary-property data (e.g., ~126k formation energy samples) and scarce secondary-property data (e.g., only ~12k elasticity entries)—and enabling transfer learning from formation energy to mechanical properties.

## Metadata
dataset_use_id: `dataset_use_de1c07d75869`
link: https://materialsproject.org

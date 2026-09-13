# Materials Project

## Ontology Type
DatasetUse

## Usage Description
A publicly available DFT-based high-throughput computational materials database containing over 154,718 entries with thermodynamic, electronic, and structural properties (e.g., formation energy above hull, band gap, crystal structure, unit cell parameters). In this paper, it serves as the primary source for the initial material pool; the authors query it via API and apply thermodynamic stability (Ehull ≤ 0.05 eV/atom), semiconductor band gap (0.1–2 eV), unit cell size (Natoms < 20, Nelements < 4), and elemental constraints (excluding H, lanthanides, actinides) to construct the 2675-material first-level dataset used for unsupervised clustering and feature engineering.

## Dataset
- [Materials Project](../datasets/materials_project.md)

## Task
- [08_HiBoFL_Thermal_Conductivity.pdf](../tasks/08_hibofl_thermal_conductivity_pdf.md)

## Paper
- [08 HiBoFL Thermal Conductivity](../papers/08_hibofl_thermal_conductivity.md)

## Provided Representations
- [composition](../representations/composition.md)
- [crystal structure](../representations/crystal_structure.md)
- [descriptor](../representations/descriptor.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)

## Evidence
- A publicly available DFT-based high-throughput computational materials database containing over 154,718 entries with thermodynamic, electronic, and structural properties (e.g., formation energy above hull, band gap, crystal structure, unit cell parameters). In this paper, it serves as the primary source for the initial material pool; the authors query it via API and apply thermodynamic stability (Ehull ≤ 0.05 eV/atom), semiconductor band gap (0.1–2 eV), unit cell size (Natoms < 20, Nelements < 4), and elemental constraints (excluding H, lanthanides, actinides) to construct the 2675-material first-level dataset used for unsupervised clustering and feature engineering.

## Metadata
dataset_use_id: `dataset_use_d71c1217c4f4`
link: https://next-gen.materialsproject.org/

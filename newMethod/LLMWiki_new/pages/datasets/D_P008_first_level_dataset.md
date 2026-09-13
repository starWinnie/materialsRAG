# Dataset: first-level dataset

- Dataset ID: `D_P008_first_level_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- first-level dataset
- 2675 three-dimensional crystal structures

## Observed material scopes

- semiconductors

## Observed research tasks

- identifying semiconductors with ultralow lattice thermal conductivity

## Observed research stages

- data_preparation
- candidate_generation

## Observed properties

- thermodynamic stability (Ehull ≤ 0.05 eV/atom)
- band gap (0.1–2 eV)
- unit cell atoms < 20
- elements per compound < 4
- exclusion of H, lanthanides, actinides

## Observed fields

- Ehull
- Eg
- Natoms
- Nelements
- elements

## Usage evidence

- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): candidate_pool in preliminary high-throughput screening — Narrow down the material pool using thermodynamic, electronic, and computational constraints
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): source in unsupervised learning for clustering materials with similar κL — Unsupervised learning for clustering materials with similar κL

## Dataset evidence

- P008, PDF page 3: "Ultimately, through excluding the materials containing hydrogen, lanthanides, and actinides, and conducting structural analysis, we further obtain 2675 three-dimensional (3D) crystal structures without calculation errors. These materials constitute the first-level dataset for our in-depth investigations."

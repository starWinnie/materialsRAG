# Dataset: first-level dataset

- Dataset ID: `D_P008_first_level_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- first-level dataset
- 2675 three-dimensional (3D) crystal structures

## Observed material scopes

- semiconductors

## Observed research tasks

- identifying semiconductors with ultralow lattice thermal conductivity

## Observed research stages

- data_preparation
- candidate_generation

## Observed properties

- thermodynamic stability (Ehull ≤0.05 eV/atom)
- band gap (0.1–2 eV)
- Natoms < 20
- Nelements < 4
- no H, lanthanides, actinides

## Observed fields

- Ehull
- Eg
- Natoms
- Nelements
- structure
- composition

## Usage evidence

- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): candidate_pool in preliminary high-throughput screening and data cleaning — filter raw MP dataset to obtain stable, semiconducting, computationally tractable candidates
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): source in unsupervised learning to identify problem-specific clusters with similar κL — provide input for unsupervised learning to identify problem-specific clusters with similar κL

## Dataset evidence

- P008, PDF page 3, Preliminary high-throughput screening: "Ultimately, through excluding the materials containing hydrogen, lanthanides, and actinides, and conducting structural analysis, we further obtain 2675 three-dimensional (3D) crystal structures without calculation errors. These materials constitute the ﬁrst-level dataset for our in-depth investigations."

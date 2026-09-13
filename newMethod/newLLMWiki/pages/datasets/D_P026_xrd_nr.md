# Dataset: XRD-nr

- Dataset ID: `D_P026_xrd_nr`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- XRD-nr
- XRD non-redundant dataset

## Observed material scopes

- inorganic crystalline materials

## Observed research tasks

- dataset redundancy control for material property prediction

## Observed research stages

- data_preparation
- model_evaluation

## Observed properties

- formation energy
- band gap

## Observed fields

- cif files
- XRD features
- XRD distance

## Usage evidence

- P026 (MD-HIT: Machine learning for material property prediction with dataset redundancy control): training in redundancy reduction using MD-HIT-structure — Generate non-redundant structure dataset by iteratively selecting representative crystal structures based on structure distance metrics
- P026 (MD-HIT: Machine learning for material property prediction with dataset redundancy control): test in evaluate ML model performance on redundancy-controlled datasets — Evaluate ML model performance on redundancy-controlled datasets

## Dataset evidence

- P026, PDF page 4, Datasets generation: "We also applied the MD-HIT-structure algorithm to all 125,619 structures and used different thresholds to generate seven XRD non-redundant datasets and eight OFM non-redundant datasets."

# XRD features (from Pymatgen)

## Ontology Type
DatasetUse

## Usage Description
X-ray diffraction (XRD) patterns computed from crystal structures using Pymatgen’s XRDCalculator, smoothed with Gaussian kernel and sampled at 900 evenly spaced 2θ angles (0–90°), yielding fixed-length 900D feature vectors. These features are used in MD-HIT-structure to define structural similarity and generate seven XRD-based non-redundant structure datasets (XRD-nr) for evaluating ALIGNN and DeeperGATGNN on formation energy and band gap prediction under controlled structural redundancy.

## Dataset
- [XRD features (from Pymatgen)](../datasets/xrd_features_from_pymatgen.md)

## Task
- [26_MD_HIT.pdf](../tasks/26_md_hit_pdf.md)

## Paper
- [26 MD HIT](../papers/26_md_hit.md)

## Provided Representations
- [crystal structure](../representations/crystal_structure.md)
- [descriptor](../representations/descriptor.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Benchmarking / Evaluation](../stages/benchmarking_evaluation.md)

## Evidence
- X-ray diffraction (XRD) patterns computed from crystal structures using Pymatgen’s XRDCalculator, smoothed with Gaussian kernel and sampled at 900 evenly spaced 2θ angles (0–90°), yielding fixed-length 900D feature vectors. These features are used in MD-HIT-structure to define structural similarity and generate seven XRD-based non-redundant structure datasets (XRD-nr) for evaluating ALIGNN and DeeperGATGNN on formation energy and band gap prediction under controlled structural redundancy.

## Metadata
dataset_use_id: `dataset_use_e39f8b7257a8`
link: https://pymatgen.org

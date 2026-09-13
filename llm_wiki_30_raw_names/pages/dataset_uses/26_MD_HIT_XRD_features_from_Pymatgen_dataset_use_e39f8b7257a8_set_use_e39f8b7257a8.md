# 26_MD_HIT - XRD features (from Pymatgen)

## Dataset Use

X-ray diffraction (XRD) patterns computed from crystal structures using Pymatgen’s XRDCalculator, smoothed with Gaussian kernel and sampled at 900 evenly spaced 2θ angles (0–90°), yielding fixed-length 900D feature vectors. These features are used in MD-HIT-structure to define structural similarity and generate seven XRD-based non-redundant structure datasets (XRD-nr) for evaluating ALIGNN and DeeperGATGNN on formation energy and band gap prediction under controlled structural redundancy.

## Links

- Paper: [26 MD HIT](../papers/26_MD_HIT_paper_364d763e5978.md)
- Task: [task page](../tasks/26_MD_HIT_task_1_task_e55c8a4f2b28.md)
- Dataset: [XRD features (from Pymatgen)](../datasets/XRD_features_from_Pymatgen_dataset_03047ecfd3fa.md)
- Dataset URL: https://pymatgen.org

## Task Context

Designing and applying a dataset redundancy control method to enable objective, realistic evaluation of machine learning models for material property prediction—specifically by preventing overestimated interpolation performance and improving out-of-distribution (OOD) generalization capability on formation energy and band gap prediction tasks.

## Metadata

- Dataset use ID: `dataset_use_e39f8b7257a8`
- Original dataset title: XRD features (from Pymatgen)
- Tags: redundancy reduction, model evaluation, OOD generalization, material property prediction

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

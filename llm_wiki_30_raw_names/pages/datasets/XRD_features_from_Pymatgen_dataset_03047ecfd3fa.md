# XRD features (from Pymatgen)

## Metadata

- Dataset ID: `dataset_03047ecfd3fa`
- Aliases: XRD features (from Pymatgen)
- Links: https://pymatgen.org
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- X-ray diffraction (XRD) patterns computed from crystal structures using Pymatgen’s XRDCalculator, smoothed with Gaussian kernel and sampled at 900 evenly spaced 2θ angles (0–90°), yielding fixed-length 900D feature vectors. These features are used in MD-HIT-structure to define structural similarity and generate seven XRD-based non-redundant structure datasets (XRD-nr) for evaluating ALIGNN and DeeperGATGNN on formation energy and band gap prediction under controlled structural redundancy.

## Uses

- [26_MD_HIT](../dataset_uses/26_MD_HIT_XRD_features_from_Pymatgen_dataset_use_e39f8b7257a8_set_use_e39f8b7257a8.md): [26 MD HIT](../papers/26_MD_HIT_paper_364d763e5978.md), [task](../tasks/26_MD_HIT_task_1_task_e55c8a4f2b28.md)

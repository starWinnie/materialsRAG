# 14_Cross_Scale_Covariance - OpenKIM Interatomic Potential Repository

## Dataset Use

A curated collection of 178 interatomic potentials (IPs) for nine FCC metals (Ag, Al, Au, Cu, Ni, Pb, Pd, Pt, Rh), each accompanied by precomputed small-scale material properties—including elastic constants (C11, C12, C44), surface energies ({100}, {110}, {111}), stacking fault energies (uSFE, iSFE), vacancy formation/migration energies, lattice constants, cohesive energies, and thermal expansion coefficients—calculated via standardized KIM Test Drivers. These IPs and their associated properties constitute the statistical pool used to identify covariant small-scale predictors and train regression models linking them to large-scale MD-predicted plastic flow strength.

## Links

- Paper: [14 Cross Scale Covariance](../papers/14_Cross_Scale_Covariance_paper_471a9187e021.md)
- Task: [task page](../tasks/14_Cross_Scale_Covariance_task_1_task_702953135e8f.md)
- Dataset: [OpenKIM Interatomic Potential Repository](../datasets/OpenKIM_Interatomic_Potential_Repository_dataset_f652501a560b.md)
- Dataset URL: https://openkim.org

## Task Context

Predicting plastic flow strength of face-centered cubic (FCC) metals from small-scale quantum-mechanically computable indicator properties, using statistical cross-scale covariance to establish regression models that quantify prediction uncertainty and provide error bounds for first-principles (DFT)-based strength estimates.

## Metadata

- Dataset use ID: `dataset_use_172cb9e4ad0d`
- Original dataset title: OpenKIM Interatomic Potential Repository
- Tags: property prediction, cross-scale modeling, uncertainty quantification

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->

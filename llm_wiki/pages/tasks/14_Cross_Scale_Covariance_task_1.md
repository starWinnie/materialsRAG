# 14_Cross_Scale_Covariance - Task 1

## Task Description

Predicting plastic flow strength of face-centered cubic (FCC) metals from small-scale quantum-mechanically computable indicator properties, using statistical cross-scale covariance to establish regression models that quantify prediction uncertainty and provide error bounds for first-principles (DFT)-based strength estimates.

## Metadata

- Task ID: `task_702953135e8f`
- Source paper: [14 Cross Scale Covariance](../papers/14_Cross_Scale_Covariance.md)
- Tags: property prediction, cross-scale modeling, uncertainty quantification

## Supporting Datasets

### [OpenKIM Interatomic Potential Repository](../datasets/OpenKIM_Interatomic_Potential_Repository.md)

- Usage page: [usage note](../dataset_uses/14_Cross_Scale_Covariance_OpenKIM_Interatomic_Potential_Repository_dataset_use_172cb9e4ad0.md)
- Original title in paper: OpenKIM Interatomic Potential Repository
- Link: https://openkim.org

A curated collection of 178 interatomic potentials (IPs) for nine FCC metals (Ag, Al, Au, Cu, Ni, Pb, Pd, Pt, Rh), each accompanied by precomputed small-scale material properties—including elastic constants (C11, C12, C44), surface energies ({100}, {110}, {111}), stacking fault energies (uSFE, iSFE), vacancy formation/migration energies, lattice constants, cohesive energies, and thermal expansion coefficients—calculated via standardized KIM Test Drivers. These IPs and their associated properties constitute the statistical pool used to identify covariant small-scale predictors and train regression models linking them to large-scale MD-predicted plastic flow strength.

### [Custom DFT dataset for FCC metals](../datasets/Custom_DFT_dataset_for_FCC_metals.md)

- Usage page: [usage note](../dataset_uses/14_Cross_Scale_Covariance_Custom_DFT_dataset_for_FCC_metals_dataset_use_444f94157343.md)
- Original title in paper: Custom DFT dataset for FCC metals
- Link: None

Density functional theory (DFT) calculations performed for seven FCC metals (Ag, Al, Au, Cu, Ni, Pd, Pt) to compute three key predictor properties: {111} surface energy, lattice constant, and vacancy migration energy—all in FCC structure. This dataset provides the quantum-accurate input values used to apply the trained cross-scale regression model and predict plastic flow strength; it supports the core task of transferring statistical covariance learned from IPs to DFT-based predictions with quantified uncertainty.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->

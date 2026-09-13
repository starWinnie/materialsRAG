# 31_Superconductivity_Ordered_Disordered - Inorganic Crystal Structure Database

## Dataset Use

The ICSD contains over 200,000 experimentally determined ordered and disordered inorganic crystal structures. In this paper, it serves two roles: (1) as the source of structural data used to construct SuperCon3D via matching with SuperCon entries; and (2) as the external candidate pool for high-Tc screening — SODNet is applied to predict Tc for ~200k ICSD entries (including disordered ones), yielding 27 prioritized candidates (e.g., Ba1.1432Co0.1429O3.0009Rh0.8574, ErH3) for experimental follow-up. Thus, ICSD supports both dataset construction and real-world superconductor screening.

## Links

- Paper: [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered.md)
- Task: [task page](../tasks/31_Superconductivity_Ordered_Disordered_task_1.md)
- Dataset: [Inorganic Crystal Structure Database](../datasets/Inorganic_Crystal_Structure_Database.md)
- Dataset URL: https://icsd.products.fiz-karlsruhe.de/

## Task Context

Predicting the superconducting transition temperature (Tc) of materials given their 3D crystal structures — including both ordered and disordered configurations — to enable high-Tc superconductor screening from known structural databases such as ICSD. The task supports identifying promising candidate superconductors for experimental validation by ranking structures based on predicted Tc values.

## Metadata

- Dataset use ID: `dataset_use_e6e877944244`
- Original dataset title: ICSD (Inorganic Crystal Structure Database)
- Tags: Tc prediction, superconductor screening, disordered structure modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->

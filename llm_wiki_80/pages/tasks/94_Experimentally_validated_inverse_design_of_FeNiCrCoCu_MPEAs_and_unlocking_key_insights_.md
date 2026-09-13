# 94_Experimentally validated inverse design of FeNiCrCoCu MPEAs and unlocking key insights with explainable AI - Task 1

## Task Description

Predicting unstable stacking fault energy (USFE) and bulk modulus for FeNiCrCoCu multi-principal element alloys (MPEAs) to enable inverse design of compositions with simultaneously high bulk modulus (>210 GPa) and targeted USFE values (e.g., 425 mJ/m² for high strength or 310 mJ/m² for enhanced ductility), supporting the selection of experimentally synthesizable candidates.

## Metadata

- Task ID: `task_96ff05a61f9f`
- Source paper: [94 Experimentally validated inverse design of FeNiCrCoCu MPEAs and unlocking key insights with explainable AI](../papers/94_Experimentally_validated_inverse_design_of_FeNiCrCoCu_MPEAs_and_unlocking_key_insights_.md)
- Tags: inverse design, property prediction, mechanical property optimization

## Supporting Datasets

### [PSO-guided MD simulation dataset for FeNiCrCoCu MPEAs](../datasets/PSO-guided_MD_simulation_dataset_for_FeNiCrCoCu_MPEAs.md)

- Usage page: [usage note](../dataset_uses/94_Experimentally_validated_inverse_design_of_FeNiCrCoCu_MPEAs_and_unlocking_key_insights_.md)
- Original title in paper: PSO-guided MD simulation dataset for FeNiCrCoCu MPEAs
- Link: https://github.com/Deshmukh-Group/Code_For_XAI_MPEA.git

A computationally generated dataset containing 19,728 MPEA compositions (59,184 atomistic structures) of FeNiCrCoCu, each with atomic fractions constrained between 5–35% per element. For each composition, molecular dynamics (MD) simulations using an embedded atom method (EAM) potential computed bulk modulus, elastic constants (C11, C12, C44), Young’s modulus, and unstable stacking fault energy (USFE). The dataset was enriched via Particle Swarm Optimization (PSO) to over-sample regions of high bulk modulus and USFE, enabling training of surrogate models for inverse design. It directly supports training the SEML model for USFE prediction and the 1D CNN model for bulk modulus prediction.

# PSO-guided MD simulation dataset for FeNiCrCoCu MPEAs

## Metadata

- Dataset ID: `dataset_365c107f1a7d`
- Aliases: PSO-guided MD simulation dataset for FeNiCrCoCu MPEAs
- Links: https://github.com/Deshmukh-Group/Code_For_XAI_MPEA.git
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A computationally generated dataset containing 19,728 MPEA compositions (59,184 atomistic structures) of FeNiCrCoCu, each with atomic fractions constrained between 5–35% per element. For each composition, molecular dynamics (MD) simulations using an embedded atom method (EAM) potential computed bulk modulus, elastic constants (C11, C12, C44), Young’s modulus, and unstable stacking fault energy (USFE). The dataset was enriched via Particle Swarm Optimization (PSO) to over-sample regions of high bulk modulus and USFE, enabling training of surrogate models for inverse design. It directly supports training the SEML model for USFE prediction and the 1D CNN model for bulk modulus prediction.

## Uses

- [94_Experimentally validated inverse design of FeNiCrCoCu MPEAs and unlocking key insights with explainable AI](../dataset_uses/94_Experimentally_validated_inverse_design_of_FeNiCrCoCu_MPEAs_and_unlocking_key_insights_.md): [94 Experimentally validated inverse design of FeNiCrCoCu MPEAs and unlocking key insights with explainable AI](../papers/94_Experimentally_validated_inverse_design_of_FeNiCrCoCu_MPEAs_and_unlocking_key_insights_.md), [task](../tasks/94_Experimentally_validated_inverse_design_of_FeNiCrCoCu_MPEAs_and_unlocking_key_insights_.md)

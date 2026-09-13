# 95_Networking autonomous material exploration systems through transfer learning - Task 1

## Task Description

Designing a framework for networking autonomous material exploration systems via transfer learning to improve the efficiency of discovering materials with high values of target properties—specifically, high magnetic moment (M), high Curie temperature (Tc), and high spin polarization (Sp)—by enabling real-time, selective knowledge sharing across systems targeting different but correlated material properties.

## Metadata

- Task ID: `task_731006d33abd`
- Source paper: [95 Networking autonomous material exploration systems through transfer learning](../papers/95_Networking_autonomous_material_exploration_systems_through_transfer_learning.md)
- Tags: autonomous discovery, transfer learning, multi-property optimization

## Supporting Datasets

### [B2-structured ternary alloy dataset](../datasets/B2-structured_ternary_alloy_dataset.md)

- Usage page: [usage note](../dataset_uses/95_Networking_autonomous_material_exploration_systems_through_transfer_learning_B2-structu.md)
- Original title in paper: B2-structured ternary alloy dataset
- Link: https://doi.org/10.48505/nims.5364

A high-throughput DFT-calculated dataset containing magnetic moment (M), Curie temperature (Tc), and spin polarization (Sp) values for 16,908 ternary alloys with B2 crystal structure, composed of 38 elements (e.g., Fe, Co, Ni, Mn, Cr, Ti, V). This dataset serves as the shared candidate search space and ground-truth reference for training and validating ensemble neural network models (ENMs) and transfer learning models (TLMs) in all three autonomous systems (ASM, ASTc, ASSp); it supports property prediction, Bayesian optimization, model selection, and retrospective evaluation of generalization on unobserved materials.

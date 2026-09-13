# 65_Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation - Materials Project

## Dataset Use

A large-scale DFT-computed database of over 2 million crystal structures, used to train Mat2Seq for literature-based generalization (Section 4.2); specifically, ~2.05M structures optimized via DFT were used to enable generation of recently discovered crystals not seen during training, supporting validity, hit rate, and novelty evaluation.

## Links

- Paper: [65 Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation](../papers/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation.md)
- Task: [task page](../tasks/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation_t.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Generating novel, stable 3D crystalline material structures from scratch—either unconditionally or conditioned on input compositions or target physical properties (e.g., band gap)—using autoregressive language models, while ensuring that mathematically equivalent crystal structures (under SE(3) transformations and periodic lattice equivalences) map to identical sequence representations.

## Metadata

- Dataset use ID: `dataset_use_022ff544a13d`
- Original dataset title: Materials Project
- Tags: crystal structure generation, conditional generation, materials discovery, invariant representation, language model generation

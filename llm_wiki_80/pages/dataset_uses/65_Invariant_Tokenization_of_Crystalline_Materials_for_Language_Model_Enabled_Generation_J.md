# 65_Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation - JARVIS-DFT

## Dataset Use

A dataset of 61,541 crystal structures with corresponding DFT-calculated band gap values; used to fine-tune the pre-trained Mat2Seq model for property-conditioned generation (e.g., band gap < 0.5 eV or > 3.0 eV), enabling targeted discovery of crystals with desired electronic properties via token-based conditioning.

## Links

- Paper: [65 Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation](../papers/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation.md)
- Task: [task page](../tasks/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation_t.md)
- Dataset: [JARVIS-DFT](../datasets/JARVIS-DFT.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Generating novel, stable 3D crystalline material structures from scratch—either unconditionally or conditioned on input compositions or target physical properties (e.g., band gap)—using autoregressive language models, while ensuring that mathematically equivalent crystal structures (under SE(3) transformations and periodic lattice equivalences) map to identical sequence representations.

## Metadata

- Dataset use ID: `dataset_use_9baa3fa9f82a`
- Original dataset title: JARVIS-DFT
- Tags: crystal structure generation, conditional generation, materials discovery, invariant representation, language model generation

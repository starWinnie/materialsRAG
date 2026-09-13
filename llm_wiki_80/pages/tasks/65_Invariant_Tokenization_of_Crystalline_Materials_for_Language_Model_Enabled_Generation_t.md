# 65_Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation - Task 1

## Task Description

Generating novel, stable 3D crystalline material structures from scratch—either unconditionally or conditioned on input compositions or target physical properties (e.g., band gap)—using autoregressive language models, while ensuring that mathematically equivalent crystal structures (under SE(3) transformations and periodic lattice equivalences) map to identical sequence representations.

## Metadata

- Task ID: `task_8104bf9bacc0`
- Source paper: [65 Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation](../papers/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation.md)
- Tags: crystal structure generation, conditional generation, materials discovery, invariant representation, language model generation

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation_P.md)
- Original title in paper: Perov-5
- Link: None

A dataset of 18,928 perovskite materials, each with up to 5 atoms in the unit cell and similar structural motifs. It is used to train and evaluate Mat2Seq for crystal structure prediction under composition conditioning, specifically assessing match rate and RMSE against ground truth structures for perovskite systems.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation_C.md)
- Original title in paper: Carbon-24
- Link: None

A dataset of 10,153 carbon-based crystalline materials, each containing at most 24 atoms in the unit cell. It serves as a benchmark for evaluating Mat2Seq’s generalization to diverse, non-perovskite structures with higher atomic complexity during unconditional and composition-conditioned generation.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation_M.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org/

A subset of the Materials Project database containing 45,231 stable inorganic crystals, each with ≤20 atoms per unit cell and covering experimentally observed and DFT-stable materials. It is used for training Mat2Seq, evaluating uniqueness (via periodic boundary shifting), and benchmarking match rate/RMSE across one-shot and 20-shot generation; includes 3,819 experimentally observed entries for real-world applicability validation.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation_M.md)
- Original title in paper: MPTS-52
- Link: None

A challenging dataset of 40,476 crystals with up to 52 atoms per unit cell, curated by DiffCSP to stress-test generative models on large, complex unit cells. It is used to evaluate Mat2Seq’s robustness in high-complexity crystal generation, where structural fidelity and lattice parameter accuracy are critical for match rate and RMSE assessment.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation_M.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org/

A large-scale DFT-computed database of over 2 million crystal structures, used to train Mat2Seq for literature-based generalization (Section 4.2); specifically, ~2.05M structures optimized via DFT were used to enable generation of recently discovered crystals not seen during training, supporting validity, hit rate, and novelty evaluation.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation_O.md)
- Original title in paper: OQMD
- Link: https://oqmd.org/

The Open Quantum Materials Database, containing DFT-optimized crystal structures beyond those in Materials Project; used alongside Materials Project and NOMAD (~2.05M total structures) to expand training coverage for generalization to novel literature-reported crystals, improving compositional and structural diversity in the training set.

### [NOMAD](../datasets/NOMAD.md)

- Usage page: [usage note](../dataset_uses/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation_N.md)
- Original title in paper: NOMAD
- Link: https://nomad-lab.eu/

A distributed repository of computational materials science data, including DFT-optimized crystal structures; combined with Materials Project and OQMD to form a ~2.05M training corpus for Mat2Seq’s conditional generation capability, enabling robust generalization to unseen compositions and structures from recent literature.

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/65_Invariant_Tokenization_of_Crystalline_Materials_for_Language_Model_Enabled_Generation_J.md)
- Original title in paper: JARVIS-DFT
- Link: https://jarvis.nist.gov/

A dataset of 61,541 crystal structures with corresponding DFT-calculated band gap values; used to fine-tune the pre-trained Mat2Seq model for property-conditioned generation (e.g., band gap < 0.5 eV or > 3.0 eV), enabling targeted discovery of crystals with desired electronic properties via token-based conditioning.

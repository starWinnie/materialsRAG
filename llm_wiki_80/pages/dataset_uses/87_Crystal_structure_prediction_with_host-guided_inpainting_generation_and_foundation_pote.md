# 87_Crystal structure prediction with host-guided inpainting generation and foundation potentials - Alexandria

## Dataset Use

A large-scale materials database built from high-throughput DFT calculations, covering diverse inorganic compounds and extended structures. The paper mentions it as a training resource used by MatterGen (a related baseline model), and while CHGGen itself is trained on Materials Project, Alexandria is cited contextually as part of the broader ecosystem of foundational datasets supporting GNN-based diffusion models for CSP — however, the text does not state that CHGGen directly uses Alexandria for training or evaluation. Therefore, per extraction rules, it is excluded.

## Links

- Paper: [87 Crystal structure prediction with host-guided inpainting generation and foundation potentials](../papers/87_Crystal_structure_prediction_with_host-guided_inpainting_generation_and_foundation_pote.md)
- Task: [task page](../tasks/87_Crystal_structure_prediction_with_host-guided_inpainting_generation_and_foundation_pote.md)
- Dataset: [Alexandria](../datasets/Alexandria.md)
- Dataset URL: None

## Task Context

Predicting symmetric and thermodynamically stable crystal structures for target chemical compositions—particularly in systems with polyanions (e.g., Zn–P–S) or intercalation chemistry (e.g., Li–Si)—by generating atomic coordinates conditioned on symmetrized host frameworks, thereby overcoming the locality bias of unconditional diffusion models and improving success rates for long-range crystalline order.

## Metadata

- Dataset use ID: `dataset_use_056d3fc91d80`
- Original dataset title: Alexandria
- Tags: crystal structure prediction, symmetric structure generation, host-guided inpainting

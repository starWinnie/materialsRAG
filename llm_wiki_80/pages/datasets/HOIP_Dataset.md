# HOIP Dataset

## Metadata

- Dataset ID: `dataset_1b9ea456752c`
- Aliases: HOIP Dataset (Hybrid Organic–Inorganic Perovskite Dataset), Hybrid Organic-Inorganic Perovskite (HOIP) dataset
- Links: https://doi.org/10.1038/sdata.2017.152, https://doi.org/10.5061/dryad.gq3rg
- Used by papers: 2
- Dataset usage records: 2

## Description Examples

- A merged dataset of 2,103 HOIP crystals compiled from two prior sources (Kim et al., 2017 and Nakajima & Sawada, 2017); used to evaluate ct-UAEs in data-scarce regimes where traditional ML models underperform. Supports the task by serving as a low-data target domain for transfer learning—ct-UAEs pretrained on MP* significantly improve formation energy prediction accuracy (e.g., 34% MAE reduction for MEGNET), directly addressing the challenge of data scarcity in complex functional materials.
- A density functional theory (DFT)-calculated dataset containing 1345 perovskite compounds, each composed of organic/inorganic cations (Ge, Sn, Pb) and anions (F, Cl, Br, I), along with computed bandgaps and other properties. It is partitioned into 12 domains based on cation–anion combinations; two extrapolative tasks—HOIP-GeF (excluding Ge+F compounds) and HOIP-PbI (excluding Pb+I compounds)—are defined by withholding entire chemical combinations from training. The dataset supports evaluating extrapolative bandgap prediction when the model must generalize to unseen elemental pairings not present in the support set.

## Uses

- [06_Transformer_Atomic_Embeddings](../dataset_uses/06_Transformer_Atomic_Embeddings_HOIP_Dataset_dataset_use_c9f9564247e0.md): [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings.md), [task](../tasks/06_Transformer_Atomic_Embeddings_task_1.md)
- [15_Extrapolative_Episodic_Training](../dataset_uses/15_Extrapolative_Episodic_Training_HOIP_Dataset_dataset_use_ed93b5e1b852.md): [15 Extrapolative Episodic Training](../papers/15_Extrapolative_Episodic_Training.md), [task](../tasks/15_Extrapolative_Episodic_Training_task_1.md)

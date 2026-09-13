# 15_Extrapolative_Episodic_Training - HOIP Dataset

## Dataset Use

A density functional theory (DFT)-calculated dataset containing 1345 perovskite compounds, each composed of organic/inorganic cations (Ge, Sn, Pb) and anions (F, Cl, Br, I), along with computed bandgaps and other properties. It is partitioned into 12 domains based on cation–anion combinations; two extrapolative tasks—HOIP-GeF (excluding Ge+F compounds) and HOIP-PbI (excluding Pb+I compounds)—are defined by withholding entire chemical combinations from training. The dataset supports evaluating extrapolative bandgap prediction when the model must generalize to unseen elemental pairings not present in the support set.

## Links

- Paper: [15 Extrapolative Episodic Training](../papers/15_Extrapolative_Episodic_Training.md)
- Task: [task page](../tasks/15_Extrapolative_Episodic_Training_task_1.md)
- Dataset: [HOIP Dataset](../datasets/HOIP_Dataset.md)
- Dataset URL: https://doi.org/10.5061/dryad.gq3rg

## Task Context

Predicting physical properties of materials in extrapolative regimes—i.e., for material classes or compositions lying outside the distribution of training data—by learning a generalizable mapping y = f(x, S) that conditions predictions on a support set S of previously seen examples, enabling rapid adaptation to unseen domains with minimal target-domain data.

## Metadata

- Dataset use ID: `dataset_use_ed93b5e1b852`
- Original dataset title: HOIP Dataset (Hybrid Organic–Inorganic Perovskite Dataset)
- Tags: property prediction, extrapolation, meta-learning

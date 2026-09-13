# 15_Extrapolative_Episodic_Training - Task 1

## Task Description

Predicting physical properties of materials in extrapolative regimes—i.e., for material classes or compositions lying outside the distribution of training data—by learning a generalizable mapping y = f(x, S) that conditions predictions on a support set S of previously seen examples, enabling rapid adaptation to unseen domains with minimal target-domain data.

## Metadata

- Task ID: `task_66e2dba11ca7`
- Source paper: [15 Extrapolative Episodic Training](../papers/15_Extrapolative_Episodic_Training.md)
- Tags: property prediction, extrapolation, meta-learning

## Supporting Datasets

### [RadonPy Polymer Dataset](../datasets/RadonPy_Polymer_Dataset.md)

- Usage page: [usage note](../dataset_uses/15_Extrapolative_Episodic_Training_RadonPy_Polymer_Dataset_dataset_use_62f7a8c2d887.md)
- Original title in paper: RadonPy Polymer Dataset
- Link: None

A computationally generated dataset of 69,480 amorphous homopolymers (with 68,700 refractive index entries), classified into 20 polymer classes (e.g., polyimide, polystyrene, polyesters), where properties—including specific heat at constant pressure (Cp) and refractive index—are calculated via all-atom molecular dynamics simulations using RadonPy. The dataset is used to construct extrapolative episodic training tasks: for each test class (e.g., p13 polyimide), models are trained on the other 19 classes and evaluated on held-out samples from the excluded class, enabling evaluation of cross-class extrapolative property prediction.

### [HOIP Dataset](../datasets/HOIP_Dataset.md)

- Usage page: [usage note](../dataset_uses/15_Extrapolative_Episodic_Training_HOIP_Dataset_dataset_use_ed93b5e1b852.md)
- Original title in paper: HOIP Dataset (Hybrid Organic–Inorganic Perovskite Dataset)
- Link: https://doi.org/10.5061/dryad.gq3rg

A density functional theory (DFT)-calculated dataset containing 1345 perovskite compounds, each composed of organic/inorganic cations (Ge, Sn, Pb) and anions (F, Cl, Br, I), along with computed bandgaps and other properties. It is partitioned into 12 domains based on cation–anion combinations; two extrapolative tasks—HOIP-GeF (excluding Ge+F compounds) and HOIP-PbI (excluding Pb+I compounds)—are defined by withholding entire chemical combinations from training. The dataset supports evaluating extrapolative bandgap prediction when the model must generalize to unseen elemental pairings not present in the support set.

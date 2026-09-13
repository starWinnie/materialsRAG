# 15_Extrapolative_Episodic_Training - RadonPy Polymer Dataset

## Dataset Use

A computationally generated dataset of 69,480 amorphous homopolymers (with 68,700 refractive index entries), classified into 20 polymer classes (e.g., polyimide, polystyrene, polyesters), where properties—including specific heat at constant pressure (Cp) and refractive index—are calculated via all-atom molecular dynamics simulations using RadonPy. The dataset is used to construct extrapolative episodic training tasks: for each test class (e.g., p13 polyimide), models are trained on the other 19 classes and evaluated on held-out samples from the excluded class, enabling evaluation of cross-class extrapolative property prediction.

## Links

- Paper: [15 Extrapolative Episodic Training](../papers/15_Extrapolative_Episodic_Training.md)
- Task: [task page](../tasks/15_Extrapolative_Episodic_Training_task_1.md)
- Dataset: [RadonPy Polymer Dataset](../datasets/RadonPy_Polymer_Dataset.md)
- Dataset URL: None

## Task Context

Predicting physical properties of materials in extrapolative regimes—i.e., for material classes or compositions lying outside the distribution of training data—by learning a generalizable mapping y = f(x, S) that conditions predictions on a support set S of previously seen examples, enabling rapid adaptation to unseen domains with minimal target-domain data.

## Metadata

- Dataset use ID: `dataset_use_62f7a8c2d887`
- Original dataset title: RadonPy Polymer Dataset
- Tags: property prediction, extrapolation, meta-learning

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->

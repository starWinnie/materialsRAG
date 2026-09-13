# 01_PRDNet - Materials Project

## Dataset Use

A large-scale DFT-computed database of inorganic crystalline materials containing 122,959 stable structures, each annotated with formation energy, band gap, metal/non-metal classification, and—on a subset of 9,473 entries—mechanical properties including bulk modulus, shear modulus, and Young’s modulus. The dataset is used in this paper to train and evaluate PRDNet for multi-task crystal property prediction, serving as the primary benchmark for regression and classification tasks.

## Links

- Paper: [01 PRDNet](../papers/01_PRDNet.md)
- Task: [task page](../tasks/01_PRDNet_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://huggingface.co/datasets/caobin/CPPbenchmark

## Task Context

Predicting multiple physical properties of crystalline materials—including formation energy, band gap, bulk modulus, shear modulus, Young's modulus, exfoliation energy, dielectric constant (refractive index), and metal/non-metal classification—from their atomic structure (i.e., crystal graph defined by atomic types, fractional coordinates, and lattice vectors).

## Metadata

- Dataset use ID: `dataset_use_eb53342235c5`
- Original dataset title: Materials Project
- Tags: crystal property prediction, materials property regression, materials property classification

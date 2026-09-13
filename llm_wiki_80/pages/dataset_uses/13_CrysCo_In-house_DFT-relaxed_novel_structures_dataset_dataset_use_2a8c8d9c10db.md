# 13_CrysCo - In-house DFT-relaxed novel structures dataset

## Dataset Use

A custom dataset of 751 novel crystalline structures generated and DFT-relaxed internally by the authors. It contains ground-truth formation energies and energies above the convex hull computed via first-principles methods. This dataset is used exclusively for out-of-distribution evaluation—testing the model’s generalization capability on materials not present in the Materials Project—by predicting Ef and EHull and reporting parity plots, Pearson correlations (0.894 and 0.931), and MAEs (0.0318 and 0.0294 eV/atom), thereby validating real-world applicability for new material discovery.

## Links

- Paper: [13 CrysCo](../papers/13_CrysCo.md)
- Task: [task page](../tasks/13_CrysCo_task_1.md)
- Dataset: [In-house DFT-relaxed novel structures dataset](../datasets/In-house_DFT-relaxed_novel_structures_dataset.md)
- Dataset URL: None

## Task Context

Predicting multiple inorganic materials properties—including energy-related properties (formation energy, energy above convex hull, band gap) and data-scarce mechanical properties (bulk modulus, shear modulus)—using a hybrid graph-transformer model that explicitly incorporates four-body atomic interactions to improve accuracy, generalization, and interpretability, especially under limited data conditions.

## Metadata

- Dataset use ID: `dataset_use_2a8c8d9c10db`
- Original dataset title: In-house DFT-relaxed novel structures dataset
- Tags: property prediction, mechanical property prediction, thermodynamic stability prediction

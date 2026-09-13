# RadonPy Polymer Dataset

## Metadata

- Dataset ID: `dataset_44aa2507e9ca`
- Aliases: RadonPy Polymer Dataset
- Links: None
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A computationally generated dataset of 69,480 amorphous homopolymers (with 68,700 refractive index entries), classified into 20 polymer classes (e.g., polyimide, polystyrene, polyesters), where properties—including specific heat at constant pressure (Cp) and refractive index—are calculated via all-atom molecular dynamics simulations using RadonPy. The dataset is used to construct extrapolative episodic training tasks: for each test class (e.g., p13 polyimide), models are trained on the other 19 classes and evaluated on held-out samples from the excluded class, enabling evaluation of cross-class extrapolative property prediction.

## Uses

- [15_Extrapolative_Episodic_Training](../dataset_uses/15_Extrapolative_Episodic_Training_RadonPy_Polymer_Dataset_dataset_us_set_use_62f7a8c2d887.md): [15 Extrapolative Episodic Training](../papers/15_Extrapolative_Episodic_Training_paper_92747bbddb26.md), [task](../tasks/15_Extrapolative_Episodic_Training_task_1_task_66e2dba11ca7.md)

# RadonPy Polymer Dataset

## Ontology Type
DatasetUse

## Usage Description
A computationally generated dataset of 69,480 amorphous homopolymers (with 68,700 refractive index entries), classified into 20 polymer classes (e.g., polyimide, polystyrene, polyesters), where properties—including specific heat at constant pressure (Cp) and refractive index—are calculated via all-atom molecular dynamics simulations using RadonPy. The dataset is used to construct extrapolative episodic training tasks: for each test class (e.g., p13 polyimide), models are trained on the other 19 classes and evaluated on held-out samples from the excluded class, enabling evaluation of cross-class extrapolative property prediction.

## Dataset
- [RadonPy Polymer Dataset](../datasets/radonpy_polymer_dataset.md)

## Task
- [15_Extrapolative_Episodic_Training.pdf](../tasks/15_extrapolative_episodic_training_pdf.md)

## Paper
- [15 Extrapolative Episodic Training](../papers/15_extrapolative_episodic_training.md)

## Provided Representations
- [composition](../representations/composition.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Benchmarking / Evaluation](../stages/benchmarking_evaluation.md)

## Evidence
- A computationally generated dataset of 69,480 amorphous homopolymers (with 68,700 refractive index entries), classified into 20 polymer classes (e.g., polyimide, polystyrene, polyesters), where properties—including specific heat at constant pressure (Cp) and refractive index—are calculated via all-atom molecular dynamics simulations using RadonPy. The dataset is used to construct extrapolative episodic training tasks: for each test class (e.g., p13 polyimide), models are trained on the other 19 classes and evaluated on held-out samples from the excluded class, enabling evaluation of cross-class extrapolative property prediction.

## Metadata
dataset_use_id: `dataset_use_62f7a8c2d887`
link: None

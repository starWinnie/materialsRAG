# Materials Project (v2023.11.1) Dielectric Dataset

## Ontology Type
DatasetUse

## Usage Description
A DFT-calculated dataset of 7,277 inorganic crystal structures with computed dielectric tensors, sourced from the Materials Project database. It contains three components per material: electronic dielectric tensor (ε∞), ionic dielectric tensor (ε⁰), and their sum (total ε), each as symmetric 3×3 tensors. After cleaning—removing entries with any tensor element outside [−10, 100] and structures containing elements unsupported by PFP—6,648 structures remained. This dataset is used to train and evaluate the DTNet model for equivariant dielectric tensor prediction across 72 elements and all crystal systems.

## Dataset
- [Materials Project (v2023.11.1) Dielectric Dataset](../datasets/materials_project_v2023_11_1_dielectric_dataset.md)

## Task
- [19_DTNet_Dielectric_Tensor.pdf](../tasks/19_dtnet_dielectric_tensor_pdf.md)

## Paper
- [19 DTNet Dielectric Tensor](../papers/19_dtnet_dielectric_tensor.md)

## Provided Representations
- [crystal structure](../representations/crystal_structure.md)
- [spectrum or tensor](../representations/spectrum_or_tensor.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)

## Evidence
- A DFT-calculated dataset of 7,277 inorganic crystal structures with computed dielectric tensors, sourced from the Materials Project database. It contains three components per material: electronic dielectric tensor (ε∞), ionic dielectric tensor (ε⁰), and their sum (total ε), each as symmetric 3×3 tensors. After cleaning—removing entries with any tensor element outside [−10, 100] and structures containing elements unsupported by PFP—6,648 structures remained. This dataset is used to train and evaluate the DTNet model for equivariant dielectric tensor prediction across 72 elements and all crystal systems.

## Metadata
dataset_use_id: `dataset_use_6abcf98e93f6`
link: https://next-gen.materialsproject.org/api

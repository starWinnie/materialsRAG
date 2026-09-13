# TSENN Dielectric Tensor Dataset

## Ontology Type
DatasetUse

## Usage Description
A custom-curated dataset of 1,432 nonmagnetic bulk semiconductors, selected from the Materials Project based on bandgap (0.3–3 eV), structural stability (energy-above-hull < 0.02 eV/atom), compositional simplicity (<3 elements, <10 atoms/unit cell), and absence of f-electron elements. For each material, first-principles dielectric tensors εαβ(ω) = εαβ₁(ω) + iεαβ₂ were computed using OpenMX within the independent-particle approximation (IPA) via the Kubo formula across 3,001 photon energies (0–30 eV, step 0.01 eV), yielding 1,432 full frequency-dependent complex dielectric tensors satisfying crystal symmetry constraints. This dataset is used to train and evaluate the TSENN model for predicting the complete tensorial optical spectra.

## Dataset
- [TSENN Dielectric Tensor Dataset](../datasets/tsenn_dielectric_tensor_dataset.md)

## Task
- [03_Tensorial_Spectra.pdf](../tasks/03_tensorial_spectra_pdf.md)

## Paper
- [03 Tensorial Spectra](../papers/03_tensorial_spectra.md)

## Provided Representations
- [composition](../representations/composition.md)
- [crystal structure](../representations/crystal_structure.md)
- [spectrum or tensor](../representations/spectrum_or_tensor.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)

## Evidence
- A custom-curated dataset of 1,432 nonmagnetic bulk semiconductors, selected from the Materials Project based on bandgap (0.3–3 eV), structural stability (energy-above-hull < 0.02 eV/atom), compositional simplicity (<3 elements, <10 atoms/unit cell), and absence of f-electron elements. For each material, first-principles dielectric tensors εαβ(ω) = εαβ₁(ω) + iεαβ₂ were computed using OpenMX within the independent-particle approximation (IPA) via the Kubo formula across 3,001 photon energies (0–30 eV, step 0.01 eV), yielding 1,432 full frequency-dependent complex dielectric tensors satisfying crystal symmetry constraints. This dataset is used to train and evaluate the TSENN model for predicting the complete tensorial optical spectra.

## Metadata
dataset_use_id: `dataset_use_81627c0d8816`
link: https://github.com/qmatyanlab/TSENN

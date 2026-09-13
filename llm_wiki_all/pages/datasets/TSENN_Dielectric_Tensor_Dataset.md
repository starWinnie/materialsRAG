# TSENN Dielectric Tensor Dataset

## Metadata

- Dataset ID: `dataset_388341d260b1`
- Aliases: TSENN Dielectric Tensor Dataset
- Links: https://github.com/qmatyanlab/TSENN
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A custom-curated dataset of 1,432 nonmagnetic bulk semiconductors, selected from the Materials Project based on bandgap (0.3–3 eV), structural stability (energy-above-hull < 0.02 eV/atom), compositional simplicity (<3 elements, <10 atoms/unit cell), and absence of f-electron elements. For each material, first-principles dielectric tensors εαβ(ω) = εαβ₁(ω) + iεαβ₂ were computed using OpenMX within the independent-particle approximation (IPA) via the Kubo formula across 3,001 photon energies (0–30 eV, step 0.01 eV), yielding 1,432 full frequency-dependent complex dielectric tensors satisfying crystal symmetry constraints. This dataset is used to train and evaluate the TSENN model for predicting the complete tensorial optical spectra.

## Uses

- [03_Tensorial_Spectra](../dataset_uses/03_Tensorial_Spectra_TSENN_Dielectric_Tensor_Dataset_dataset_use_81627c0d8816.md): [03 Tensorial Spectra](../papers/03_Tensorial_Spectra.md), [task](../tasks/03_Tensorial_Spectra_task_1.md)

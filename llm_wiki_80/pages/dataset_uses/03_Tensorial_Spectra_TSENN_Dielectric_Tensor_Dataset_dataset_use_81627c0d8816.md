# 03_Tensorial_Spectra - TSENN Dielectric Tensor Dataset

## Dataset Use

A custom-curated dataset of 1,432 nonmagnetic bulk semiconductors, selected from the Materials Project based on bandgap (0.3–3 eV), structural stability (energy-above-hull < 0.02 eV/atom), compositional simplicity (<3 elements, <10 atoms/unit cell), and absence of f-electron elements. For each material, first-principles dielectric tensors εαβ(ω) = εαβ₁(ω) + iεαβ₂ were computed using OpenMX within the independent-particle approximation (IPA) via the Kubo formula across 3,001 photon energies (0–30 eV, step 0.01 eV), yielding 1,432 full frequency-dependent complex dielectric tensors satisfying crystal symmetry constraints. This dataset is used to train and evaluate the TSENN model for predicting the complete tensorial optical spectra.

## Links

- Paper: [03 Tensorial Spectra](../papers/03_Tensorial_Spectra.md)
- Task: [task page](../tasks/03_Tensorial_Spectra_task_1.md)
- Dataset: [TSENN Dielectric Tensor Dataset](../datasets/TSENN_Dielectric_Tensor_Dataset.md)
- Dataset URL: https://github.com/qmatyanlab/TSENN

## Task Context

Predicting the full frequency-dependent dielectric tensor (a rank-2, complex-valued, symmetric 3×3 tensor at each photon energy) directly from crystal structure, while strictly respecting crystalline symmetry constraints—including rotational equivariance and correct isotropic/anisotropic decomposition—to enable accurate modeling of anisotropic optical responses for optoelectronic materials design.

## Metadata

- Dataset use ID: `dataset_use_81627c0d8816`
- Original dataset title: TSENN Dielectric Tensor Dataset
- Tags: tensor prediction, optical property prediction, symmetry-aware modeling

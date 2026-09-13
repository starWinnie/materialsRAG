# C2DB

## Metadata

- Dataset ID: `dataset_68145cf04333`
- Aliases: C2DB, C2DB (Computational 2D Materials Database), Computational 2D Materials Database (C2DB)
- Links: https://c2db.fysik.dtu.dk/, https://cmr.fysik.dtu.dk/c2db/c2db.html, https://www.c2db.org/
- Used by papers: 5
- Dataset usage records: 5

## Description Examples

- A high-throughput DFT database containing structural, electronic, and thermodynamic data for over 4,000 atomically thin 2D materials. Used to train a specialized ECSG variant for predicting thermodynamic stability of 2D materials, supporting the case study on wide-bandgap semiconductor screening.
- A high-throughput computational database containing DFT-derived properties—including piezoelectric tensors—for over 4,000 two-dimensional materials. This paper uses 1350 validated 2D piezoelectric tensor entries (after outlier filtering and symmetry enforcement) to train and test EATGNN on low-dimensional systems. It enables the task of predicting the reduced 3×3 piezoelectric stress tensor for 2D crystals while preserving in-plane rotational equivariance and lattice-symmetry compliance.
- A publicly available computational database containing DFT-relaxed atomic structures and properties of over 4000 experimentally known and predicted 2D materials; in this paper, it provides the 2615 stable 2D materials (ΔHhull < 0.3 eV/atom) used as training data for the CDVAE and as seed structures for lattice decoration, and later hosts all 11630 newly predicted relaxed structures (8599 with ΔHhull < 0.3 eV/atom, 2004 within 50 meV of the convex hull) for community access and validation.
- A database of 11,581 pairs of initial and DFT-relaxed 2D crystal structures covering 62 elements, including monolayers and bilayers. Each entry contains full Cartesian coordinates, lattice vectors, and cell metrics for both unrelaxed and relaxed states. It is used to evaluate DeepRelax’s transfer learning capability—where a model pre-trained on 3D MP data is fine-tuned—to assess generalization to low-dimensional materials without requiring energy/force labels.
- The Computational 2D Materials Database, containing 3,521 experimentally and computationally validated 2D materials; used in this paper to train a dedicated VQCrystal model for 2D crystal generation, generate ~12,000 candidate structures, and perform stability-driven inverse design (e.g., filtering for formation energy < −1 eV/atom, validated via DFT on 23 relaxed structures with 73.91% success rate).

## Uses

- [05_Thermodynamic_Stability_Ensemble](../dataset_uses/05_Thermodynamic_Stability_Ensemble_C2DB_dataset_use_6e03492b67fb.md): [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble.md), [task](../tasks/05_Thermodynamic_Stability_Ensemble_task_1.md)
- [07_EATGNN_Piezoelectric_Tensor](../dataset_uses/07_EATGNN_Piezoelectric_Tensor_C2DB_dataset_use_bd8d17f15f63.md): [07 EATGNN Piezoelectric Tensor](../papers/07_EATGNN_Piezoelectric_Tensor.md), [task](../tasks/07_EATGNN_Piezoelectric_Tensor_task_1.md)
- [47_Data-driven discovery of 2D materials by deep generative models](../dataset_uses/47_Data-driven_discovery_of_2D_materials_by_deep_generative_models_C2DB_dataset_use_2f8382.md): [47 Data-driven discovery of 2D materials by deep generative models](../papers/47_Data-driven_discovery_of_2D_materials_by_deep_generative_models.md), [task](../tasks/47_Data-driven_discovery_of_2D_materials_by_deep_generative_models_task_1.md)
- [70_Scalable crystal structure relaxation using an iteration-free deep generative model with uncertainty quantification](../dataset_uses/70_Scalable_crystal_structure_relaxation_using_an_iteration-free_deep_generative_model_wit.md): [70 Scalable crystal structure relaxation using an iteration-free deep generative model with uncertainty quantification](../papers/70_Scalable_crystal_structure_relaxation_using_an_iteration-free_deep_generative_model_wit.md), [task](../tasks/70_Scalable_crystal_structure_relaxation_using_an_iteration-free_deep_generative_model_wit.md)
- [88_Massive discovery of crystal structures across dimensionalities by leveraging vector quantization](../dataset_uses/88_Massive_discovery_of_crystal_structures_across_dimensionalities_by_leveraging_vector_qu.md): [88 Massive discovery of crystal structures across dimensionalities by leveraging vector quantization](../papers/88_Massive_discovery_of_crystal_structures_across_dimensionalities_by_leveraging_vector_qu.md), [task](../tasks/88_Massive_discovery_of_crystal_structures_across_dimensionalities_by_leveraging_vector_qu.md)

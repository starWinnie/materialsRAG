# JARVIS-DFT

## Metadata

- Dataset ID: `dataset_19d1b1004506`
- Aliases: JARVIS-DFT
- Links: https://jarvis.nist.gov, https://jarvis.nist.gov/, https://jarvis.nist.gov/jarvisdft/
- Used by papers: 4
- Dataset usage records: 4

## Description Examples

- A DFT-based dataset comprising 75,993 3D crystal structures (dft_3d), each annotated with formation energy, band gap (computed using both OPT and MBJ functionals), bulk modulus, shear modulus, total energy, and energy above hull (Ehull). It also includes the JARVIS-DFT-3D-2021 subset (55,723 entries). This dataset supports comprehensive evaluation of PRDNet across diverse electronic and mechanical property prediction tasks, with emphasis on robustness across computational functionals and stability metrics.
- The Joint Automated Repository for Various Integrated Simulations (JARVIS) dataset, which provides DFT-computed properties for ~67,000 experimentally synthesized and hypothetical crystals, including formation energy, band gap (OPT and MBJ), total energy, energy above hull (Ehull), bulk modulus, and shear modulus. The dataset includes Cartesian atomic coordinates, lattice vectors, and symmetry information. In this paper, JARVIS-DFT serves as a benchmark for evaluating predictive accuracy across seven property prediction tasks under identical experimental protocols.
- A publicly available materials database containing 55,722 DFT-calculated crystalline materials, each with 19 computed properties including formation energy, bandgap (OPT and MBJ), total energy, Ehull, bulk modulus (Kv), shear modulus (Gv), SLME (%), and spillage. It provides full 3D structural information: atom types (A), fractional coordinates (F), and lattice vectors (L). In this paper, JARVIS-DFT is used exclusively for the downstream fine-tuning and evaluation phase — i.e., to train and test the crystal property prediction models on nine target properties under standard train/val/test splits (80%/10%/10%).
- A high-throughput density functional theory (DFT) database containing computed properties for over 80,000 inorganic materials, including formation energies, bandgaps, elastic moduli, phonon spectra, and more. In this paper, JARVIS-DFT serves as the primary reference dataset for AI-based property prediction benchmarks (e.g., formation energy per atom, exfoliation energy) and as a source of ground-truth computational data for force-field and quantum computation benchmarking; its pre-split train/validation/test sets enable standardized model training and evaluation in the AI category.

## Uses

- [01_PRDNet](../dataset_uses/01_PRDNet_JARVIS-DFT_dataset_use_77880778a960_set_use_77880778a960.md): [01 PRDNet](../papers/01_PRDNet_paper_5138be33ab55.md), [task](../tasks/01_PRDNet_task_1_task_b7092f83ac79.md)
- [12_PDDFormer](../dataset_uses/12_PDDFormer_JARVIS-DFT_dataset_use_f5d6c5ee4833_set_use_f5d6c5ee4833.md): [12 PDDFormer](../papers/12_PDDFormer_paper_9e212a4383a8.md), [task](../tasks/12_PDDFormer_task_1_task_502a51c697a5.md)
- [23_CrysDiff](../dataset_uses/23_CrysDiff_JARVIS-DFT_dataset_use_8fe9915f1b57_set_use_8fe9915f1b57.md): [23 CrysDiff](../papers/23_CrysDiff_paper_0010b7688bb5.md), [task](../tasks/23_CrysDiff_task_1_task_1f1a85917ec8.md)
- [28_JARVIS_Leaderboard](../dataset_uses/28_JARVIS_Leaderboard_JARVIS-DFT_dataset_use_339beba1dea4_set_use_339beba1dea4.md): [28 JARVIS Leaderboard](../papers/28_JARVIS_Leaderboard_paper_30ac315b16dd.md), [task](../tasks/28_JARVIS_Leaderboard_task_1_task_933637998dc2.md)

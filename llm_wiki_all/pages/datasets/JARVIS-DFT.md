# JARVIS-DFT

## Metadata

- Dataset ID: `dataset_19d1b1004506`
- Aliases: JARVIS-3D, JARVIS-DFT, JARVIS-DFT (2021.8.18), JARVIS-DFT (3D 2021), JARVIS-DFT 3D 2021, JARVIS-DFT dataset
- Links: https://figshare.com/collections/JARVIS-DFT/4301672, https://jarvis.nist.gov, https://jarvis.nist.gov/, https://jarvis.nist.gov/jarvisdft/
- Used by papers: 12
- Dataset usage records: 12

## Description Examples

- A DFT-based dataset comprising 75,993 3D crystal structures (dft_3d), each annotated with formation energy, band gap (computed using both OPT and MBJ functionals), bulk modulus, shear modulus, total energy, and energy above hull (Ehull). It also includes the JARVIS-DFT-3D-2021 subset (55,723 entries). This dataset supports comprehensive evaluation of PRDNet across diverse electronic and mechanical property prediction tasks, with emphasis on robustness across computational functionals and stability metrics.
- A publicly available dataset of 55,723 crystalline materials, each represented by its 3D unit cell (atomic species, Cartesian coordinates, lattice vectors) and annotated with DFT-simulated properties: formation energy per atom, total energy (OptB88vdW), bandgap (OptB88vdW and TBmBJ), and energy above hull. Used in this paper to train and evaluate CrystalFramer on five regression tasks with fixed train/validation/test splits (44,578 / 5,572 / 5,572 for most targets; 14,537 / 1,817 / 1,817 for MBJ bandgap), serving as a benchmark for SE(3)-invariant crystal encoders.
- The Joint Automated Repository for Various Integrated Simulations (JARVIS) dataset, which provides DFT-computed properties for ~67,000 experimentally synthesized and hypothetical crystals, including formation energy, band gap (OPT and MBJ), total energy, energy above hull (Ehull), bulk modulus, and shear modulus. The dataset includes Cartesian atomic coordinates, lattice vectors, and symmetry information. In this paper, JARVIS-DFT serves as a benchmark for evaluating predictive accuracy across seven property prediction tasks under identical experimental protocols.
- A curated collection of DFT-computed crystal tensor properties sourced from the JARVIS-DFT database, containing 4,713 dielectric tensors (unitless relative dielectric constants), 4,998 piezoelectric tensors (in C/m²), and 14,220 elastic tensors (in GPa), each paired with its corresponding crystal structure (atomic positions, lattice vectors, and elemental features). The dataset is constructed by extracting both tensor values and structures directly from consistent DFT calculation files to guarantee alignment between structural symmetry and tensor symmetry constraints, and is used to train and evaluate GMTNet’s ability to predict symmetry-respecting tensors.
- A dataset of 55,723 DFT-computed crystalline materials compiled by Choudhary et al. (2020), available via the JARVIS platform. It includes unit-cell structural data (atomic positions, species, lattice vectors) and properties: formation energy, total energy, bandgap (computed with two functionals: OPT and MBJ), and energy above hull (E_hull). The paper uses it for regression benchmarking across five property prediction tasks, following standardized splits established in prior work (e.g., Yan et al., 2022).

## Uses

- [01_PRDNet](../dataset_uses/01_PRDNet_JARVIS-DFT_dataset_use_77880778a960.md): [01 PRDNet](../papers/01_PRDNet.md), [task](../tasks/01_PRDNet_task_1.md)
- [10_CrystalFramer](../dataset_uses/10_CrystalFramer_JARVIS-DFT_dataset_use_90b21b3174ab.md): [10 CrystalFramer](../papers/10_CrystalFramer.md), [task](../tasks/10_CrystalFramer_task_1.md)
- [12_PDDFormer](../dataset_uses/12_PDDFormer_JARVIS-DFT_dataset_use_f5d6c5ee4833.md): [12 PDDFormer](../papers/12_PDDFormer.md), [task](../tasks/12_PDDFormer_task_1.md)
- [20_GMTNet](../dataset_uses/20_GMTNet_JARVIS-DFT_dataset_use_af6839f5e534.md): [20 GMTNet](../papers/20_GMTNet.md), [task](../tasks/20_GMTNet_task_1.md)
- [22_Crystalformer](../dataset_uses/22_Crystalformer_JARVIS-DFT_dataset_use_394c5b165816.md): [22 Crystalformer](../papers/22_Crystalformer.md), [task](../tasks/22_Crystalformer_task_1.md)
- [23_CrysDiff](../dataset_uses/23_CrysDiff_JARVIS-DFT_dataset_use_8fe9915f1b57.md): [23 CrysDiff](../papers/23_CrysDiff.md), [task](../tasks/23_CrysDiff_task_1.md)
- [24_Structure_Aware_Transfer_Learning](../dataset_uses/24_Structure_Aware_Transfer_Learning_JARVIS-DFT_dataset_use_0ee7894cdd6e.md): [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning.md), [task](../tasks/24_Structure_Aware_Transfer_Learning_task_1.md)
- [28_JARVIS_Leaderboard](../dataset_uses/28_JARVIS_Leaderboard_JARVIS-DFT_dataset_use_339beba1dea4.md): [28 JARVIS Leaderboard](../papers/28_JARVIS_Leaderboard.md), [task](../tasks/28_JARVIS_Leaderboard_task_1.md)
- [33_DenseGNN](../dataset_uses/33_DenseGNN_JARVIS-DFT_dataset_use_e40b11d77764.md): [33 DenseGNN](../papers/33_DenseGNN.md), [task](../tasks/33_DenseGNN_task_1.md)
- [36_PotNet](../dataset_uses/36_PotNet_JARVIS-DFT_dataset_use_945acdb92eb2.md): [36 PotNet](../papers/36_PotNet.md), [task](../tasks/36_PotNet_task_1.md)
- [37_CrysGNN](../dataset_uses/37_CrysGNN_JARVIS-DFT_dataset_use_ba0c2a957168.md): [37 CrysGNN](../papers/37_CrysGNN.md), [task](../tasks/37_CrysGNN_task_1.md)
- [40_ALIGNN](../dataset_uses/40_ALIGNN_JARVIS-DFT_dataset_use_2fedbd6f2004.md): [40 ALIGNN](../papers/40_ALIGNN.md), [task](../tasks/40_ALIGNN_task_1.md)

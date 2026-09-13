# JARVIS-DFT 3D 2021

## Metadata

- Dataset ID: `dataset_2e1ced6293e7`
- Aliases: JARVIS-DFT 3D 2021
- Links: https://jarvis.nist.gov/
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A publicly available dataset of 55,723 crystalline materials, each represented by its 3D unit cell (atomic species, Cartesian coordinates, lattice vectors) and annotated with DFT-simulated properties: formation energy per atom, total energy (OptB88vdW), bandgap (OptB88vdW and TBmBJ), and energy above hull. Used in this paper to train and evaluate CrystalFramer on five regression tasks with fixed train/validation/test splits (44,578 / 5,572 / 5,572 for most targets; 14,537 / 1,817 / 1,817 for MBJ bandgap), serving as a benchmark for SE(3)-invariant crystal encoders.

## Uses

- [10_CrystalFramer](../dataset_uses/10_CrystalFramer_JARVIS-DFT_3D_2021_dataset_use_103f3f743b3b_set_use_103f3f743b3b.md): [10 CrystalFramer](../papers/10_CrystalFramer_paper_376c54bdb055.md), [task](../tasks/10_CrystalFramer_task_1_task_f4a8c4f8f856.md)

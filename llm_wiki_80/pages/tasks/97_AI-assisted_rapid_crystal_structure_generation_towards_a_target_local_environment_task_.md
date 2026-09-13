# 97_AI-assisted rapid crystal structure generation towards a target local environment - Task 1

## Task Description

Generating novel, physically plausible crystal structures of sp2-carbon allotropes that satisfy target local atomic environments (specifically sp2 coordination geometry) and remain within 0.5 eV/atom of graphite’s ground-state energy, starting from a small set of known examples — enabling rapid, symmetry-aware exploration of complex crystals beyond the ~20–30 atom limit of conventional CSP methods.

## Metadata

- Task ID: `task_897b8fe85c77`
- Source paper: [97 AI-assisted rapid crystal structure generation towards a target local environment](../papers/97_AI-assisted_rapid_crystal_structure_generation_towards_a_target_local_environment.md)
- Tags: crystal structure generation, local environment targeting, sp2 carbon allotrope discovery

## Supporting Datasets

### [Samara Carbon Allotrope Database (SACADA)](../datasets/Samara_Carbon_Allotrope_Database_SACADA.md)

- Usage page: [usage note](../dataset_uses/97_AI-assisted_rapid_crystal_structure_generation_towards_a_target_local_environment_Samar.md)
- Original title in paper: Samara Carbon Allotrope Database (SACADA)
- Link: https://sacada.org

A curated database of experimentally and computationally reported 3-periodic carbon allotropes, extracted from scientific literature via Web of Science and Scopus. It contains 140 sp2-carbon structures with full crystallographic data (space group, Wyckoff sites, atomic positions, unit cell parameters) and DFT-computed energies (0–1.344 eV/atom relative to graphite). In this paper, SACADA serves as the primary source for the initial training set of known sp2 allotropes, which is filtered (excluding low-symmetry or large-unit-cell structures) and augmented to build the v1-60k/v2-120k/v3-240k datasets used to train LEGO-xtal’s generative models.

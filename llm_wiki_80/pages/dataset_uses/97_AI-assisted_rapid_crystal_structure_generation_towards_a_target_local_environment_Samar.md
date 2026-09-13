# 97_AI-assisted rapid crystal structure generation towards a target local environment - Samara Carbon Allotrope Database (SACADA)

## Dataset Use

A curated database of experimentally and computationally reported 3-periodic carbon allotropes, extracted from scientific literature via Web of Science and Scopus. It contains 140 sp2-carbon structures with full crystallographic data (space group, Wyckoff sites, atomic positions, unit cell parameters) and DFT-computed energies (0–1.344 eV/atom relative to graphite). In this paper, SACADA serves as the primary source for the initial training set of known sp2 allotropes, which is filtered (excluding low-symmetry or large-unit-cell structures) and augmented to build the v1-60k/v2-120k/v3-240k datasets used to train LEGO-xtal’s generative models.

## Links

- Paper: [97 AI-assisted rapid crystal structure generation towards a target local environment](../papers/97_AI-assisted_rapid_crystal_structure_generation_towards_a_target_local_environment.md)
- Task: [task page](../tasks/97_AI-assisted_rapid_crystal_structure_generation_towards_a_target_local_environment_task_.md)
- Dataset: [Samara Carbon Allotrope Database (SACADA)](../datasets/Samara_Carbon_Allotrope_Database_SACADA.md)
- Dataset URL: https://sacada.org

## Task Context

Generating novel, physically plausible crystal structures of sp2-carbon allotropes that satisfy target local atomic environments (specifically sp2 coordination geometry) and remain within 0.5 eV/atom of graphite’s ground-state energy, starting from a small set of known examples — enabling rapid, symmetry-aware exploration of complex crystals beyond the ~20–30 atom limit of conventional CSP methods.

## Metadata

- Dataset use ID: `dataset_use_c1a2c17859b7`
- Original dataset title: Samara Carbon Allotrope Database (SACADA)
- Tags: crystal structure generation, local environment targeting, sp2 carbon allotrope discovery

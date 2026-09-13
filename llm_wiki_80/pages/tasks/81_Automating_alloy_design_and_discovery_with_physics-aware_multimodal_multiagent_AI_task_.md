# 81_Automating alloy design and discovery with physics-aware multimodal multiagent AI - Task 1

## Task Description

Automating the design and discovery of metallic alloys with enhanced mechanical properties—specifically predicting and optimizing fracture toughness, ductility, dislocation core structure, and Peierls barriers—by integrating physics-based atomistic simulations, theoretical models, and multimodal reasoning across composition, defect structure, and property relationships.

## Metadata

- Task ID: `task_6e54abb27401`
- Source paper: [81 Automating alloy design and discovery with physics-aware multimodal multiagent AI](../papers/81_Automating_alloy_design_and_discovery_with_physics-aware_multimodal_multiagent_AI.md)
- Tags: alloy design, fracture toughness prediction, dislocation modeling

## Supporting Datasets

### [NbMo alloy system computational dataset](../datasets/NbMo_alloy_system_computational_dataset.md)

- Usage page: [usage note](../dataset_uses/81_Automating_alloy_design_and_discovery_with_physics-aware_multimodal_multiagent_AI_NbMo_.md)
- Original title in paper: NbMo alloy system computational dataset
- Link: https://github.com/lamm-mit/AtomAgents

A custom-generated dataset comprising atomistic simulation results for Nb–Mo binary alloys across Nb concentrations (0–100% in 20% intervals), including computed elastic constants, surface energies, unstable stacking fault energies, differential displacement maps for screw dislocations, and Peierls barrier distributions obtained via nudged elastic band (NEB) simulations using a moment tensor potential; used to train and validate the multiagent system’s ability to predict ductility index (D = KIe/KIc), classify ductile vs. brittle behavior, and discover correlations between energy landscape statistics (e.g., SD of potential energy change) and mechanical performance.

### [Tungsten (W) screw dislocation dataset with EAM potentials](../datasets/Tungsten_W_screw_dislocation_dataset_with_EAM_potentials.md)

- Usage page: [usage note](../dataset_uses/81_Automating_alloy_design_and_discovery_with_physics-aware_multimodal_multiagent_AI_Tungs.md)
- Original title in paper: Tungsten (W) screw dislocation dataset with EAM potentials
- Link: https://github.com/lamm-mit/AtomAgents

A curated set of atomistic simulation outputs for body-centered cubic tungsten under two Embedded Atom Method (EAM) potentials—Zhou–Johnson (W_Zhou04.eam.alloy) and Marinica (w_eam4.fs)—including relaxed dislocated structures, pristine lattice references, and generated differential displacement (DD) maps; used to support multimodal image-based classification of polarized vs. unpolarized screw dislocation core structures and benchmark the AI agent’s visual reasoning capability in defect analysis.

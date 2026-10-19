# Dataset: TAPSim-MD virtual [001]-oriented TiAl crystalline tip

- Dataset ID: `D_P305_tapsim_md_virtual_001_oriented_tial_crystalline_tip`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- TAPSim-MD virtual [001]-oriented TiAl crystalline tip
- virtual TiAl crystalline tip
- [001] oriented virtual TiAl crystalline tip
- cylindrical [001]-oriented TiAl tip
- 3800 atoms consisting of a 20 × 20 × 19 substrate cell and an island with 52 atoms

## Observed material scopes

- γ-TiAl
- [001]-oriented stoichiometric, unalloyed TiAl

## Observed research tasks

- interpreting field evaporation through dynamic bond-breaking processes

## Observed research stages

- data_preparation
- model_training
- computational_validation

## Observed properties

- atomic positions
- crystallographic orientation
- geometry (cylinder, 8 nm radius, 24 nm height)
- stoichiometry
- surface morphology

## Observed fields

- atom identity
- x/y/z coordinates
- bond connectivity
- substrate vs. island assignment

## Usage evidence

- P097 (Unexpected field evaporation sequence in γ-TiAl: Interpreting field evaporation through dynamic bond-breaking processes): source in construction of [001]-oriented virtual TiAl crystalline tip — Serve as the initial atomistic model for full-dynamics field evaporation simulation: a cylindrical [001]-oriented TiAl tip with defined geometry and stoichiometry.
- P097 (Unexpected field evaporation sequence in γ-TiAl: Interpreting field evaporation through dynamic bond-breaking processes): training in TAPSim-MD simulation execution with electrostatic voltage ramping — Provide the structural input for TAPSim-MD simulation execution, enabling ab initio prediction of evaporation events and atom trajectories under electrostatic voltage ramping.
- P097 (Unexpected field evaporation sequence in γ-TiAl: Interpreting field evaporation through dynamic bond-breaking processes): computational_validation in analysis of atom trajectories and bond-breaking dynamics — Enable quantitative analysis of atom trajectories and bond-breaking dynamics by providing the full trajectory output from TAPSim-MD simulation.

## Dataset evidence

- P305, PDF page 3, Methods: "A [001] oriented virtual TiAl crystalline tip was constructed in the form of a cylinder with 8 nm in radius and 24 nm in height."
- P305, PDF page 3, Methods: "In order to better analyze the field evaporation mechanism in TiAl within our TAPSim-MD results, we also studied a [001]-TiAl model system in LAMMPS [16,17] with 3800 atoms consisting of a 20 × 20 × 19 substrate cell and an island with 52 atoms on the top surface including a ‘‘test’’ atom in a kink site, as shown in Fig. 4(a)."

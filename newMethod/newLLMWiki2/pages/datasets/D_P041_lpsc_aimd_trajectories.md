# Dataset: LPSC AIMD trajectories

- Dataset ID: `D_P041_lpsc_aimd_trajectories`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- LPSC AIMD trajectories
- fine-tuning dataset
- MD trajectories of an LPSC unit cell (52 atoms) obtained from 100 ps simulations conducted at 600 and 1000 K

## Observed material scopes

- Li6PS5Cl (LPSC)

## Observed research tasks

- fine-tuning pretrained universal machine-learning interatomic potentials

## Observed research stages

- data_acquisition
- data_preparation
- model_training

## Observed properties

- potential energy surface (PES) features
- Li-ion migration configurations

## Observed fields

- atomic configurations
- DFT energies
- forces

## Usage evidence

- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): source in constructing the fine-tuning dataset from AIMD trajectories of LPSC — constructing the fine-tuning dataset from AIMD trajectories of LPSC
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): training in preprocessing datasets for fine-tuning — preprocessing datasets for fine-tuning
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): training in fine-tuning SevenNet-0 using reEWC loss function — fine-tuning SevenNet-0 using reEWC loss function

## Dataset evidence

- P041, PDF page 4, Fine-tuning MLIPs on LPSC dataset: "To construct the fine-tuning dataset, we focus on LPSC, one of the most extensively studied argyrodite-type Li SSEs55. It exhibits fairly high ionic conductivity, approximately 5 mS/cm56, at room temperature. This feature facilitates efficient sampling of diverse Li-ion hopping events within a limited simulation time, making LPSC an ideal system for generating the fine-tuning dataset aimed at enhancing the predictability of Li diffusion in Li SSE systems. The fine-tuning dataset is constructed from MD trajectories of an LPSC unit cell (52 atoms) obtained from 100 ps simulations conducted at 600 and 1000 K. At each temperature, 500 structures are uniformly sampled at 200 fs intervals, resulting in a total of 1000 structures. These structures are then randomly split into training and validation datasets at a 9:1 ratio."

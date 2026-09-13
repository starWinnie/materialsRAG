# Dataset: MPtrj

- Dataset ID: `D_mptrj`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- MPtrj
- MPtrj dataset

## Observed material scopes

- diverse inorganic crystals
- most elements in the periodic table

## Observed research tasks

- fine-tuning pretrained universal machine-learning interatomic potentials

## Observed research stages

- data_acquisition
- model_training

## Observed properties

- energy
- force
- stress

## Observed fields

- atomic configurations
- DFT energies
- forces
- stresses

## Usage evidence

- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): source in constructing the Replay set by sampling from the pretrained MPtrj dataset — constructing the Replay set by sampling from the pretrained MPtrj dataset
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): label_source in fine-tuning SevenNet-0 using reEWC loss function — fine-tuning SevenNet-0 using reEWC loss function

## Dataset evidence

- P041, PDF page 4, Fine-tuning MLIPs on LPSC dataset: "As the pretrained MLIP to be fine-tuned, we employ SevenNet-0 (version dated 11 July 202454), which was trained on the MPtrj dataset22."
- P041, PDF page 1: "pretrained MLIPs by leveraging graph neural networks [...] and training them on large-scale datasets covering most elements in the periodic table, such as the Materials Project18, Alexandria Database19, and OMat2420."

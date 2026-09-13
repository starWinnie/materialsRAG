# Dataset: HOIP dataset

- Dataset ID: `D_hoip_dataset`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- HOIP dataset
- hybrid organic–inorganic perovskite (HOIP) dataset
- HOIP dataset40,41

## Observed material scopes

- hybrid organic–inorganic perovskites

## Observed research tasks

- extrapolative prediction of material properties

## Observed research stages

- data_acquisition
- data_preparation
- candidate_generation
- model_training
- model_evaluation
- candidate_screening

## Observed properties

- bandgap
- dielectric constants
- relative energies

## Observed fields

- crystal structure
- bandgap
- dielectric constants
- relative energies

## Usage evidence

- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): source in acquisition of polymer and perovskite datasets — To acquire computational material property dataset for training and evaluation of perovskite bandgaps.
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): source in descriptor generation for materials — To generate MPNN-encoded latent vectors for crystal structures.
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): candidate_pool in generation of extrapolative episodes — To generate extrapolative episodes by partitioning into 12 anion–cation domains and sampling test instances from one domain and support sets from the remaining ten.
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): training in meta-training of matching neural networks via extrapolative episodic training (E2T) — To train matching neural networks via extrapolative episodic training (E2T) using episodes with (x,y) sampled from one anion–cation combination and support set S from the remaining ten.
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): test in evaluation of extrapolative prediction performance — To evaluate extrapolative prediction performance on held-out anion–cation combination data (HOIP-GeF and HOIP-PbI).
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): training in fine-tuning for downstream extrapolative domains — To fine-tune pretrained E2T models on target-domain HOIP-GeF or HOIP-PbI data.

## Dataset evidence

- P015, PDF page 10, Methods: "The HOIP dataset40,41 contains 1345 perovskite compounds and their properties, including bandgaps, dielectric constants, and relative energies, calculated using the density functional theory."
- P015, PDF page 12, References: "Kim, C., Huan, T. D., Krishnan, S. & Ramprasad, R. A hybrid organic-inorganic perovskite dataset. Scientific Data 4, 170057 (2017)."
- P015, PDF page 12, References: "Kim, C., Huan, T. D., Krishnan, S. & Ramprasad, R. A hybrid organic-inorganic perovskite dataset. https://doi.org/10.5061/dryad.gq3rg (2017)."

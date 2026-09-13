# Dataset: MPtrj dataset

- Dataset ID: `D_mptrj_dataset`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- MPtrj dataset
- pretrained dataset
- MPtrj

## Observed material scopes

- materials across the periodic table up to Pu
- most elements in the periodic table

## Observed research tasks

- developing a foundation machine learning interatomic potential with polarizable long-range interactions
- fine-tuning pretrained universal machine-learning interatomic potentials

## Observed research stages

- data_acquisition
- model_evaluation

## Observed properties

- total potential energy
- forces
- stress
- potential energy
- atomic forces

## Observed fields

- atomic coordinates
- atomic types
- boundary conditions
- atomic positions
- cell parameters
- energies
- forces

## Usage evidence

- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): training in acquiring training datasets — to train the foundation equivariance neural network potential
- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): test in benchmarking the foundation model on the MPtrj dataset and long-range dimer interactions — to benchmark the foundation model's accuracy on large-scale materials property prediction
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): source in constructing the Replay set by random sampling from the pretrained dataset — provide source data for constructing the Replay set

## Dataset evidence

- P039, PDF page 9, Methods: "To train the foundation equivariance neural network potential, we used the MPtrj dataset16 sourced from Materials Projects48 as the training dataset."
- P039, PDF page 10, Data availability: "The MPtrj dataset is also publicly available from the reference94 through https://doi.org/10.6084/m9.figshare.23713842."
- P041, PDF page 4, Fine-tuning MLIPs on LPSC dataset: "As the pretrained MLIP to be fine-tuned, we employ SevenNet-0 (version dated 11 July 202454), which was trained on the MPtrj dataset22."

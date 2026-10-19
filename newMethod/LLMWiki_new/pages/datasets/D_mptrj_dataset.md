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
- Materials Project Trajectory (MPtrj)
- Materials Project Trajectory (MPtrj) dataset
- MPTrj dataset
- MPTrj16

## Observed material scopes

- materials across the periodic table up to Pu
- most elements in the periodic table
- inorganic materials
- crystalline structures
- materials up to Plutonium
- inorganic bulk materials

## Observed research tasks

- developing a foundation machine learning interatomic potential with polarizable long-range interactions
- fine-tuning pretrained universal machine-learning interatomic potentials
- material property prediction and human-AI interaction for materials science
- training Machine Learning Interatomic Potentials (MLIPs) for inorganic materials

## Observed research stages

- data_acquisition
- model_evaluation
- model_training

## Observed properties

- total potential energy
- forces
- stress
- potential energy
- atomic forces
- chemical formula
- space group
- crystal system
- metallicity
- direct bandgap
- stability
- experimental observation
- magnetic status
- magnetic order
- formation energy
- energy above hull
- bandgap
- energy
- cell stress

## Observed fields

- atomic coordinates
- atomic types
- boundary conditions
- atomic positions
- cell parameters
- energies
- forces
- lattice
- mp-id
- energy
- cell stress
- unit cell

## Usage evidence

- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): training in acquiring training datasets — to train the foundation equivariance neural network potential
- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): test in benchmarking the foundation model on the MPtrj dataset and long-range dimer interactions — to benchmark the foundation model's accuracy on large-scale materials property prediction
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): source in constructing the Replay set by random sampling from the pretrained dataset — provide source data for constructing the Replay set
- P050 (MatterChat: A Multi-Modal LLM for Material Science): source in curating dataset of crystalline structures from Materials Project — To obtain a large-scale, high-quality dataset of relaxed inorganic material structures and associated properties.
- P053 (Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models): training in pretraining and fine-tuning of EquiformerV2 and eSEN models on OMat24 and related datasets — to fine-tune pretrained models on domain-specific data

## Dataset evidence

- P039, PDF page 9, Methods: "To train the foundation equivariance neural network potential, we used the MPtrj dataset16 sourced from Materials Projects48 as the training dataset."
- P039, PDF page 10, Data availability: "The MPtrj dataset is also publicly available from the reference94 through https://doi.org/10.6084/m9.figshare.23713842."
- P041, PDF page 4, Fine-tuning MLIPs on LPSC dataset: "As the pretrained MLIP to be fine-tuned, we employ SevenNet-0 (version dated 11 July 202454), which was trained on the MPtrj dataset22."
- P107, PDF page 10, Method: "In this work, we curated a comprehensive dataset from the Materials Project Trajectory (MPtrj) dataset [36], focusing specifically on relaxed samples."
- P107, PDF page 3, Results: "The dataset was curated from the Materials Project [29] and contains 142,899 material structures."
- P110, PDF page 2, 2.1 The OMat24 dataset: "OMat24 was designed to train MLIP models that predict both equilibrium and non-equilibrium properties. It includes equilibrium and non-equilibrium structures, yielding broader label distributions than relaxation-only datasets. We confirm this by comparing final label distributions to MPtrj and Alexandria, shown in Figure 1b, plotting energies relative to elemental bulk phases computed with each dataset’s DFT settings."
- P110, PDF page 2, Results: "We pretrain several variants of the EquiformerV226,27 and eSEN28 architectures on OMat24 and show that, after fine-tuning to account for differences in DFT settings, state-of-the-art results are achieved on the popular MatBench Discovery leaderboard29."

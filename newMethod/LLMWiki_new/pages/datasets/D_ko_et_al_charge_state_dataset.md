# Dataset: Ko et al. charge-state dataset

- Dataset ID: `D_ko_et_al_charge_state_dataset`
- Dataset type: `public_subset`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Ko et al. charge-state dataset
- dataset developed by Ko et al.28
- Ag3+/−
- Na8/9Cl8+
- C10H2/C10H3+
- Au2-MgO

## Observed material scopes

- charged clusters (e.g., Ag3+/−, Na8/9Cl8+)
- molecular systems (e.g., water, C10H2/C10H3+)
- periodic systems (e.g., Au2-MgO)

## Observed research tasks

- developing a foundation machine learning interatomic potential with polarizable long-range interactions

## Observed research stages

- model_evaluation
- candidate_screening

## Observed properties

- total potential energy
- forces

## Observed fields

- atomic coordinates
- atomic types
- boundary conditions

## Usage evidence

- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): benchmark in benchmarking the foundation model on diverse charge-state datasets — to evaluate the capability of the framework in capturing different charge states and long-range interactions
- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): candidate_pool in finetuning the foundation model for ab initio accuracy on specific challenging systems — to perform targeted finetuning for ab initio accuracy on specific challenging systems

## Dataset evidence

- P039, PDF page 3, Validation on diverse charge-state datasets: "To evaluate the capability of our framework in capturing different charge states and long-range interactions, we validated our framework against the dataset developed by Ko et al.28 and Maruf et al.38, which encompass various charge states and charge transfer systems. They contain six distinct subsets: Ag cluster with positive and negative total charge, (Ag3+/−), Na-Cl ionic cluster with one neutral Na removed (Na8/9Cl8+), hydrogenated carbon chains in both neutral and cationic states (C10H2/C10H3+), a periodic system consisting of Au clusters adsorbed on an MgO-(001) surface..."
- P039, PDF page 10, Data availability: "For datasets containing different charge states, the C10H2/C10H3+, Na8/9Cl8+, Ag3+/−and Au2-MgO datasets are publicly available from the reference93 at https://doi.org/10.24435/materialscloud:f3-yh..."

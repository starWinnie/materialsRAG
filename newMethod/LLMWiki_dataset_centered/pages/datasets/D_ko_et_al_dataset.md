# Dataset: Ko et al. dataset

- Dataset ID: `D_ko_et_al_dataset`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Ko et al. dataset
- Ko et al.28
- dataset developed by Ko et al.28

## Observed material scopes

- Ag3+/−
- Na8/9Cl8+
- C10H2/C10H3+
- Au2-MgO

## Observed research tasks

- Develop a foundation machine learning interatomic potential with explicit polarizable long-range interactions

## Observed research stages

- data_acquisition
- model_evaluation
- candidate_screening

## Observed properties

- total potential energy
- forces

## Observed fields

- atomic coordinates
- atomic types
- energies
- forces

## Usage evidence

- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): benchmark in Acquire training datasets including diverse charge-state systems and periodic table elements — Validate framework capability in capturing different charge states and long-range interactions
- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): test in Benchmark model performance on diverse charge-state datasets and physical properties — Benchmark model performance on diverse charge-state systems
- P039 (A foundation machine learning potential with polarizable long-range interactions for materials modelling): candidate_pool in Screen candidate systems for finetuning to achieve ab initio accuracy — Screen candidate systems for finetuning to achieve ab initio accuracy

## Dataset evidence

- P039, PDF page 3, Validation on diverse charge-state datasets: "To evaluate the capability of our framework in capturing different charge states and long-range interactions, we validated our framework against the dataset developed by Ko et al.28 and Maruf et al.38, which encompass various charge states and charge transfer systems."
- P039, PDF page 3, Validation on diverse charge-state datasets: "They contain six distinct subsets: Ag cluster with positive and negative total charge, (Ag3+/−), Na-Cl ionic cluster with one neutral Na removed (Na8/9Cl8+), hydrogenated carbon chains in both neutral and cationic states (C10H2/C10H3+), a periodic system consisting of Au clusters adsorbed on an MgO-(001) surface..."
- P039, PDF page 10, Data availability: "The C10H2/C10H3+, Na8/9Cl8+, Ag3+/−and Au2-MgO datasets are publicly available from the reference93 at https://doi.org/10.24435/materialscloud:f3-yh..."

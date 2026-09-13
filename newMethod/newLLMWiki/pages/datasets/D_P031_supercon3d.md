# Dataset: SuperCon3D

- Dataset ID: `D_P031_supercon3d`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- SuperCon3D

## Observed material scopes

- crystals
- superconductors
- ordered and disordered structures

## Observed research tasks

- designing novel superconducting candidates

## Observed research stages

- data_acquisition
- model_training

## Observed properties

- superconducting transition temperature (Tc)

## Observed fields

- chemical formula
- crystal structure
- Tc
- space group
- lattice parameter

## Usage evidence

- P031 (Learning Superconductivity from Ordered and Disordered Material Structures): candidate_pool in constructing SuperCon3D dataset — Final constructed dataset containing 1,578 entries with both crystal structure and experimental Tc, used as the core dataset for all downstream modeling
- P031 (Learning Superconductivity from Ordered and Disordered Material Structures): training in training SODNet for Tc prediction — Training SODNet for Tc prediction on both ordered and disordered crystal structures
- P031 (Learning Superconductivity from Ordered and Disordered Material Structures): training in training DiffCSP-SC for inverse design — Training DiffCSP-SC for inverse design, using SuperCon3D as the target dataset for fine-tuning after pre-training

## Dataset evidence

- P031, PDF page 1, Abstract: "Hence, we present a new dataset for data-driven approaches, namely SuperCon3D, containing both 3D crystal structures and experimental superconducting transition temperature (Tc) for the first time."
- P031, PDF page 7, 5.1.1 SuperCon3D dataset.: "We extracted approximately 33,000 superconductors with their chemical formulas and corresponding critical temperatures from SuperCon. After removing duplicates and non-superconductors, we identified 11,949 superconducting materials. Additionally, over 200,000 ordered and disordered crystal structures were gathered from the ICSD database [3]. We then matched these 11,949 SuperCon entries with 208,425 ICSD entries based on chemical composition, space group and lattice parameter. Moreover, Tc values and structural data for hydrogen-enriched superconductors were collated from various literature sources. This process resulted in 1,578 superconductor data entries, each featuring both Tc and crystal structure."

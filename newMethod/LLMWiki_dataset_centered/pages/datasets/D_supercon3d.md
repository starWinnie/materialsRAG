# Dataset: SuperCon3D

- Dataset ID: `D_supercon3d`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- SuperCon3D

## Observed material scopes

- superconductors

## Observed research tasks

- designing high Tc superconductors

## Observed research stages

- data_acquisition
- model_training
- computational_validation

## Observed properties

- superconducting transition temperature (Tc)

## Observed fields

- 3D crystal structure
- experimental Tc

## Usage evidence

- P031 (Learning Superconductivity from Ordered and Disordered Material Structures): training in constructing SuperCon3D dataset — the constructed dataset used as input for model training
- P031 (Learning Superconductivity from Ordered and Disordered Material Structures): training in training SODNet — training SODNet for screening known structures
- P031 (Learning Superconductivity from Ordered and Disordered Material Structures): training in training DiffCSP-SC — training DiffCSP-SC for creating new structures
- P031 (Learning Superconductivity from Ordered and Disordered Material Structures): computational_validation in DFT verification of candidates — providing reference Tc values for DFT verification of generated candidates

## Dataset evidence

- P031, PDF page 1, Abstract: "Hence, we present a new dataset for data-driven approaches, namely SuperCon3D, containing both 3D crystal structures and experimental superconducting transition temperature (Tc) for the first time."
- P031, PDF page 2, Introduction: "Constructing a dataset that captures the structure-to-superconductivity relationship is essential for training AI models aimed at designing superconductors. Hence, we introduce SuperCon3D, a new dataset combining crystal structures and the critical temperature Tc from SuperCon and ICSD."
- P031, PDF page 7, 5.1.1 SuperCon3D dataset.: "We extracted approximately 33,000 superconductors with their chemical formulas and corresponding critical temperatures from SuperCon. After removing duplicates and non-superconductors, we identified 11,949 superconducting materials. Additionally, over 200,000 ordered and disordered crystal structures were gathered from the ICSD database [3]. We then matched these 11,949 SuperCon entries with 208,425 ICSD entries based on chemical composition, space group and lattice parameter. Moreover, Tc values and structural data for hydrogen-enriched superconductors were collated from various literature sources. This process resulted in 1,578 superconductor data entries, each featuring both Tc and crystal structure."

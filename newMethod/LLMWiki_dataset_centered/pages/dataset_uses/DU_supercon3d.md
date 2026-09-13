# Dataset Use: SuperCon3D

- DatasetUse ID: `DU_supercon3d`
- Dataset: SuperCon3D (`D_supercon3d`)
- Papers: P031
- Usage records: 4

## Usage roles

- training
- computational_validation

## Purposes

- the constructed dataset used as input for model training
- training SODNet for screening known structures
- training DiffCSP-SC for creating new structures
- providing reference Tc values for DFT verification of generated candidates

## Used fields

- 3D crystal structure
- experimental Tc

## Construction methods

- matching SuperCon entries with ICSD entries based on chemical composition, space group and lattice parameter; collating Tc and structural data for hydrogen-enriched superconductors from literature

## Filter conditions

- None stated

## Sample counts

- 1578

## Availability

- Dataset: public
- Recommendable: false

## Confidence

0.95

## Usage records

### UR_P031_01_supercon3d

- Paper: `P031` — Learning Superconductivity from Ordered and Disordered Material Structures
- Task: designing high Tc superconductors (`T_P031_01`)
- Stage: constructing SuperCon3D dataset (`data_acquisition`, `S_P031_01`)
- Usage role: training
- Purpose: the constructed dataset used as input for model training
- Used fields: 3D crystal structure, experimental Tc
- Filter conditions: Not stated
- Construction method: matching SuperCon entries with ICSD entries based on chemical composition, space group and lattice parameter; collating Tc and structural data for hydrogen-enriched superconductors from literature
- Sample count: 1578
- Confidence: 1.0

Evidence:
- P031, PDF page 7, 5.1.1 SuperCon3D dataset.: "This process resulted in 1,578 superconductor data entries, each featuring both Tc and crystal structure."

### UR_P031_02_supercon3d

- Paper: `P031` — Learning Superconductivity from Ordered and Disordered Material Structures
- Task: designing high Tc superconductors (`T_P031_01`)
- Stage: training SODNet (`model_training`, `S_P031_02`)
- Usage role: training
- Purpose: training SODNet for screening known structures
- Used fields: 3D crystal structure, experimental Tc
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P031, PDF page 1, Abstract: "Based on SuperCon3D, we propose two deep learning methods for designing high Tc superconductors. The first is SODNet, a novel equivariant graph attention model for screening known structures, which differs from existing models in incorporating both ordered and disordered geometric content."

### UR_P031_03_supercon3d

- Paper: `P031` — Learning Superconductivity from Ordered and Disordered Material Structures
- Task: designing high Tc superconductors (`T_P031_01`)
- Stage: training DiffCSP-SC (`model_training`, `S_P031_03`)
- Usage role: training
- Purpose: training DiffCSP-SC for creating new structures
- Used fields: 3D crystal structure, experimental Tc
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P031, PDF page 1, Abstract: "The second is a diffusion generative model DiffCSP-SC for creating new structures, which enables high Tc-targeted generation."

### UR_P031_06_supercon3d

- Paper: `P031` — Learning Superconductivity from Ordered and Disordered Material Structures
- Task: designing high Tc superconductors (`T_P031_01`)
- Stage: DFT verification of candidates (`computational_validation`, `S_P031_06`)
- Usage role: computational_validation
- Purpose: providing reference Tc values for DFT verification of generated candidates
- Used fields: experimental Tc
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 0.95

Evidence:
- P031, PDF page 10, 5.3.3 Candidate Superconductors.: "Subsequently, density-functional theory (DFT) were performed on selected candidates to verify their superconducting properties. Notably, Van Hove singularities (VHS) were observed in the electronic structures of Ba2CuCl2O2, Lu, and BaFe2Se2, as further detailed in Appendix E.5."

## Aggregated evidence

- , PDF page 7, 5.1.1 SuperCon3D dataset.: "This process resulted in 1,578 superconductor data entries, each featuring both Tc and crystal structure."
- , PDF page 1, Abstract: "Based on SuperCon3D, we propose two deep learning methods for designing high Tc superconductors. The first is SODNet, a novel equivariant graph attention model for screening known structures, which differs from existing models in incorporating both ordered and disordered geometric content."
- , PDF page 1, Abstract: "The second is a diffusion generative model DiffCSP-SC for creating new structures, which enables high Tc-targeted generation."
- , PDF page 10, 5.3.3 Candidate Superconductors.: "Subsequently, density-functional theory (DFT) were performed on selected candidates to verify their superconducting properties. Notably, Van Hove singularities (VHS) were observed in the electronic structures of Ba2CuCl2O2, Lu, and BaFe2Se2, as further detailed in Appendix E.5."

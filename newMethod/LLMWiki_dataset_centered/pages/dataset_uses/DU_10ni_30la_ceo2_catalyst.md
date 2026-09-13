# Dataset Use: 10Ni/30La-CeO2 catalyst

- DatasetUse ID: `DU_10ni_30la_ceo2_catalyst`
- Dataset: 10Ni/30La-CeO2 catalyst (`D_10ni_30la_ceo2_catalyst`)
- Papers: P040
- Usage records: 4

## Usage roles

- experimental_validation
- computational_validation
- screening
- benchmark

## Purposes

- In situ observation of particle-to-cluster transformation under H2 atmosphere and heating to 600 °C
- DFT and ML-MD simulations of interfacial atomic migration and adsorption energetics on NiOy/LaCeO2−x surface
- Comparative evaluation against 10Ni/CeO2 to identify La doping as critical enabler of reverse dispersion
- Catalytic performance testing and kinetic analysis for ammonia decomposition activity and stability metrics

## Used fields

- HAADF-STEM
- ETEM
- HRTEM
- adsorption energies
- migration pathways
- thermodynamic stability of Ni-O-La configurations
- XRD
- H2-TPR
- XPS
- FTIR
- Raman
- NH₃ conversion
- H₂ production rate
- stability over 240 h
- apparent activation energy

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- None stated

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P040_02_10ni_30la_ceo2_catalyst

- Paper: `P040` — Atomic-scale revelation of in situ reverse regulation from particles to clusters in the Ni/La-CeOx catalyst
- Task: reverse regulation from particles to clusters (`T_P040_01`)
- Stage: in situ observation of particle-to-cluster transformation (`experimental_validation`, `S_P040_02`)
- Usage role: experimental_validation
- Purpose: In situ observation of particle-to-cluster transformation under H2 atmosphere and heating to 600 °C
- Used fields: HAADF-STEM, ETEM, HRTEM
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P040, PDF page 2, Results: "By means of high-angle annular dark-field scanning transmission electronmicroscopy (HAADF-STEM) and in situ environmental transmission electron microscopy (ETEM), the structural evolution process of Ni particles transforming into Ni clusters in situ under a high-temperature and reducing atmosphere was clearly elucidated."
- P040, PDF page 2, Results: "In situ aberration-corrected ETEM was employed to characterize the 10Ni/30La-CeO2 catalyst. The nanoparticles gradually contracted when the temperature increased from room temperature to 450 °C under a H2 atmosphere... Then, the particles completely dispersed upon further increasing the temperature to 600 °C..."

### UR_P040_03_10ni_30la_ceo2_catalyst

- Paper: `P040` — Atomic-scale revelation of in situ reverse regulation from particles to clusters in the Ni/La-CeOx catalyst
- Task: reverse regulation from particles to clusters (`T_P040_01`)
- Stage: DFT and ML-MD simulations of interfacial atomic migration and adsorption energetics (`computational_validation`, `S_P040_03`)
- Usage role: computational_validation
- Purpose: DFT and ML-MD simulations of interfacial atomic migration and adsorption energetics on NiOy/LaCeO2−x surface
- Used fields: adsorption energies, migration pathways, thermodynamic stability of Ni-O-La configurations
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P040, PDF page 5: "Density Functional Theory (DFT) calculations revealed that the reactive Oads coordinated with either Ce or La atoms on the catalyst surface could establish strong MSI with Ni species, consequently promoting the redispersion of Ni nanoparticles."
- P040, PDF page 6: "Machine learning force field-based molecular dynamics on NiOy/CeO2−x and NiOy/LaCeO2−x at 800 K."

### UR_P040_04_10ni_30la_ceo2_catalyst

- Paper: `P040` — Atomic-scale revelation of in situ reverse regulation from particles to clusters in the Ni/La-CeOx catalyst
- Task: reverse regulation from particles to clusters (`T_P040_01`)
- Stage: comparative evaluation of La-doped vs. undoped support (`candidate_screening`, `S_P040_04`)
- Usage role: screening
- Purpose: Comparative evaluation against 10Ni/CeO2 to identify La doping as critical enabler of reverse dispersion
- Used fields: XRD, H2-TPR, XPS, FTIR, Raman
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P040, PDF page 3: "The markedly different evolution of 10Ni/CeO2 and 10Ni/30La-CeO2 under identical conditions clearly demonstrates that electron beam irradiation is not the primary cause of particle dispersion; rather, the reverse sintering is an intrinsic property of the catalyst."
- P040, PDF page 3: "Notably, the 10Ni/30La-CeO2 catalyst exhibited a significantly higher proportion of Niδ+ species (51.1%) compared to the 10Ni/CeO2 reference (30.6%)..."

### UR_P040_05_10ni_30la_ceo2_catalyst

- Paper: `P040` — Atomic-scale revelation of in situ reverse regulation from particles to clusters in the Ni/La-CeOx catalyst
- Task: reverse regulation from particles to clusters (`T_P040_01`)
- Stage: catalytic performance testing and kinetic analysis (`model_evaluation`, `S_P040_05`)
- Usage role: benchmark
- Purpose: Catalytic performance testing and kinetic analysis for ammonia decomposition activity and stability metrics
- Used fields: NH₃ conversion, H₂ production rate, stability over 240 h, apparent activation energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P040, PDF page 7, Catalytic performance and the catalytic role of La promoter.: "10Ni/30La-CeO2 with an actual Ni loading of only 7.3% (determined by ICP-MS, Table 1) exhibited a superior NH3 conversion of 61% at 500 °C (GHSV = 30,000 mL·gcat−1h−1)... achieving a H2 formation rate of 279.2 mmolH2·gNi−1·min−1 at 500 °C..."
- P040, PDF page 7, Catalytic performance and the catalytic role of La promoter.: "The 10Ni/30La-CeO2 catalyst exhibited remarkably superior cycling stability... and high-temperature stability... maintaining its performance consistently throughout the stability evaluation over 240 h."

## Aggregated evidence

- , PDF page 2, Results: "By means of high-angle annular dark-field scanning transmission electronmicroscopy (HAADF-STEM) and in situ environmental transmission electron microscopy (ETEM), the structural evolution process of Ni particles transforming into Ni clusters in situ under a high-temperature and reducing atmosphere was clearly elucidated."
- , PDF page 2, Results: "In situ aberration-corrected ETEM was employed to characterize the 10Ni/30La-CeO2 catalyst. The nanoparticles gradually contracted when the temperature increased from room temperature to 450 °C under a H2 atmosphere... Then, the particles completely dispersed upon further increasing the temperature to 600 °C..."
- , PDF page 5: "Density Functional Theory (DFT) calculations revealed that the reactive Oads coordinated with either Ce or La atoms on the catalyst surface could establish strong MSI with Ni species, consequently promoting the redispersion of Ni nanoparticles."
- , PDF page 6: "Machine learning force field-based molecular dynamics on NiOy/CeO2−x and NiOy/LaCeO2−x at 800 K."
- , PDF page 3: "The markedly different evolution of 10Ni/CeO2 and 10Ni/30La-CeO2 under identical conditions clearly demonstrates that electron beam irradiation is not the primary cause of particle dispersion; rather, the reverse sintering is an intrinsic property of the catalyst."
- , PDF page 3: "Notably, the 10Ni/30La-CeO2 catalyst exhibited a significantly higher proportion of Niδ+ species (51.1%) compared to the 10Ni/CeO2 reference (30.6%)..."
- , PDF page 7, Catalytic performance and the catalytic role of La promoter.: "10Ni/30La-CeO2 with an actual Ni loading of only 7.3% (determined by ICP-MS, Table 1) exhibited a superior NH3 conversion of 61% at 500 °C (GHSV = 30,000 mL·gcat−1h−1)... achieving a H2 formation rate of 279.2 mmolH2·gNi−1·min−1 at 500 °C..."
- , PDF page 7, Catalytic performance and the catalytic role of La promoter.: "The 10Ni/30La-CeO2 catalyst exhibited remarkably superior cycling stability... and high-temperature stability... maintaining its performance consistently throughout the stability evaluation over 240 h."

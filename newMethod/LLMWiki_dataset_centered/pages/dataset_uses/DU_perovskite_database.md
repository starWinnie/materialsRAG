# Dataset Use: Perovskite Database

- DatasetUse ID: `DU_perovskite_database`
- Dataset: Perovskite Database (`D_perovskite_database`)
- Papers: P042
- Usage records: 5

## Usage roles

- source
- benchmark
- computational_validation

## Purposes

- Manual extraction of device data from peer-reviewed literature
- Consistent formatting and validation of extracted data
- Development of interactive web-based analysis and visualization tools
- Demonstration and validation of analytical insights using the database
- Implementation of FAIR-compliant infrastructure and open-source release

## Used fields

- reference data
- cell-related data
- device stack
- synthesis related data
- performance metrics
- power conversion efficiency (PCE)
- open-circuit voltage (Voc)
- bandgap (Eg)
- stability (T80)
- scalability (cell area)

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 42400

## Availability

- Dataset: public
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P042_01_perovskite_database

- Paper: `P042` — An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles
- Task: Creation of an open-access, FAIR-compliant database and analysis tool for perovskite solar cell device data (`T_P042_01`)
- Stage: Manual extraction of device data from peer-reviewed literature (`data_acquisition`, `S_P042_01`)
- Usage role: source
- Purpose: Manual extraction of device data from peer-reviewed literature
- Used fields: reference data, cell-related data, device stack, synthesis related data, performance metrics
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 42400
- Confidence: 1.0

Evidence:
- P042, PDF page 2, Data: "We have manually gone through every paper found in the Web of Science with the search phrase ‘perovskite solar’ up to the end of February 2020 (that is, over 15,000 papers). In total, we have manually extracted data for over 42,400 devices."
- P042, PDF page 7, Methods: "The search phrase ‘perovskite solar’ in the Web of Science generated over 15,000 entries by the end of February 2020. Not all of those publications relate to metal-halide perovskites and photovoltaic applications, but most do. Similarly, a few relevant papers will be missed in this search. From here, our collective team has manually gone through every paper and extracted data for all the described devices."

### UR_P042_02_perovskite_database

- Paper: `P042` — An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles
- Task: Creation of an open-access, FAIR-compliant database and analysis tool for perovskite solar cell device data (`T_P042_01`)
- Stage: Consistent formatting and validation of extracted data (`data_preparation`, `S_P042_02`)
- Usage role: source
- Purpose: Consistent formatting and validation of extracted data
- Used fields: reference data, cell-related data, device stack, synthesis related data, performance metrics
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P042, PDF page 3, Data: "Once extracted, the data have been consistently formatted according to the instruction in the supporting documentation and is now freely available in the Perovskite Database."
- P042, PDF page 7, Methods: "To reduce the errors, we went through the extracted data to check for errors, misunderstandings, confusing entries and inconsistent formatting."

### UR_P042_03_perovskite_database

- Paper: `P042` — An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles
- Task: Creation of an open-access, FAIR-compliant database and analysis tool for perovskite solar cell device data (`T_P042_01`)
- Stage: Development of interactive web-based analysis and visualization tools (`candidate_generation`, `S_P042_03`)
- Usage role: source
- Purpose: Development of interactive web-based analysis and visualization tools
- Used fields: reference data, cell-related data, device stack, synthesis related data, performance metrics
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P042, PDF page 2, Data: "Apart from making all historical data accessible and providing means to upload new experimental data, interactive graphical data visualization tools have been implemented that enable simple and interactive exploration, analysis and filtering (Fig. 1)."
- P042, PDF page 3, Data: "To increase the usability of the data, we have developed interactive tools for simple exploration, analysis, filtering and visualization that can be used without programming knowledge."

### UR_P042_04_perovskite_database

- Paper: `P042` — An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles
- Task: Creation of an open-access, FAIR-compliant database and analysis tool for perovskite solar cell device data (`T_P042_01`)
- Stage: Demonstration and validation of analytical insights using the database (`candidate_screening`, `S_P042_04`)
- Usage role: benchmark
- Purpose: Demonstration and validation of analytical insights using the database
- Used fields: power conversion efficiency (PCE), open-circuit voltage (Voc), bandgap (Eg), stability (T80), scalability (cell area)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P042, PDF page 3, Data: "What follows is a small selection of analyses, visualizations and insights made possible by the Perovskite Database and the associated toolbox."
- P042, PDF page 7, Conclusions: "We demonstrate the capabilities of the database and the associated tools by giving a few examples of insights that can be gleaned from the analysis of this large dataset in terms of, for example, record development, tandem integration, stability and scalability."

### UR_P042_05_perovskite_database

- Paper: `P042` — An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles
- Task: Creation of an open-access, FAIR-compliant database and analysis tool for perovskite solar cell device data (`T_P042_01`)
- Stage: Implementation of FAIR-compliant infrastructure and open-source release (`computational_validation`, `S_P042_05`)
- Usage role: computational_validation
- Purpose: Implementation of FAIR-compliant infrastructure and open-source release
- Used fields: reference data, cell-related data, device stack, synthesis related data, performance metrics
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P042, PDF page 1: "The database, graphics and analysis tools are made available to the community and will continue to evolve as an open-source initiative."
- P042, PDF page 3, Data: "All the resources are found at the project website (www.perovskitedatabase.com), where they will be updated and maintained for the foreseeable future."
- P042, PDF page 3, Data: "The code base for the project is written in Python and is available at GitHub (https://github.com/Jesperkemist/perovskitedatabase), and everyone is invited to contribute and expand the scope of the project."

## Aggregated evidence

- , PDF page 2, Data: "We have manually gone through every paper found in the Web of Science with the search phrase ‘perovskite solar’ up to the end of February 2020 (that is, over 15,000 papers). In total, we have manually extracted data for over 42,400 devices."
- , PDF page 7, Methods: "The search phrase ‘perovskite solar’ in the Web of Science generated over 15,000 entries by the end of February 2020. Not all of those publications relate to metal-halide perovskites and photovoltaic applications, but most do. Similarly, a few relevant papers will be missed in this search. From here, our collective team has manually gone through every paper and extracted data for all the described devices."
- , PDF page 3, Data: "Once extracted, the data have been consistently formatted according to the instruction in the supporting documentation and is now freely available in the Perovskite Database."
- , PDF page 7, Methods: "To reduce the errors, we went through the extracted data to check for errors, misunderstandings, confusing entries and inconsistent formatting."
- , PDF page 2, Data: "Apart from making all historical data accessible and providing means to upload new experimental data, interactive graphical data visualization tools have been implemented that enable simple and interactive exploration, analysis and filtering (Fig. 1)."
- , PDF page 3, Data: "To increase the usability of the data, we have developed interactive tools for simple exploration, analysis, filtering and visualization that can be used without programming knowledge."
- , PDF page 3, Data: "What follows is a small selection of analyses, visualizations and insights made possible by the Perovskite Database and the associated toolbox."
- , PDF page 7, Conclusions: "We demonstrate the capabilities of the database and the associated tools by giving a few examples of insights that can be gleaned from the analysis of this large dataset in terms of, for example, record development, tandem integration, stability and scalability."
- , PDF page 1: "The database, graphics and analysis tools are made available to the community and will continue to evolve as an open-source initiative."
- , PDF page 3, Data: "All the resources are found at the project website (www.perovskitedatabase.com), where they will be updated and maintained for the foreseeable future."
- , PDF page 3, Data: "The code base for the project is written in Python and is available at GitHub (https://github.com/Jesperkemist/perovskitedatabase), and everyone is invited to contribute and expand the scope of the project."

# Requirements

## Functional Requirements
Functional Requirements specify what the system must accomplish in terms of behavior and calculation to meet the UBA standard

### Abstract Workflow 

![UML Diagram](./AQI_UML_diagram.drawio.png)


**Workflow Description:**

1. **Data Loading** Read local CSV files from the `/data/raw/` directory.
2. **Data Preprocessing** Clean data, handle missing values, and parse timestamps
3. **Calculate Individual Pollutant Index** Map concentrations for all 5 pollutants to the 5-level index using `src/aqi_calculator.py` and `src/aqi_thresholds.py`
4. **Compute Final AQI Score** Apply the "Maximum Operator Rule" to get the single worst index
5. **Generate Figures and Tables** Save the final time series and create visualizations

---

## Non-Functional Requirements
1. **Maintainability**: Organized folder structure, consistent naming conventions, and functions support long term maintenance.
2. **Portability**: Notebook based interface enables reuse across environments with standard Python/Jupyter setup.
3. **Extensibility**:  Easy to scale to new stations and time ranges through modular functions.
4. **Testability**: Comprehensive pytest suite ensures reliability and correctness.
5. **Documentation & Licensing**:  Includes `LICENSE`, `CITATION.cff`, `CONTRIBUTING.md`, and `CONDUCT.md` for open source compliance and transparency.

---

## Component Description Table
| **Abstract Workflow Node (Operation)** | **Input(s)** | **Output(s)** | **Implementation** |
|---------------------------------------|---------------|----------------|--------------------|
| **Load Raw Data** | File paths to CSV | Raw pollutant dataFrame | notebook code – uses `pandas.read_csv()` to load local static files from `/data/raw/` |
| **Data Preprocessing** | Raw pollutant dataframe | Cleaned Concentration Time Series | notebook code uses pandas to handle missing values ('-'), convert types, and parse timestamps|
| **Calculate IPIs** | Cleaned Concentration Time Series | Individual Pollutant Index Time Series |  The function `src/aqi_calculator.py:classify_pollutant()` using UBA breakpoints from `src/aqi_thresholds.py`|
| **Compute Final AQI Score** | Individual Pollutant Index Time Series | Final AQI Score & Category | The function `src/aqi_calculator.py:compute_row_aqi()` applying Maximum Operator Rule|
| **Generate Figures and Tables** | Final AQI Score & Category | DataFrame comparisons, insights | Notebook code – compares computed vs official AQI, generates analysis |
| **Testing** | Source code | Test results | `tests/test_aqi_calculator.py` – pytest suite with equivalence classes, boundaries, regression tests |

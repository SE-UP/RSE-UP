# German Air Quality Index Analyzer

A Python based tool to load German air quality data, compute Air Quality Index (AQI) metrics using the German AQI methodology, and produce figures and tables.

# Overview

This project aims to develop a software tool to analyze the German National AQI using the data provided by the [Federal Environment Agency (UBA)](https://www.umweltbundesamt.de/en/calculation-base-air-quality-index) It is designed as a case study in applying Research Software Engineering (RSE) principles to an environmental challenge.
The project follows the methodology developed and managed by the UBA, which classifies air quality on a five level scale (1–5), that reflects four atmospheric pollutant concentrations into a clear and interpretable risk levels. 
This project follows the methodology and principles taught in the [Research Software Engineering at the University of Potsdam (RSE-UP)](https://se-up.github.io/RSE-UP/) course.  
The lecture materials are largely based on *Irving et al. (2021), Research Software Engineering with Python* — available at [third-bit.com/py-rse](https://third-bit.com/py-rse/).


# Project Structure
```
german-air-quality-index-analyzer/
├── data/
│ ├── processed/
│ └── raw/
│   ├── air-quality_Berlin-Grunewald_october.csv
│   ├── air-quality_Bremen-Hasenbueren.csv
│   ├── air-quality_DEBE032_Berlin-Grunewald-september.csv
│   └── Grunewald_august.csv  # UBA datasets for various locations and periods
│
├── docs/ # documentation and meta files
│ ├── AQI_UML_diagram.drawio.png
│ └── requirements.md
│
├── notebooks/
│ └── computational_narrative.ipynb
├── results/
│
├── src/
│ ├── __init__.py
│ ├── aqi_calculator.py
│ └── aqi_thresholds.py
├── tests/
│ └── test_aqi_calculator.py
│
├── .gitignore
├── CITATION.cff
├── LICENSE
├── CONDUCT.md
├── CONTRIBUTING.md
├── pyproject.toml
├── requirements.txt
└── README.md
```

# Installation

Follow these steps to set up the project locally.

## 1. Clone the repository

Clone this repository from the University of Potsdam GitLab (Git.UP):

```bash
git clone https://gitup.uni-potsdam.de/mohammedah/german-air-quality-index-analyzer.git
cd german-air-quality-index-analyzer
```
## 2. Create a virtual environment (optional)

```
python3 -m venv .venv
source .venv/bin/activate        # On macOS/Linux
# OR
.\.venv\Scripts\activate         # On Windows
```
## 3. Install dependencies
```
pip install -r requirements.txt
```

## 4. Code quality tools

Linting and formatting are configured in `pyproject.toml`. Run them with:

```bash
black src/ tests/          # auto-format
isort src/ tests/          # sort imports
flake8 src/ tests/         # style checks
mypy src/                  # type checking
```

# Usage

## Computational Narrative (Full Analysis)
Run the computational narrative in `notebooks/computational_narrative.ipynb` to:
- Load and preprocess UBA air quality data
- Compute German AQI using official methodology
- Compare computed results with official UBA values
- Generate analysis and visualizations

## AQI Calculator Module (Quick Demo)
Run the AQI calculator module directly to see a demonstration of the core functionality:

```bash
python -m src.aqi_calculator
```

This will display:
- Example pollutant concentrations for all 5 pollutants
- Individual pollutant classifications
- Overall AQI calculation using the maximum operator rule
- Complete AQI category reference

# Data
The air quality index data is sourced from the German Environment Agency [(Umweltbundesamt)](https://www.umweltbundesamt.de/en/calculation-base-air-quality-index).

**Source:** Umweltbundesamt mit Daten der Messnetze der Länder und des Bundes (German Environment Agency with data from the monitoring networks of the federal states and the federal government).

**Download:** Raw CSV files can be downloaded from the [UBA Air Quality Data Portal](https://luftdaten.umweltbundesamt.de). Select a monitoring station, choose a time range, and export as CSV with a semicolon (`;`) delimiter.

**License:** The data is provided under the Data license Germany – attribution – version 2.0 (dl-de/by-2-0).

# Testing

All core logic is covered by a pytest suite in [tests/test_aqi_calculator.py](tests/test_aqi_calculator.py), including equivalence class, boundary value, and metamorphic tests. Run with:

```bash
pytest
```

# CI/CD

This project uses a [Jenkins](https://www.jenkins.io/) pipeline for continuous integration.
On every push to any branch, Jenkins automatically runs linting (flake8, black, isort, mypy)
and the full test suite with coverage reporting. Results are reported back to GitLab as commit statuses.

# Contribution
We welcome contributions!  
Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for how to get started.

# License
This project is licensed under the [MIT License](./LICENSE).

# Citation
If you use this project in your research or publication, please cite it appropriately. See the full citation details in the [CITATION.cff](./CITATION.cff) file.

# Code of Conduct
This project adheres to the [Contributor Covenant Code of Conduct](./CONDUCT.md). All contributors are expected to uphold these guidelines in all project spaces.

# Authors and Acknowledgment

Software Engineering Team





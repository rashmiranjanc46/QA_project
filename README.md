# Automated QA Framework for Microgrid Security APIs

## Project Overview
This project bridges advanced power system analytics with modern software engineering practices. It provides a REST API web service designed to process sensor data from microgrid Load Frequency Control (LFC) systems and detect False Data Injection (FDI) attacks. 

More importantly, this repository demonstrates a robust Quality Engineering (QE) architecture, implementing automated testing suites and a continuous integration pipeline to validate the underlying logic.

## Technical Stack
* **Language:** Python
* **Web Services:** FastAPI, Uvicorn
* **Test Automation:** Pytest, HTTPX
* **DevOps / CI:** GitHub Actions
* **Data Validation:** Pydantic

## Quality Engineering Methodologies Implemented
To ensure the integrity of the anomaly detection system, the following QA processes were automated:
1. **Positive/Functional Testing:** Verifying the API correctly processes nominal frequency deviation and tie-line power data.
2. **Boundary Value Analysis (BVA):** Parameterized testing at the absolute mathematical thresholds of the detection logic (e.g., exactly `0.05` Hz and `0.051` Hz) to validate edge-case stability.
3. **Negative Testing:** Simulating payload corruption and invalid data types to verify the system rejects unprocessable entities (HTTP 422) without crashing the server.

## Continuous Integration (DevOps)
This project utilizes a GitHub Actions CI pipeline. Upon every code push, an automated runner provisions an Ubuntu environment, configures the Python engine, installs dependencies, and executes the complete `pytest` automation suite to ensure no code regressions are introduced into the main branch.
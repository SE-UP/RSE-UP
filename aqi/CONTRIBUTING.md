# Contributing to This Project

Thank you for your interest in contributing to this Research Software Engineering (RSE) project! 
We are implementing the official Air Quality Index calculation for Germany using data from from [Federal Environment Agency (UBA)](https://www.umweltbundesamt.de/en/calculation-base-air-quality-index).

This guide will help you get started contributing code, data, documentation, or ideas.

---

## Before You Start

Please make sure to read our:

- [Code of Conduct](./CONDUCT.md)
- [README.md](./README.md) for project context

---

## How to Contribute

### Step 1: Fork This Repository

1. Click the **Fork** button in the top right of this repo’s GitUP/GitHub page.
2. Clone your fork locally:

    ```bash
    git clone https://gitup.uni-potsdam.de/mohammedah/german-air-quality-index-analyzer.git
    cd german-air-quality-index-analyzer
    ```

---

### Step 2: Set Up Your Environment

1. Install required tools (e.g., Python, Jupyter Notebook).
2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

### Step 3: Make Your Changes

You can contribute by:

- Fixing typos or bugs in notebooks or scripts
- Improving or adding data cleaning processes
- Adding visualizations or statistical analysis
- Writing new features or functions
- Enhancing documentation or README

When you're ready to commit:

```bash
git add your-changed-files
git commit -m "A clear and concise commit message"
```
Make sure your commits are focused and easy to understand.

---

### Step 4: Quality Assurance and Testing

Testing is mandatory for RSE projects. Your contribution must be validated against the project's quality standards.

 **1- Code Style:** All Python code must conform to the PEP-8 standard. Use a linter (like pycodestyle or Black) to verify compliance.

 **2- Run Tests:** Execute the unit and integration test suites using pytest. Your changes must not introduce any failing tests.
 ```bash
 # Run all unit and integration tests
 pytest
 ```
 **3- Scientific Robustness:** If you modify the core AQI calculation logic, ensure coverage of advanced scientific checks, including the Metamorphic Tests designed to validate the monotonicity of the Critical Pollutant Principle ($\max$ rule).

---



### Step 5: Push and Create a Pull Request (PR)

1. Push your changes to your forked repository:

    ```bash
    git push origin your-branch-name
    ```

2. Go to the original repository on GitUP/GitHub and open a **Pull Request**.

3. In your PR description, include:

- What you changed and why  
- Any screenshots or examples (e.g., chart outputs)  
- Reference any related issues (e.g., `Closes #5`)  

A team member will review your PR and may request changes.

---

### Reporting Bugs or Suggesting Features

Use the issue tracker to discuss and document planned work:

 - Bug Report: Use a clear, descriptive title. Provide detailed steps to reproduce the bug, including the version of the software, operating system, and data used.  
 - Feature Suggestion: Clearly describe the proposed enhancement and the benefit it provides to the project.  
 - Labeling: Apply appropriate labels (e.g., bug, enhancement, question) to help with triage and prioritization.  
---

### Adding Data

- Place raw data in the `data/` directory.
- Document the source of the data in the `README.md` or a separate `metadata.md` file.
- Do **not** upload very large datasets (>100 MB) directly; link them externally or use [Git LFS](https://git-lfs.com/) if needed.

---

### License and Code of Conduct

- This project uses the [MIT License](./LICENSE)
- All contributors must follow our [Code of Conduct](./CONDUCT.md)


Thank You!

We appreciate your interest in improving this project!
Whether you're fixing a bug, adding new data, or improving documentation, your contributions are welcome and valued.

Feel free to open an issue if you’re not sure where to start — we’d love to help!
# README Files

In software projects, it is common to include a file named `README.md` in the root directory. 
This file is often the first thing a person encounters when visiting your repository, 
making it a crucial entry point for users and potential contributors. 
The README serves as a guide to help others understand the purpose of your open-source project and how to get started with it.

A well-crafted README provides essential information and instructions, such as installation steps, usage examples, and contribution guidelines. 
To be effective, it should be concise, clearly organized, and easy to read, 
ensuring that visitors can quickly grasp what your project is about and how they can participate.

## What to Include in a README file?

There are various recommendations on what to include in a README file, with many stemming from the open-source software community. 
These guidelines help ensure clarity, usability, and accessibility for a broad range of users and contributors.

In addition to general best practices, specific advice exists for research software. 
Notable examples include the [“README Best Practices” from Tilburg Science Hub](https://tilburgsciencehub.com/topics/collaborate-share/share-your-work/content-creation/readme-best-practices/) 
and [Cornell Data Services’ guide on “Writing READMEs for Research Code & Software.”](https://data.research.cornell.edu/data-management/sharing/writing-readmes-for-research-code-software/)
Both resources provide valuable insights tailored to the academic and research context.

In the following we combine Tilburg’s and Cornell’s recommendations to provide minimal and extended templates for research software README files.

Note that the templates provided should be viewed as guidance rather than strict rules. 
They are meant to offer structure and suggestions, but they are not set in stone. 
If certain components are not relevant to a particular project, they can simply be omitted without issue. 

For projects with very detailed or extensive content, it's perfectly acceptable to place that information in a separate file. 
In such cases, a brief description along with a link to the external file can be included in the README to keep it clear and concise.

## Minimal Template

```
# Project Title

## Overview
Briefly describe the purpose of the project and what it does. Mention the research question or objective.

## Getting Started
Instructions to set up the project locally:

- Prerequisites
- Installation steps

## Usage
Short example of how to run the software or script.

## Data
Brief description of required input/output data:

- Data format(s)
- Links to datasets or how to obtain them

## License
Specify the license (e.g., MIT, GPL).

## Citation
How to cite this software or related publication.

## Contact
Who to contact for questions or collaboration.
```

## Extended Template

```
# Project Title
Provide the title, version, and a one-sentence description of the project.

## 1. Overview
Provide detailed description of the project, and include (as applicable):

- Purpose of the software
- Research context and goals
- Notable features and purpose 
- Associated publication(s) (if any)
- Date of creation of the project  

## 2. Table of Contents
[Optional, but useful for longer READMEs]

## 3. Project Structure
Provide a brief explanation of folders/files, and include (as applicable):

- List of relevant files (or folders) that make up the project  
- Format of files that comprise the project  
- Size of total set of files for the project

## 4. Installation
Provide step-by-step instructions on how to install the project on a user's machine. 

### Prerequisites
- Python version or other environment details
- Required packages/libraries

### Instructions
Step-by-step installation guide (e.g., using `pip`, `conda`, or Docker).

## 5. Usage
Provide instructions on how to use the code. This might include screenshots or code examples (as applicable):

- Screenshots of functionality
- List of useful notebooks and what they demonstrate
- Example commands  
- Code examples  
- Running tests (if applicable)

## 6. Data
Provide details about the data required to run the software, and include (as applicable): 

- Source of datasets used or generated
- File formats, structure, and expected location
- Any preprocessing steps required

## 7. Reproducibility
Describe the necessary steps to reproduce your results (e.g., random seeds, configs).
If applicable, include the environment setup (include environment.yml, requirements.txt, or Dockerfile). 

## 8. Contribution
Describe how others can contribute to your porject. 
Link to issues or discussion forum (if applicable)

## 9. License
Include the license type and a short description or link to full license.

## 10. Citation
Include a preferred citation. 

## 11. Contact
Provide at least two contacts; repeat block for additional contributors as needed

- Name  
- Role (e.g., principal investigator, programmer, developer, maintainer, copyright owner)
- ORCID
- Institution
- Email

## 12. Acknowledgments
Acknowledge support for the project (as applicable): 

- (external) contributors 
- funding sources 
- publications that cite or use the project

```

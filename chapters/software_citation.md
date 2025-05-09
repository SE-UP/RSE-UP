#  Software Citation and FAIR

In this chapter we will explore software citation and the FAIR principles for research software including a pragmatic approach to FAIR.

## Software Publication and Citation
For decades, publishing peer-reviewed papers has been the cornerstone of scientific progress. Papers serve as crucial building blocks, allowing researchers to share findings, build upon existing knowledge, and receive credit for their work. However, the research ecosystem extends far beyond the written word. Data, code, and software play equally pivotal roles, yet their publication and citation remain significantly less common. This creates a gap that hinders transparency, reproducibility, and ultimately, scientific advancement.

#### A Broader Landscape:

Just as papers deserve publication and citation, so do other research outputs. Embracing this shift offers several benefits, aligned with key software citation principles:

**Importance and Credit & Attribution**: Sharing software alongside papers enhances transparency and empowers Research Software Engineers (RSEs). Formal citation practices give RSEs rightful credit for their contributions, adhering to the "Importance" and "Credit & Attribution" principles.

**Transparency and Unique Identification**: Making software openly available with persistent unique identifiers allows others to readily understand the "how" of research and identify the specific software version used ("Specificity" principle).

**Reproducibility and Persistence**: Openly available software enables others to run the same analyses, ensuring replicability and adherence to the "Persistence" principle.

**Collaboration and Accessibility**: Shared software fosters collaboration by offering reusable tools and codebases. This reduces duplication of effort, promotes community-driven development, and ensures the long-term sustainability of valuable research tools, fulfilling the "Accessibility" principle.


#### Making the Shift with Key Principles in Mind:

Several initiatives promote software publication and citation, aligned with these core principles:

- **Dedicated repositories**: Platforms like Zenodo and Software Heritage provide persistent, citable archives for research software, upholding the "Persistence" principle.

- **Citation guidelines**: Organizations like FORCE11 offer clear guidelines for formatting software citations in reference lists, ensuring "Specificity" and clarity.

- **Incentives and mandates**: Funding agencies and journals increasingly encourage or even mandate software publication as part of research outputs, promoting the overall importance of software.

By embracing these developments and adhering to these key principles, a research environment where software is valued, shared, and cited as readily as papers can be created. This shift will ultimately lead to more robust, transparent, and collaborative scientific progress, benefiting both researchers and society as a whole.

#### What could you do? 

- Advocate for software publication and citation within your research community and institutions.

- Utilize resources like the Zenodo guide for researchers to simplify software publication.

- Encourage colleagues to use dedicated repositories for long-term accessibility.

- Support the development of robust software citation metrics to properly acknowledge RSE contributions.

### How to Cite software?

Giving credit where credit is due applies to software just as much as any other intellectual creation. However, software citation can be tricky due to its unique nature. This guide explores how to identify the relevant metadata needed for proper software citation, highlighting resources like the Citation File Format (CFF) to make the process smoother.

#### Identifying the Relevant Metadata:
The ideal scenario is for the software project itself to clearly provide essential metadata for citation. This information typically includes:

- **Software name and version**: This seems obvious, but specifying the exact version ensures clarity and reproducibility.

- **Authors or developers**: Identify individuals or teams responsible for the software's creation.

- **Publication date or release date**: Pinpoint the initial release or significant update dates.

- **URL or access information**: Include links to official websites, repositories, or download locations.

- **DOI (Digital Object Identifier)**: If available, a DOI offers a persistent identifier for the software.

- **License information**: Specify the terms under which the software is distributed for proper ethical and legal attribution.

Unfortunately, not all software projects provide such detailed information. In such cases, consider these next steps:

- Consult the software website or documentation: Documentation often includes information about creators, release dates, and access details.

- **Search for publications** : Explore research papers or other publications related to the software's development. They often cite the software itself and might provide valuable metadata.

- Engage with the community forums or mailing lists: Reach out to the software's developer community for specific guidance on how to cite their work.

#### Enter the Citation File Format (CFF): 
The Citation File Format (CFF) offers a standardized way to store and share software citation metadata. 

Imagine it as a dedicated passport for your software, holding all the key information in a machine-readable format. Benefits of using CFF include:

- **Clarity and accuracy**: CFF ensures consistent and complete citation information, minimizing errors and ambiguity.
Tool support: Tools like cffinit help automatically generate CFF files from existing project data, streamlining the process.

- **Platform integration**: CFF can be integrated with platforms like Zenodo and GitHub, facilitating discovery and access to the software and its citation information.

- **Community adoption**: With over 16,000 CFF files already existing on GitHub, the format is gaining traction in the software development community.

Not all software projects utilize CFF yet. However, adopting this format demonstrates good scientific practice and encourages others to do the same, ultimately benefitting the entire research ecosystem.

In conclusion, citing software effectively requires identifying the relevant metadata, and resources like CFF make the process more efficient and standardized. 

### How to Publish Software

While making your software publicly available on platforms like GitHub is crucial for collaboration and access, it doesn't qualify as a formal "publication" in the academic sphere. To gain recognition and establish a proper citation record for your software, you need to follow specific strategies.

Here's how to effectively publish your software and ensure its academic merit:

#### 1. Publication Repositories:

- **Zenodo.org**: This open-access repository for research outputs allows you to upload your software along with associated data, documentation, and version control information. Zenodo assigns persistent identifiers (DOIs) for easy citation and tracking.

- **Figshare**: Another open-access platform, Figshare accepts various research artifacts, including software, and provides DOIs for citation. Similar to Zenodo, it offers version control and detailed metadata options.

#### 2. Software Journals:

- **Journal of Open Source Software (JOSS)**: A peer-reviewed, open-access journal dedicated to scientific software. Publication in JOSS involves a thorough review process ensuring software quality, reproducibility, and documentation clarity.

- **Journal of Research on Software (JORS)**: Similar to JOSS, JORS is a peer-reviewed open-access journal for software publications. It focuses on research software with significant contributions to scientific advancement.

- **Other options**: Explore discipline-specific software journals relevant to your field. Many engineering and computational sciences journals have dedicated software sections accepting peer-reviewed publications.

#### 3. "Publication" as a (Tools) Paper:

Consider writing a dedicated "tools paper" describing your software's development, methodology, functionalities, and impact. Submit this paper to relevant journals in your field, highlighting the software's contribution to your research area.

Ensure the paper clearly distinguishes itself from a user manual or technical documentation by focusing on the scientific significance and broader implications of your software.

#### 4. "Publication" in the Methods Section:

If your software is instrumental to your research findings, embed a detailed description of its functionality and development within the Methods section of your primary research paper.

Provide clear instructions on accessing and using the software, alongside a link to the publicly available code repository.

Additional considerations:

**Open Source Licensing**: Consider releasing your software under an open-source license like MIT or GPL to encourage contribution and wider adoption.
Version Control: Use a version control system like Git to track changes and ensure different versions are properly cited.

**Community Engagement**: Actively engage with users and developers on forums and platforms like GitHub to improve your software and foster a user community.
By following these strategies, you can effectively publish your software and gain the recognition it deserves within the academic community. Remember, formal publication goes beyond code availability and emphasizes transparency, reproducibility, and scientific contribution.

## FAIR Principles for Research Software (FAIR4RS)

In the age of information overload, ensuring the quality and usefulness of data is paramount. The FAIR principles offer a framework for managing data effectively, promoting its findability, accessibility, interoperability, and reusability. {cite:p}`wilkinson2016fair`  

```{figure} ../figures/fair/fair.png
:name: fair_princeples

FAIR 
```

- **Findability**: Think of data as hidden treasures. They need clear labels, descriptions, and identifiers (like unique file names) so people and machines can easily "discover" them. This means having rich metadata - information about the data itself, its format, context, and creation - that's searchable and discoverable through online repositories and catalogues.

- **Accessibility**: Once found, the treasure chest needs to be unlocked. Data should be readily accessible to authorized users. This requires clear access procedures, understandable licensing terms, and appropriate authentication processes. Consider factors like cost, technological barriers, and legal restrictions when defining accessibility.

- **Interoperability**: Imagine building with Lego bricks from different sets. Data interoperability ensures seamless integration with other datasets and analysis tools, regardless of format or origin. This requires using standardized vocabularies, data structures, and communication protocols. Think of it as creating a common language for different datasets to "talk" to each other.

-**Reusability**: Data should be more than just a one-time treasure trove. By having well-described metadata and clear documentation, data becomes reusable for future research, analysis, or even creative projects. This includes providing information about the data's limitations, provenance, and any modifications made. Reusability encourages collaboration, innovation, and maximizes the value of data beyond its initial purpose.

**_The FAIR principles are not just guidelines; they're essential for responsible data stewardship_**. By adhering to them, organizations, researchers, and individuals can unlock the true potential of their data, fostering research advancement, collaboration, and ultimately, knowledge creation.

Additional considerations:

- **Context is key** : The FAIR principles need to be applied within the specific context of the data and its intended use.

- **Community standards**: Existing community standards and best practices should be leveraged when implementing FAIR principles.

- **Technology can help**: Many tools and technologies exist to facilitate FAIR data management, from repositories to metadata creation platforms.

- **It's an ongoing process**: Implementing and maintaining FAIR data practices is an iterative process that requires continuous attention and collaboration.

### Digital Objects
According to the European Commision: 

> Central to the realization of FAIR are FAIR Digital Objects, which may represent data, software or other research resources.

But: How do the FAIR Principles relate to software? 

There is a mismatch between the broad intentions of the 4 foundational FAIR principles and how the 15 FAIR Guiding Principles are communicated and perceived.

It is also Important to note that **Software is (not) Data**

```{figure} ../figures/fair/fair_digital_objects.png
:name: fair_digital_objects
Fair Digital Objects
```

### FAIR not equal FOSS

Both FAIR principles and Open Source software (FOSS) aim for greater transparency, accessibility, and collaboration. However, they differ in their specific focus and requirements.

#### Similarities:

- **Transparency**: Both promote openness and understanding of underlying systems. FAIR encourages clear metadata and documentation, while FOSS provides public access to code.

- **Accessibility**: Both aim to make data or code readily available to users. FAIR advocates for accessible licensing and clear user guides, while FOSS utilizes open licenses for free access and modification.

- **Collaboration**: Both encourage community involvement and improvement. FAIR facilitates data reuse and integration, while FOSS enables collaborative development and modification of code.

#### Differences:

- **Open Data not Mandatory for FAIR**: While FAIR encourages open access to data, it acknowledges limitations due to privacy, security, and ethical concerns. In contrast, FOSS requires the source code to be publicly available.

- **Specificity**: FAIR focuses on data management for findability, accessibility, interoperability, and reusability. FOSS focuses on the code itself, with its specific licensing and community development practices.

**_Examples_**:

- **Patient health data**: Sharing such data openly could violate privacy. FAIR principles can still be applied by providing detailed metadata and access controls for authorized users.

- **Research software**: Openly sharing the code allows others to verify, improve, and build upon it. This aligns with both FAIR and FOSS principles.

**_The Case for Open Research Software_**:

While open data in certain fields might pose challenges, open research software aligns well with both FAIR and FOSS principles. Sharing methods and code improves transparency, reproducibility, and collaboration in research.


#### Summary

FAIR and FOSS are not equivalent, but they have significant overlap in promoting transparency, accessibility, and collaboration. While FAIR focuses on data management practices, FOSS focuses on open access to code. Both play crucial roles in fostering knowledge creation and innovation, often working hand-in-hand in research areas like computational biology where sharing both data and methods is crucial.


### Software Quality and FAIR

For Research Software Engineers (RSEs), ensuring software quality is paramount. It directly impacts the reliability, reproducibility, and ultimately, the credibility of research findings. The FAIR (Findable, Accessible, Interoperable, Reusable) principles have emerged as a potent framework for enhancing research data quality. But can FAIR adequately address the multifaceted concerns surrounding software quality in RSE?

#### The Two Dimensions of Software Quality:

One has to distinguish between the form and function of software, each contributing to its overall quality:

- **Form**: Focuses on code quality, maintainability, and documentation. These aspects are closely aligned with FAIR principles. **_Clear documentation (F1)_**, use of **_persistent identifiers (F2)_**, and **_well-defined metadata (F3)_** improve findability and understanding. Adherence to **_community standards and open-source practices (F4)_** promotes interoperability and reusability.

- **Function**: Encompasses software's core functionality, including correctness, security, and computational efficiency. While FAIR indirectly supports some (e.g., clear documentation aids usability), it primarily addresses data management and sharing, leaving these crucial aspects outside its immediate scope.

#### Potential of FAIR for Form Quality:

FAIR principles offer invaluable tools for RSEs:

- **Transparency and Trust**: By making software findable and accessible (F1, A1), researchers can easily review and understand its functionality, fostering trust and collaboration.

- **Reproducibility and Sustainability**: Interoperable and reusable software (F4) facilitates re-running analyses and building upon existing work, enhancing research reproducibility and sustainability.

- **Community Engagement**: Open access to software through repositories (A1) encourages contributions and improves code quality through community scrutiny and testing.

**_Limitations of FAIR for Function Quality_**:

Despite its strengths, FAIR doesn't directly address:

- **Functional Correctness**: Ensuring software produces accurate results remains the responsibility of RSEs and requires rigorous testing, validation, and domain expertise.

- **Security**: FAIR doesn't explicitly cover security practices crucial for protecting sensitive data and preventing vulnerabilities.

- **Computational Efficiency**: Optimizing software performance falls outside FAIR's focus, relying on the RSE's understanding of algorithms and hardware constraints.

#### Complementary Approaches:

To address these limitations, RSEs need to combine FAIR principles with other established software quality practices:

- **Unit and integration testing**: Rigorous testing ensures functional correctness and identifies bugs.

- **Static code analysis**: Tools can detect potential vulnerabilities and code quality issues.

- **Peer review**: Expert evaluation provides valuable insights into both function and form.

- **Domain expertise**: Understanding the research context is crucial for ensuring software produces meaningful results.


FAIR principles offer a powerful framework for improving the form of research software, promoting findability, accessibility, interoperability, and reusability. However, RSEs need to employ complementary practices to ensure the functional quality of their software, including correctness, security, and efficiency. By combining FAIR with established software quality practices, RSEs can ensure their software meets the rigorous expectations of research.

### FAIR4RS Principles

The FAIR4RS Principles (Findable, Accessible, Interoperable, and Reusable for Research Software) {cite:p}`lamprecht2020towards, barker2022introducing, hong2022fair` aim to improve the sharing and reuse of research software, ultimately leading to more transparent, reproducible, and robust research. Developed by a collaborative effort from the Research Data Alliance, FORCE11, and Research Software Alliance, these principles provide a framework for researchers, developers, and other stakeholders to create and manage research software effectively.

#### Key Points of the FAIR4RS Principles

- **Findability:**
Software, and its associated metadata, is easy for both humans and machines to find.  

F1. Software is assigned a globally unique and persistent identifier.  
F1.1. Components of the software representing levels of granularity are assigned distinct identifiers.  
F1.2. Different versions of the software are assigned distinct identifiers.
F2. Software is described with rich metadata.  
F3. Metadata clearly and explicitly include the identifier of the software they describe.  
F4. Metadata are FAIR, searchable and indexable.  

- **Accessibility:**
Software, and its metadata, is retrievable via standardised protocols.  

A1. Software is retrievable by its identifier using a standardised communications protocol.  
A1.1. The protocol is open, free, and universally implementable.  
A1.2. The protocol allows for an authentication and authorization procedure, where necessary.  
A2. Metadata are accessible, even when the software is no longer available.  


- **Interoperability:**
Software interoperates with other software by exchanging data and/or metadata, and/or through interaction via application programming interfaces (APIs), described through standards.  

I1: Software uses community-recognized formats and standards for data, inputs, and outputs.  
I2: Application Programming Interfaces (APIs) are well-documented and support interoperability with other software.  
I3: The software interacts seamlessly with other relevant research tools and workflows.

- **Reusability:**
Software is both usable (can be executed) and reusable (can be understood, modified, built upon, or incorporated into other software)

R1: Software is described with a plurality of accurate and relevant attributes.  
R1.1: Software is given a clear and accessible license.  
R1.2: Software is associated with detailed provenance.  
R2: Software includes qualified references to other software.  
R3: Software meets domain-relevant community standards.  
#### Impact of FAIR4RS Principles

Adopting these principles benefits various stakeholders in the research community:

- **Researchers**: Increased transparency, reproducibility, and efficiency in conducting research.

- **Software developers**: Improved usability, maintenance, and community engagement for their software.

- **Funders**: More confident in investing in research with sustainable and reusable software practices.

- **Publishers**: Clear guidelines for evaluating and promoting FAIR research software.

Overall, the FAIR4RS Principles offer a valuable framework for creating and managing research software that contributes to a more collaborative, efficient, and trustworthy research ecosystem.


## Pragmatic FAIR

**"Five Recommendations for FAIR Software"**, [Netherlands eScience Center - fair-software.eu](https://fair-software.eu/)

1. Use a publicly accessible repository with version control. 
2. Add a license.
3. Register your code in a community registry.
4. Enable citation of the software.
5. Use a software quality checklist.

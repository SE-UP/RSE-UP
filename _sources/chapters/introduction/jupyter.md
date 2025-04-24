# Jupyter Notebooks
Jupyter Notebooks are interactive computing environments that enable users to create and share documents that combine live code, visualizations, explanatory text, and more. They offer a powerful platform for data analysis, scientific computing, and complex computational workflows, supporting an interactive and exploratory approach to programming and research.

While Python is the most widely used language in Jupyter Notebooks, they also support other programming languages such as R, Julia, and Scala. A notebook is structured into cells, which can contain code, formatted text, mathematical equations, or visual output. These cells can be executed independently or in sequence, allowing for flexible experimentation and step-by-step analysis.

One of the key strengths of Jupyter Notebooks is their support for **live code execution**, which enables an iterative and interactive workflow. Users can run and modify code snippets, immediately visualize the results, and make real-time observations, making the development process highly dynamic and responsive.

Jupyter Notebooks also foster **collaboration** by allowing users to share their work in a variety of formats, such as HTML, PDF, and Markdown. This versatility makes it easy to distribute notebooks across teams, publish them online, or include them in reports and documentation.

Because of their ability to seamlessly combine code, analysis, and narrative in a single, interactive environment, Jupyter Notebooks have become a **popular tool** in fields like academia, data science, machine learning, and scientific research. They offer a powerful platform for both individual exploration and collaborative innovation.

## Creating and Working With Jupyter Notebooks
Jupyter Notebooks are saved in files with the `.ipynb` extension, which stands for “Interactive Python Notebook.” These files serve as the primary format for storing all notebook content, including code cells, their outputs, markdown text, and any embedded visualizations or equations.

Internally, `.ipynb` files are structured using a JSON-based format, which captures the entire session state of a notebook. This makes them easy to share, version control, and reproduce across different environments. Whether you're collaborating with colleagues or archiving your work, `.ipynb` files ensure that everything—from code to commentary—is preserved in one cohesive document.

When opened in Jupyter Notebook or compatible platforms like JupyterLab or VS Code, the notebook appears as an interactive document. Users can freely modify and execute code cells, inspect outputs, explore data visualizations, and follow the surrounding narrative—all in one seamless interface.

## Starting a Jupyter Notebook Server
As a bridge between your computer and the web-based notebook interfaces, you need to start a Jupyter Notebook server, which can happen in two main ways. 
The Jupyter Notebook server can be started in two main ways. One common method is through **Anaconda Navigator**, a user-friendly graphical interface that allows you to launch Jupyter Notebooks with just a few clicks. Alternatively, you can start the server from the **command line** by simply running the command `jupyter notebook`, which will open the notebook interface in your default web browser. Both approaches provide access to the same interactive environment for working with notebooks.

## A Zipf Notebook
For our running example about Zipf's law, there's a [Notebook version available](https://gitup.uni-potsdam.de/se-up/rse_course/rse_course_materials/-/blob/main/zipf/bin/Zipf.ipynb), too.

## .ipynb or .py?
The choice between using `.ipynb` (Jupyter Notebook) files or `.py` (Python script) files ultimately depends on your specific needs and preferences. Generally speaking, `.py` files are ideal for traditional script development and are excellent for code reuse. They are particularly useful when you're creating structured, reusable modules or when building applications that may need a command-line interface (CLI). 

On the other hand, `.ipynb` files shine in situations where interactive data analysis, exploration, and documentation are key. They allow you to combine code, visualizations, and narrative explanations in a single document, making them particularly well-suited for data science, machine learning, and research tasks.

In many projects, a combination of both file types proves beneficial. For example, you might develop the core functionality and structure of your program in `.py` files, then import those modules into `.ipynb` files. This provides an interactive interface that allows you to explore and experiment with your code more flexibly while maintaining the modularity and reusability of your `.py` scripts.

### .ipynb pros and cons:

**Pro:**

✅ Interactivity and visualization<br> 
✅ Rich documentation<br> 
✅ Exploratory data analysis<br> 
✅ Collaboration and sharing

**Cons:**

❌ Complexity<br> 
❌ Limited portability<br> 
❌ Version control challenges

### .py pros and cons

**Pros:**

✅ Simplicity<br> 
✅ Portability<br> 
✅ Code reusability<br> 
✅ Better Version control

**Cons:** 

❌ Lack of interactivity<br> 
❌ Limited documentation capabilities<br> 
❌ Linear execution<br> 
❌ Visualization cumbersome


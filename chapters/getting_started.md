# Running Example and Project Organization


> Everything starts somewhere, though many physicists disagree.
>
> --- Terry Pratchett
 

As with many research projects, the first step in our Zipf's Law analysis
is to download the research data and install the required software.
Before doing that, it's worth taking a moment to think about
how we are going to organize everything.
We will soon have a number of books from [Project Gutenberg](https://www.gutenberg.org/) in the form of a series of text files, plots we've produced showing the word frequency distribution in each book, as well as the code we've written to produce those plots and to document and release our software package.
If we aren't organized from the start, things could get messy later on.

## Zipf's Law:
Imagine a giant bowl filled with words from all your favorite books. [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law), named after linguist George Kingsley Zipf, predicts a curious pattern within this jumble. As you scoop out the most used words, one by one, you'll find something fascinating: a rank-frequency relationship.

```{figure} ../figures/zipf/George_Kingsley_Zipf_1917.jpg 
:name  George Kingsley Zipf {cite:p}`1184354673`
```

The most frequent word will appear roughly twice as often as the second most frequent word, three times as often as the third, and so on. This means a small number of words ("the," "of," "and") dominate the word soup, while countless others appear rarely.

Mathematically, Zipf's law looks like this: frequency of a word $∝$ 1/rank. (Remember, "$∝$" means "proportional to.") So, ranking the words by frequency and plotting them on a graph creates a characteristic curved line (with axes on a log scale), showing the sharp drop-off in usage.

But Zipf's law isn't limited to words. It pops up in surprising places! Here are some examples:

- City sizes: The population of the second-largest city is roughly half that of the largest, the third is a third, and so on.

- Website hits: The most popular page on a website gets far more visits than the second, and so on.

- Income distribution: A small number of people hold a large chunk of wealth, while most have less. (This connects to the "Pareto principle", also known as the 80/20 rule.)

This can be seen in the following graph:

```{figure} ../figures/zipf/Zipf_30wiki_en_labels.png
:name Zipfs Law visualized

```

While not perfect, Zipf's law offers a powerful tool for understanding various systems. It tells us that few things are extremely common, while many things are rare. This pattern has implications for language evolution, information retrieval, economic analysis, and even urban planning.

However, it's important to remember that Zipf's law is an empirical observation, not an ironclad rule. Deviations occur, and other factors can influence frequency distributions. Still, its ubiquity and simplicity make it a valuable lens for exploring the hidden order in seemingly random data.

So, the next time you pick up a book, think of Zipf's law at work. The words you see most often are just the tip of the iceberg, reflecting a deeper pattern about how information is distributed in our world.

## Project Structure

Project organization is like a diet:
everyone has one, it's just a question of whether it's healthy or not.
In the case of a project, "healthy" means that people can find what they need and do what they want without becoming frustrated.
This depends on how well organized the project is and how familiar people are  with that style of organization.

As with good coding style, small pieces in predictable places with readable names are easier to find and use than large chunks that vary from project to project and have names like "stuff".
We can be messy while we are working and then tidy up later, but experience teaches that we will be more productive if we make tidiness a habit.

In building the Zipf's Law project, we'll follow a widely used template for organizing small and medium-sized data analysis projects {cite:p}`Nobl2009`.
The project will live in a directory called `zipf`, which will also be a Git repository stored on GitHub chapter [Git Command-line](https://se-up.github.io/RSE-UP/chapters/intro_version_control.html).

The following is an abbreviated version of the project directory tree
as it appears toward the end of the book:

```text
zipf/
├── .gitignore
├── CITATION.md
├── CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── README.md
├── Makefile
├── bin
│   ├── book_summary.sh
│   ├── collate.py
│   ├── countwords.py
│   └── ...
├── data
│   ├── README.md
│   ├── dracula.txt
│   ├── frankenstein.txt
│   └── ...
├── docs
│   └── ...
├── results
│   ├── collated.csv
│   ├── dracula.csv
│   ├── dracula.png
│   └── ...
└── ...
```

The full, final directory tree is documented in the [Appendix: Tree](https://se-up.github.io/RSE-UP/chapters/tree.html)

### Standard information

Our project will contain a few standard files that should be present in every research software project, open source or otherwise:

-   `README` includes basic information on our project. We'll add it in Section on including a [README](https://se-up.github.io/RSE-UP/chapters/introduction/documentation.html#readme-files)
     We'll create it in Chapter [Git Advanced](https://se-up.github.io/RSE-UP/chapters/git_advanced.html),
     and extend it in Chapter [Packaging](https://se-up.github.io/RSE-UP/chapters/python_packaging.html).

-   `LICENSE` is the project's license. We'll add it in Section on including a [license](https://se-up.github.io/RSE-UP/chapters/working_in_teams.html#software).

-   `CONTRIBUTING` explains how to contribute to the project. We'll add it in [here](https://se-up.github.io/RSE-UP/chapters/working_in_teams.html#make-all-this-obvious-to-newcomers).

-   `CONDUCT` is the project's Code of Conduct. We'll add it in [here](https://se-up.github.io/RSE-UP/chapters/working_in_teams.html#establish-a-code-of-conduct)

-   `CITATION` explains how to cite the software. We'll add it [here](https://se-up.github.io/RSE-UP/chapters/python_packaging.html#software-journals).

Some projects also include a `CONTRIBUTORS` or `AUTHORS` file that lists everyone who has contributed to the project, while others include that information in the `README` (we do this in Chapter [Git Advanced](https://se-up.github.io/RSE-UP/chapters/git_advanced.html)
or make it a section in `CITATION`.
These files are often called **boilerplate**, meaning they are copied without change from one use to the next.

### Organizing project content

Following {cite:p}`Nobl2009`, the directories in the repository's root are organized according to purpose:

-   Runnable programs go in `bin/`
    (an old Unix abbreviation for "binary", meaning "not text").
    This will include both shell scripts,
    e.g., `book_summary.sh` developed in Chapter [bash Advanced](https://se-up.github.io/RSE-UP/chapters/bash_advanced.html),,
    and Python programs,
    e.g., `countwords.py`, developed in Chapter [Building Command-Line Tools with Python](https://se-up.github.io/RSE-UP/chapters/python_cli.html).

-   Raw data goes in `data/`
    and is never modified after being stored.
    You'll set up this directory
    and its contents in Section [download the data](https://se-up.github.io/RSE-UP/chapters/getting_started.html#downloading-the-data).

-   Results are put in `results/`.
    This includes cleaned-up data,
    figures,
    and everything else created using what's in `bin` and `data`.
    In this project,
    we'll describe exactly how `bin` and `data` are used
    with `Makefile` created in Chapter [Introduction to Make and Snakemake](https://se-up.github.io/RSE-UP/chapters/introduction/automation.html).

-   Finally,
    documentation and manuscripts go in `docs/`.
    In this project,
    `docs` will contain automatically generated
    documentation for the Python package, created in
    Section on [Documentation using Sphinx](https://se-up.github.io/RSE-UP/chapters/python_packaging.html#creating-a-web-page-for-documentation).

This structure works well for many computational research projects and
we encourage its use beyond just this book.
We will add some more folders and files not directly addressed by {cite:p}`Nobl2009`
when we talk about testing (Chapter on [Testing](https://se-up.github.io/RSE-UP/chapters/testing_programs.html)),
provenance (Chapter [Tracking Provenance](https://se-up.github.io/RSE-UP/chapters/tracking_provenance.html)),
and packaging (Chapter [Packaging](https://se-up.github.io/RSE-UP/chapters/python_packaging.html)).


## Downloading the Data

The data files used in the book are archived at an online repository called Figshare (which we discuss in detail in Section on [where to archive data](https://se-up.github.io/RSE-UP/chapters/tracking_provenance.html#where-to-archive-data) and can be accessed at:

<https://doi.org/10.6084/m9.figshare.13040516>

We can download a zip file containing the data files by clicking
"download all" at this URL
and then unzipping the contents into a new `zipf/data` **directory**
(also called a **folder**)
that follows the project structure described above.
Here's how things look once we're done:

```text
zipf/
└── data
    ├── README.md
    ├── dracula.txt
    ├── frankenstein.txt
    ├── jane_eyre.txt
    ├── moby_dick.txt
    ├── sense_and_sensibility.txt
    ├── sherlock_holmes.txt
    └── time_machine.txt
```

## Summary 

Now that our project structure is set up, our data is downloaded, we are ready to start our analysis.

### Getting ready 

Make sure you've downloaded the required data files
(following Section [downloading the data ](https://se-up.github.io/RSE-UP/chapters/getting_started.html#downloading-the-data))
and installed the required software ([as described here](https://se-up.github.io/RSE-UP/chapters/install.html)) before progressing to the next chapter.

## Key Points

```{include} keypoints/getting_started.md

```

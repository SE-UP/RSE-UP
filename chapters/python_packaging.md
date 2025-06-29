# Creating Packages with Python 

We will continue with our Zipf's Law project, which should include the following files:

```text
zipf/
├── .gitignore
├── CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── README.md
├── requirements.txt
├── bin
│   ├── collate.py
│   ├── wordcount.py
│   ├── plotcount.py
│   ├── plotparams.yml
│   ├── template.py
│   ├── testzipfs.py
│   └── zipf.ipynb
├── data
│   ├── README.md
│   ├── dracula.txt
│   └── ...
├── results
│   ├── dracula.txt
│   ├── dracula.png
│   └── ...
└── test_data
    ├── random_words.txt
    └── risk.txt
```

## Creating a Python Package 

A package consists of one or more Python source files in a specific directory structure combined with installation instructions for the computer.
Python packages can come from various sources:
some are distributed with Python itself as part of the language's [standard library](https://docs.python.org/3/library/),
but anyone can create one,
and there are thousands that can be downloaded and installed from online repositories.

> **Terminology**
>
> People sometimes refer to packages as modules.
> Strictly speaking,
> a module is a single source file,
> while a package is a directory structure that contains one or more modules.

A generic package folder hierarchy looks like this:

```text
pkg_name
├── pkg_name
│   ├── module1.py
│   └── module2.py
├── README.md
└── setup.py
```



The top-level directory is named after the package.
It contains a directory that is also named after the package,
and that contains the package's source files.
It is initially a little confusing to have two directories with the same name,
but most Python projects follow this convention because
it makes it easier to set up the project for installation.

> **`__init__.py`**
>
> Python packages often contain a file with a special name:
> `__init__.py`
> (two underscores before and after `init`).
> Just as importing a module file executes the code in the module,
> importing a package executes the code in `__init__.py`.
> Packages *had* to have this file before Python 3.3,
> even if it was empty,
> but since Python 3.3 it is only needed
> if we want to run some code as the package is being imported.

If we want to make our Zipf's Law software available as a Python package,
we need to follow the generic folder hierarchy.
A quick search of the [Python Package Index (PyPI)](https://pypi.org/
) reveals that the package name `zipf` is already taken,
so we will need to use something different.
Let's use `pyzipf` and update our directory names accordingly:

```bash
$ mv ~/zipf ~/pyzipf
$ cd ~/pyzipf
$ mv bin pyzipf
```

> **Updating GitHub's Repository Name**
>
> We won't do it in this case
> (because it would break links/references from earlier in the book),
> but now that we've decided to name our package `pyzipf`,
> we would normally update the name of our GitHub repository to match.
> After changing the name at the GitHub website,
> we would need to update our `git remote` so that our 
> local repository could still be synchronized with GitHub: 
>
> ```bash
> $ git remote set-url origin https://gitlab.com/../YOUR_NAME/pyzipf.git  
> ```
*URL used is only an example*



Python has several ways to build an installable package.
We will show how to use [`setuptools`](https://setuptools.readthedocs.io/),
which is the lowest common denominator and will allow everyone, regardless of what Python distribution they have, to use our package. To use `setuptools`, we must create a file called `setup.py` in the directory *above* the root directory of the package. (This is why we require the two-level directory structure described earlier.)
`setup.py` must have exactly that name, and must contain lines like these:

```python
from setuptools import setup


setup(
    name='pyzipf',
    version='0.1.0',
    author='YOUR NAME',
    packages=['pyzipf'])
```

The `name` and `author` parameters are self-explanatory.
Most software projects use **semantic versioning**
for software releases.
A version number consists of three integers X.Y.Z,
where X is the major version, Y is the minor version,
and Z is the **patch** version.
Major version zero (0.Y.Z) is for initial development, so we have started with 0.1.0.
The first stable public release would be version 1.0.0,
and in general, the version number is incremented as follows:

-   Increment `major` every time there's an incompatible externally visible change.
-   Increment `minor` when adding new functionality in a backwards-compatible manner
    (i.e., without breaking any existing code).
-   Increment `patch` for backwards-compatible bug fixes that don't add any new features.

Finally,
we specify the name of the directory
containing the code to be packaged with the `packages` parameter.
This is straightforward in our case because we only have a single package directory.
For more complex projects,
the [`find_packages`](https://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages) function from `setuptools`
can automatically find all packages by recursively searching the current directory.

## Virtual Environments 

We can add additional information to our package later,
but this is enough to be able to build it for testing purposes.
Before we do that,
though,
we should create a **virtual environment** to test how our package installs
without breaking anything in our main Python installation.
We exported details of our environment in Chapter [Provenance](https://se-up.github.io/RSE-UP/chapters/tracking_provenance.html) as a way to document the software we're using;
in this section, we'll use environments to make the software we're creating more robust.

A virtual environment is a layer on top of an existing Python installation.
Whenever Python needs to find a package,
it looks in the virtual environment before checking the main Python installation.
This gives us a place to install packages that only some projects need
without affecting other projects.

Virtual environments also help with package development:

-   We want to be able to easily test install and uninstall our package,
    without affecting the entire Python environment.
-   We want to answer problems people have with our package with something more helpful than
    "I don't know, it works for me."
    By installing and running our package in a completely empty environment,
    we can ensure that we're not accidentally relying on other packages being installed.

There are multiple ways to manage virtual environments: 

You can manage virtual environments using [`conda`](https://conda.io/) (Appendix [Anaconda](https://se-up.github.io/RSE-UP/chapters/anaconda.html)) or you can use [`pyenv`](https://github.com/pyenv/pyenv). 

Follow the instructions to setup [`PYENV`](https://github.com/pyenv/pyenv)
Or if you want to stick to Anaconda follow the tutorial [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).  

## Installing a Development Package 

Let's install our package in this virtual environment.
First we re-activate it:

In Anaconda:
```bash
$ conda activate pyzipf
```
in PYENV
```bash
$ pyenv activate pyzipf
```

Next,
we go into the upper `pyzipf` directory that contains our `setup.py` file
and install our package:

```bash
(pyzipf)$ cd ~/pyzipf
(pyzipf)$ pip install -e .
```

```text
Obtaining file:///Users/YOUR-NAME/pyzipf
Installing collected packages: pyzipf
  Running setup.py develop for pyzipf
Successfully installed pyzipf
```

The `-e` option indicates that we want to install the package in "editable" mode,
which means that any changes we make in the package code are directly available to use
without having to reinstall the package;
the `.` means "install from the current directory."

If we look in the location containing package installations 
(e.g., `/Users/YOUR-NAME/anaconda3/envs/pyzipf/lib/python3.12/site-packages/`),
we can see the `pyzipf` package beside all the other locally installed packages.
If we try to use the package at this stage,
though,
Python will complain that some of the packages it depends on,
such as `pandas`,
are not installed.
We could install these manually,
but it is more reliable to automate this process
by listing everything that our package depends on
using the `install_requires` parameter in `setup.py`:

```python
from setuptools import setup


setup(
    name='pyzipf',
    version='0.1',
    author='YOUR-NAME',
    packages=['pyzipf'],
    install_requires=[
        'matplotlib',
        'pandas',
        'scipy',
        'pyyaml',
        'pytest'])
```

We don't have to list `numpy` explicitly
because it will be installed as a dependency for `pandas` and `scipy`.

> **Versioning Dependencies**
>
> It is good practice to specify the versions of our dependencies
> and even better to specify version ranges.
> For example, if we have only tested our package on pandas version 1.1.2,
> we could put `pandas==1.1.2` or `pandas>=1.1.2` instead of just `pandas`
> in the list argument passed to the `install_requires` parameter.

Next,
we can install our package using the modified `setup.py` file:

```bash
(pyzipf)$ cd ~/pyzipf
(pyzipf)$ pip install -e .
```

```text
Obtaining file:///Users/YOUR-NAME/pyzipf
Collecting matplotlib
  Downloading matplotlib-3.3.3-cp37-cp37m-macosx_10_9_x86_64.whl
     |████████████████████████████████| 8.5 MB 3.1 MB/s 
Collecting cycler>=0.10
  Using cached cycler-0.10.0-py2.py3-none-any.whl
Collecting kiwisolver>=1.0.1
  Downloading kiwisolver-1.3.1-cp37-cp37m-macosx_10_9_x86_64.whl 
     |████████████████████████████████| 61 kB 2.0 MB/s 
Collecting numpy>=1.15
  Downloading numpy-1.19.4-cp37-cp37m-macosx_10_9_x86_64.whl
     |████████████████████████████████| 15.3 MB 8.9 MB/s 
Collecting pillow>=6.2.0
  Downloading Pillow-8.0.1-cp37-cp37m-macosx_10_10_x86_64.whl
     |████████████████████████████████| 2.2 MB 6.3 MB/s 
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3
  Using cached pyparsing-2.4.7-py2.py3-none-any.whl
Collecting python-dateutil>=2.1
  Using cached python_dateutil-2.8.1-py2.py3-none-any.whl
Collecting six
  Using cached six-1.15.0-py2.py3-none-any.whl
Collecting pandas
  Downloading pandas-1.1.5-cp37-cp37m-macosx_10_9_x86_64.whl
     |████████████████████████████████| 10.0 MB 1.4 MB/s 
Collecting pytz>=2017.2
  Using cached pytz-2020.4-py2.py3-none-any.whl
Collecting pytest
  Using cached pytest-6.2.1-py3-none-any.whl
Collecting attrs>=19.2.0
  Using cached attrs-20.3.0-py2.py3-none-any.whl
Collecting importlib-metadata>=0.12
  Downloading importlib_metadata-3.3.0-py3-none-any.whl
Collecting pluggy<1.0.0a1,>=0.12
  Using cached pluggy-0.13.1-py2.py3-none-any.whl
Collecting py>=1.8.2
  Using cached py-1.10.0-py2.py3-none-any.whl
Collecting typing-extensions>=3.6.4
  Downloading typing_extensions-3.7.4.3-py3-none-any.whl
Collecting zipp>=0.5
  Downloading zipp-3.4.0-py3-none-any.whl
Collecting iniconfig
  Using cached iniconfig-1.1.1-py2.py3-none-any.whl
Collecting packaging
  Using cached packaging-20.8-py2.py3-none-any.whl
Collecting pyyaml
  Using cached PyYAML-5.3.1.tar.gz
Collecting scipy
  Downloading scipy-1.5.4-cp37-cp37m-macosx_10_9_x86_64.whl
     |████████████████████████████████| 28.7 MB 10.7 MB/s 
Collecting toml
  Using cached toml-0.10.2-py2.py3-none-any.whl
Building wheels for collected packages: pyyaml
  Building wheel for pyyaml (setup.py) ... done
  Created wheel for pyyaml:
    filename=PyYAML-5.3.1-cp37-cp37m-macosx_10_9_x86_64.whl
    size=44626
    sha256=5a59ccf08237931e7946ec6b526922e4
           f0c8ee903d43671f50289431d8ee689d
  Stored in directory: /Users/amira/Library/Caches/pip/wheels/
    5e/03/1e/e1e954795d6f35dfc7b637fe2277bff021303bd9570ecea653
Successfully built pyyaml
Installing collected packages: zipp, typing-extensions, six,
pyparsing, importlib-metadata, toml, pytz, python-dateutil, py,
pluggy, pillow, packaging, numpy, kiwisolver, iniconfig, cycler,
attrs, scipy, pyyaml, pytest, pandas, matplotlib, pyzipf
  Attempting uninstall: pyzipf
    Found existing installation: pyzipf 0.1.0
    Uninstalling pyzipf-0.1.0:
      Successfully uninstalled pyzipf-0.1.0
  Running setup.py develop for pyzipf
Successfully installed attrs-20.3.0 cycler-0.10.0
importlib-metadata-3.3.0 iniconfig-1.1.1 kiwisolver-1.3.1
matplotlib-3.3.3 numpy-1.19.4 packaging-20.8 pandas-1.1.5
pillow-8.0.1 pluggy-0.13.1 py-1.10.0 pyparsing-2.4.7
pytest-6.2.1 python-dateutil-2.8.1 pytz-2020.4 pyyaml-5.3.1
pyzipf scipy-1.5.4 six-1.15.0 toml-0.10.2
typing-extensions-3.7.4.3 zipp-3.4.0
```

(The precise output of this command will change
depending on which versions of our dependencies get installed.)

We can now import our package in a script or a [Jupyter notebook](https://jupyter.org/) just as we would any other package.
For example, to use the function in `zipftest`, we would write:

```python
from pyzipf import zipftest as zt


zt.collection_to_csv(...)
```

To allow our functions to continue accessing `zipftest.py`,
we need to change that line in both `wordcount.py` and `collate.py`.

However,
the useful command-line scripts that we used to count and plot word counts
are no longer accessible directly from the Unix shell.
Fortunately there is an alternative to changing the function import
as described above.
The `setuptools` package allows us to install programs along with the package.
These programs are placed beside those of other packages.
We tell `setuptools` to do this by defining
**entry points** in `setup.py`:

```python
from setuptools import setup


setup(
    name='pyzipf',
    version='0.1',
    author='Your-Name',
    packages=['pyzipf'],
    install_requires=[
        'matplotlib',
        'pandas',
        'scipy',
        'pyyaml',
        'pytest'],
    entry_points={
        'console_scripts': [
            'wordcount= pyzipf.wordcount:main',
            'collate = pyzipf.collate:main',
            'plotcount = pyzipf.plotcount:main']})
```

The right side of the `=` operator is the location of a function,
written as `package.module:function`;
the left side is the name we want to use to call this function from the command line.
In this case we want to call each module's `main` function;
right now, we do not have one yet since the iput argument `args` are handled elsewhere. Thus we need to create a main function 
containing the command-line arguments given by the user (Section [Scripting Options](https://se-up.github.io/RSE-UP/chapters/python_cli.html#handling-command-line-options)).

Since we can't pass any arguments to `main` when we define entry points in our `setup.py` file,
so we need to factor this in:

```python

def main():
    parser = argparse.ArgumentParser(description="Process word counts and generate plots.")
    parser.add_argument("input_file", type=str, help="Input file with word counts")
    parser.add_argument("output_file", type=str, help="Output file or display mode")
    parser.add_argument("--limit", type=int, default=10, help="Limit the number of word counts to display")
    parser.add_argument('--plotparams', type=str, default=None, help='matplotlib parameters (YAML file)')    
    
    args = parser.parse_args()

    counts = load_word_counts(args.input_file)
    set_plot_params(args.plotparams)
    
    plot_word_counts(counts, args.limit)

    if args.output_file == "show":
        plt.show()
    elif args.output_file == "ascii":
        words, counts, _ = list(zip(*counts))
        for line in plot_ascii_bars(counts[:args.limit], words[:args.limit], truncate=False):
            print(line)
    else:
        plt.savefig(args.output_file)

if __name__ == "__main__":
    main()
```

 `main()` does not require any input arguments.

Once we have made the corresponding change in `collate.py` and `plotcount.py`,
we can re-install our package:

```bash
(pyzipf)$ pip install -e .
```

```text
Defaulting to user installation because normal site-packages is
  not writeable
Obtaining ...
....
....
Installing collected packages: pyzipf
  Running setup.py develop for pyzipf
Successfully installed pyzipf
```

The output looks slightly different than the first run
because `pip` could re-use some packages saved locally by the previous install
rather than re-fetching them from online repositories.
(If we hadn't used the `-e` option to make the package immediately editable,
we would have to uninstall it before reinstalling it during development.)

We can now use our commands directly from the Unix shell
without writing the full path to the file
and without prefixing it with `python`.

```bash
(pyzipf)$ countwords data/dracula.txt -n 5
```

```text
the,8036
and,5896
i,4712
to,4540
of,3738
```

> **Tracking `pyzipf.egg-info`?**
> 
> Using `setuptools` automatically creates a new folder
> in your project directory named `pyzipf.egg-info`.
> This folder is [another example](https://github.com/github/gitignore) of information generated by a script
> that is also included in the repository,
> so it should be included in the `.gitignore` file to avoid tracking with Git.

## What Installation Does 

Now that we have created and installed a Python package,
let's explore what actually happens during installation.
The short version is that the contents of the package are copied into a directory that Python will search when it imports things.
In theory we can "install" packages by manually copying source code into the right places, but it's much more efficient and safer to use a tool specifically made for this purpose, such as `conda` or `pip`.

Most of the time, these tools copy packages into the Python installation's `site-packages` directory, but this is not the only place Python searches. Just as the `PATH` environment in the shell contains a list of directories it searches. We can look at this list inside the interpreter:

```python
import sys
sys.path
```

```text
['', '/usr/lib64/python312.zip', '/usr/lib64/python3.12', '/usr/lib64/python3.12/lib-dynload', '/home/nibe/.local/lib/python3.12/site-packages', '/usr/lib64/python3.12/site-packages', '/usr/lib/python3.12/site-packages']
```

The empty string at the start of the list means "the current directory."
The rest are system paths for our Python installation,
and will vary from computer to computer.

## Distributing Packages 

> **Look but Don't Execute**
>
> In this section we upload the `pyzipf` package
> to TestPyPI and PyPI:
>
> <https://test.pypi.org/project/pyzipf>
>
> <https://pypi.org/project/pyzipf/>
>
> You won't be able to execute the `twine upload`
> commands below exactly as shown
> (because Amira has already uploaded the `pyzipf` package),
> but the general sequence of commands in this section
> is an excellent resource to refer to when you are
> uploading your own packages.
> If you want to try uploading your own `pyzipf` package via `twine`,
> you could edit the project name to include your name (e.g., `pyzipf-yourname`)
> and use the TestPyPI repository for the upload.

An installable package is most useful
if we distribute it so that anyone who wants it
can run `pip install pyzipf` and get it. To make this possible,
we need to use `setuptools` to create a **source distribution** (known as an `sdist` in Python packaging jargon):

```bash
(pyzipf)$ python setup.py sdist
```

```text
running sdist
running egg_info
creating pyzipf.egg-info
writing pyzipf.egg-info/PKG-INFO
writing dependency_links to pyzipf.egg-info/dependency_links.txt
writing entry points to pyzipf.egg-info/entry_points.txt
writing requirements to pyzipf.egg-info/requires.txt
writing top-level names to pyzipf.egg-info/top_level.txt
writing manifest file 'pyzipf.egg-info/SOURCES.txt'
package init file 'pyzipf/__init__.py' not found
(or not a regular file)
reading manifest file 'pyzipf.egg-info/SOURCES.txt'
writing manifest file 'pyzipf.egg-info/SOURCES.txt'
running check
warning: check: missing required meta-data: url

warning: check: missing meta-data: if 'author' supplied, 
                'author_email' must be supplied too

creating pyzipf-0.1
creating pyzipf-0.1/pyzipf
creating pyzipf-0.1/pyzipf.egg-info
copying files to pyzipf-0.1...
copying README.md -> pyzipf-0.1
copying setup.py -> pyzipf-0.1
copying pyzipf/collate.py ->
  pyzipf-0.1/pyzipf
copying pyzipf/countwords.py ->
  pyzipf-0.1/pyzipf
copying pyzipf/plotcounts.py ->
  pyzipf-0.1/pyzipf
copying pyzipf/script_template.py ->
  pyzipf-0.1/pyzipf
copying pyzipf/test_zipfs.py ->
  pyzipf-0.1/pyzipf
copying pyzipf/utilities.py ->
  pyzipf-0.1/pyzipf
copying pyzipf.egg-info/PKG-INFO ->
  pyzipf-0.1/pyzipf.egg-info
copying pyzipf.egg-info/SOURCES.txt ->
  pyzipf-0.1/pyzipf.egg-info
copying pyzipf.egg-info/dependency_links.txt ->
  pyzipf-0.1/pyzipf.egg-info
copying pyzipf.egg-info/entry_points.txt ->
  pyzipf-0.1/pyzipf.egg-info
copying pyzipf.egg-info/requires.txt ->
  pyzipf-0.1/pyzipf.egg-info
copying pyzipf.egg-info/top_level.txt ->
  pyzipf-0.1/pyzipf.egg-info
Writing pyzipf-0.1/setup.cfg
creating dist
Creating tar archive
removing 'pyzipf-0.1' (and everything under it)
```

This creates a file named `pyzipf-0.1.tar.gz`,
located in a new directory in our project, `dist/`
(another directory to add to [`.gitignore`](https://github.com/github/gitignore)).
These distribution files can now be distributed via [PyPI](https://pypi.org),
the standard repository for Python packages.
Before doing that, though, we can put `pyzipf` on [TestPyPI](https://test.pypi.org), which lets us test the distribution of our package
without having things appear in the main PyPI repository.
We must have an account,
but they are free to create.

The preferred tool for uploading packages to PyPI is called [twine](https://twine.readthedocs.io/en/latest/), which we can install with:

```bash
(pyzipf)$ pip install twine
```

Following the [Python Packaging User Guide](https://packaging.python.org/guides/using-testpypi/), we upload our distribution from the `dist/` folder
using the `--repository` option to specify the TestPyPI repository:

```bash
$ twine upload --repository testpypi dist/*
```

```text
Uploading distributions to https://test.pypi.org/legacy/
```

```bash
Enter your username: YOUR NAME
Enter your password: *********
```

```text
Uploading pyzipf-0.1.0.tar.gz
100%|█████████████████| 5.59k/5.59k [00:01<00:00, 3.27kB/s]

View at:
https://test.pypi.org/project/pyzipf/0.1/
```

```{figure} ../figures/packaging/testpypi.png
:name: packaging-testpypi
Test PyPi
```
and view the results at the new test project webpage
([Figure Test Pypi](packaging-testpypi)).
In the exercises,
we will explore additional metadata that can be added to `setup.py`
so that it appears on the project webpage.

We can test that everything works as expected
by creating a virtual environment
and installing our package from TestPyPI 
(the `--extra-index-url` reference to PyPI below accounts for the fact that
not all of our package dependencies are available on TestPyPI):

```bash
(pyzipf)$ conda create -n pyzipf-test pip python=3.7.6
(pyzipf)$ conda activate pyzipf-test 
(pyzipf-test)$ pip install --index-url
  https://test.pypi.org/simple 
  --extra-index-url https://pypi.org/simple pyzipf
```



```text
Looking in indexes: https://test.pypi.org/simple,
                    https://pypi.org/simple
Collecting pyzipf
  Downloading pyzipf-0.1.tar.gz (5.5 kB)
Collecting matplotlib
 Using cached matplotlib-3.3.3-cp37-cp37m-macosx_10_9_x86_64.whl
...collecting other packages...
Building wheels for collected packages: pyzipf
  Building wheel for pyzipf (setup.py) ... done
  Created wheel for pyzipf:
    filename=pyzipf-0.1-py3-none-any.whl
    size=6836
    sha256=62a23715379b71ad5a6b124444fab194
           596d094c7df293c4019d33bdd648aff1
  Stored in directory: /Users/amira/Library/Caches/pip/wheels/
   c6/d6/08/f16cf80ec82a9c70ab8a5d9c8acc7ab35c9a01009539aeb2be
Successfully built pyzipf
Installing collected packages: zipp, typing-extensions, six,
pyparsing, importlib-metadata, toml, pytz, python-dateutil, py,
pluggy, pillow, packaging, numpy, kiwisolver, iniconfig, cycler,
attrs, scipy, pyyaml, pytest, pandas, matplotlib, pyzipf
Successfully installed attrs-20.3.0 cycler-0.10.0
importlib-metadata-3.3.0 iniconfig-1.1.1 kiwisolver-1.3.1
matplotlib-3.3.3 numpy-1.19.4 packaging-20.8 pandas-1.1.5
pillow-8.0.1 pluggy-0.13.1 py-1.10.0 pyparsing-2.4.7
pytest-6.2.1 python-dateutil-2.8.1 pytz-2020.4 pyyaml-5.3.1
pyzipf-0.1 scipy-1.5.4 six-1.15.0 toml-0.10.2
typing-extensions-3.7.4.3 zipp-3.4.0
```

Once again,
`pip` takes advantage of the fact that some packages already existing on our system
(e.g., they are cached from our previous installs)
and doesn't download them again.
Once we are happy with our package at TestPyPI,
we can go through the same process to put it on the main [PyPI](https://pypi.org) repository.

> **Python Wheels**
>
> When we installed our package from TestPyPI,
> the output said that it collected our source distribution 
> and then used it to build a **wheel** for `pyzipf`.
> This build takes time (especially for large, complex packages),
> so it can be a good idea for package authors to create and upload wheel files (`.whl`)
> to PyPI along with the source distribution.
> `pip` will use the appropriate wheel file if it's available at PyPI
> instead of building it from the source distribution,
> which makes the installation process faster and more efficient.
> Check out the [Real Python guide to wheels](https://realpython.com/python-wheels/) for details.     

> **`conda` Installation Packages**
>
> Given the widespread use of [`conda`](https://conda.io) for package management,
> it can be a good idea to post a `conda` installation package to
> [Anaconda Cloud](https://anaconda.org).
> The `conda` documentation has [instructions](https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html) for quickly building
> a `conda` package for a Python module that is already available on PyPI.
> See [Appendix on Anaconda](https://se-up.github.io/RSE-UP/chapters/anaconda.html) for more information about `conda` and Anaconda Cloud.

## Documenting Packages 

Now that our package has been distributed,
we need to think about whether we have provided sufficient documentation.
Docstrings (Section [Docstrings](https://se-up.github.io/RSE-UP/chapters/writing_documentation.html)) and READMEs
are sufficient to describe most simple packages,
but as our code base grows larger,
we will want to complement these manually written sections with automatically generated content,
references between functions,
and search functionality.
For most large Python packages,
such documentation is generated using a **documentation generator**} called [Sphinx](https://www.sphinx-doc.org/en/master/),
which is often used in combination with a free online hosting service called
[Read the Docs](https://docs.readthedocs.io/en/stable/config-file/v2.html).
In this section we will update our README file with some basic package-level documentation,
before using Sphinx and Read the Docs to host that information online
along with more detailed function-level documentation.
For further advice on writing documentation for larger and more complex packages,
see Chapter [Documentation](https://se-up.github.io/RSE-UP/chapters/writing_documentation.html)).

### Including package-level documentation in the `README` 

When a user first encounters a package, they usually want to know what the package is meant to do,instructions on how to install it, and examples of how to use it. We can include these elements in the `README.md` file we started in [Chapter Git Advanced](https://se-up.github.io/RSE-UP/chapters/git_advanced.html). At the moment it reads as follows:

```bash
$ cat README.md
```

```text
# Zipf's Law

These Zipf's Law scripts tally the occurrences of words in text
files and plot each word's rank versus its frequency.

...
```

This file is currently written in [Markdown](https://se-up.github.io/RSE-UP/chapters/introduction/documentation.html), but Sphinx uses a format called **reStructuredText** (reST), so we will switch to that. Like Markdown, reST is a plain-text markup format that can be rendered into HTML or PDF documents with complex indices and cross-links. GitHub recognizes files ending in `.rst` as reST files and displays them nicely,
so our first task is to rename our existing file:

```bash
$ git mv README.md README.rst
```

We then make a few edits to the file formatting:
titles are underlined and overlined,
section headings are underlined,
and code blocks are set off with two colons (`::`) and indented.
We can also add some context about why to use the package,
as well as updated information about package installation:

```markdown
The ``pyzipf`` package tallies the occurrences of words in text
files and plots each word's rank versus its frequency together 
with a line for the theoretical distribution for Zipf's Law.

Motivation
----------

Zipf's Law is often stated as an observational pattern in the
relationship between the frequency and rank of words in a text:

`"…the most frequent word will occur approximately twice as
often as the second most frequent word,
three times as often as the third most
frequent word, etc."`
— `wikipedia <https://en.wikipedia.org/wiki/Zipf%27s_law>`_

Many books are available to download in plain text format
from sites such as
`Project Gutenberg <https://www.gutenberg.org/>`_,
so we created this package to qualitatively explore how well
different books align with the word frequencies predicted by
Zipf's Law.

Installation
------------

``pip install pyzipf``

Usage
-----

After installing this package, the following three commands will
be available from the command line

- ``countwords`` for counting the occurrences of words in a text
- ``collate`` for collating multiple word count files together
- ``plotcounts`` for visualizing the word counts

A typical usage scenario would include running the following
from your terminal::

    countwords dracula.txt > dracula.csv
    countwords moby_dick.txt > moby_dick.csv
    collate dracula.csv moby_dick.csv > collated.csv
    plotcounts collated.csv --outfile zipf-drac-moby.jpg

Additional information on each function
can be found in their docstrings and appending the ``-h`` flag,
e.g., ``countwords -h``.

Contributing
------------

Interested in contributing?
Check out the CONTRIBUTING.md
file for guidelines on how to contribute.
Please note that this project is released with a
Contributor Code of Conduct (CONDUCT.md).
By contributing to this project,
you agree to abide by its terms.
Both of these files can be found in our
`GitHub repository. <https://github.com/amira-khan/zipf>`_
```

### Creating a web page for documentation 

Now that we've added package-level documentation to our README file,
we need to think about function-level documentation.
We want to provide users with a list of all the functions available in our package
along with a short description of what they do and how to use them.
We could achieve this by manually cutting and pasting function names and docstrings
from our Python modules (i.e., `wordcount.py`, `plotcount.py`, etc.),
but that would be a time-consuming process prone to errors as more functions are added over time.
Instead, we can use a **documentation generator** called [Sphinx](https://www.sphinx-doc.org/en/master/) that is capable of scanning Python code for function names and docstrings and can export that information to HTML format for hosting on the web.

To start, let's install Sphinx and create a `docs/` directory at the top of our repository:

```bash
$ pip install sphinx
$ mkdir docs
$ cd docs
```

We can then run Sphinx's `quickstart` tool to create a minimal set of documentation
that includes the package-level information in the `README.rst` file we just created
and the function-level information in the docstrings we've written along the way.
It asks us to specify the project's name,
the name of the project's author,
and a release;
we can use the default settings for everything else.

```bash
$ sphinx-quickstart
```

```text
Welcome to the Sphinx 3.1.1 quickstart utility.

Please enter values for the following settings (just press Enter
to accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx
output. Either, you use a directory "_build" within the root
path, or you separate "source" and "build" directories within
the root path.
```

```bash
> Separate source and build directories (y/n) [n]: n
```

```text
The project name will occur in several places in the built
documentation.
```

```bash
> Project name: pyzipf
> Author name(s): YOUR NAME
> Project release []: 0.1
```

```text
If the documents are to be written in a language other than
English, you can select a language here by its language code.
Sphinx will then translate text that it generates into that
language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html
```

```bash
> Project language [en]:
```

```text
Creating file /Users/amira/pyzipf/docs/conf.py.
Creating file /Users/amira/pyzipf/docs/index.rst.
Creating file /Users/amira/pyzipf/docs/Makefile.
Creating file /Users/amira/pyzipf/docs/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file
/Users/amira/pyzipf/docs/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. HTML,
LaTeX or linkcheck.
```

`quickstart` creates a file called `conf.py` in the `docs` directory that configures Sphinx.
We will make two changes to that file
so that another tool called `autodoc` can find our modules (and their docstrings).
The first change relates to the "path setup" section near the head of the file:

```text
# -- Path setup -----------------------------------------------

# If extensions (or modules to document with autodoc) are in
# another directory, add these directories to sys.path here. If
# the directory is relative to the documentation root, use
# os.path.abspath to make it absolute, like shown here.
```

Relative to the `docs/` directory,
our modules (i.e., `countwords.py`, `utilities.py`, etc.) are located in the `../pyzipf` directory.
We therefore need to uncomment the relevant lines of the path setup section in `conf.py`
to tell Sphinx where those modules are:

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../pyzipf'))
```

We will also change the "general configuration" section
to add `autodoc` to the list of Sphinx extensions we want:

```python
extensions = ['sphinx.ext.autodoc']
```



With those edits complete,
we can now generate a Sphinx `autodoc` script
that generates information about each of our modules
and puts it in corresponding `.rst` files in the `docs/source` directory:

```bash
sphinx-apidoc -o source/ ../pyzipf
```

```text
Creating file source/collate.rst.
Creating file source/countwords.rst.
Creating file source/plotcounts.rst.
Creating file source/test_zipfs.rst.
Creating file source/utilities.rst.
Creating file source/modules.rst.
```

At this point, we are ready to generate our webpage.
The `docs` sub-directory contains a Makefile that was generated by `sphinx-quickstart`.
If we run `make html` and open `docs/_build/index.html` in a web browser,
we'll have a landing page with minimal documentation ([Figure Packaging Sphinx Landing page](packaging-sphinx-landing-page-original)).
If we click on the `Module Index` link we can access the documentation for the individual modules
(Figures [Module List](packaging-sphinx-module-list) and [Sphinx Module Countwords](packaging-sphinx-module-countwords)).

```{figure} ../figures/packaging/landing-page-original.png
:name: packaging-sphinx-landing-page-original
Packaging Sphinx Landing Page
```
```{figure} ../figures/packaging/module-index.png
:name: packaging-sphinx-module-list
Sphinx Module List
```

```{figure} ../figures/packaging/module-countwords.png
:name: packaging-sphinx-module-countwords
Sphinx Module Countwords
```

The landing page for the website is the perfect place for the content of our README file,
so we can add the line `.. include:: ../README.rst` to the `docs/index.rst` file to insert it:

```markdown
Welcome to pyzipf's documentation!
==================================

.. include:: ../README.rst

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

If we re-run `make html`,
we now get an updated set of web pages that
re-uses our README as the introduction to the documentation (Figure [Sphinx Landing page](packaging-sphinx-landing-page)).

```{figure} ../figures/packaging/landing-page.png
:name: packaging-sphinx-landing-page
Sphinx Landing page
```

Before going on,
note that Sphinx is not included in the installation requirements in `requirements.txt` ([Chapter CI/CD](https://se-up.github.io/RSE-UP/chapters/introduction/cicd.html).
Sphinx isn't needed to run, develop, or even test our package,
but it is needed for building the documentation.
To note this requirement,
but without requiring everyone installing the package to install Sphinx,
let's create a `requirements_docs.txt` file that contains this line
(where the version number is found by running `pip freeze`):

```text
Sphinx>=1.7.4
```

Anyone wanting to build the documentation (including us, on another computer)
now only needs run `pip install -r requirements_docs.txt`

### Hosting documentation online 

Now that we have generated our package documentation,
we need to host it online.
A common option for Python projects is [Read the Docs](https://docs.readthedocs.io/en/latest/), which is a community-supported site that hosts software documentation free of charge.

Just as continuous integration systems automatically re-test things ([Chapter CI/CD](https://se-up.github.io/RSE-UP/chapters/introduction/cicd.html), Read the Docs integrates with GitHub
so that documentation is automatically re-built
every time updates are pushed to the project's GitHub repository.
If we register for Read the Docs with our GitHub account,
we can log in at the Read the Docs website and
import a project from our GitHub repository.
Read the Docs will then build the documentation
(using `make html` as we did earlier)
and host the resulting files.

For this to work,
all of the source files generated by Sphinx
need to be checked into your GitHub repository:
in our case,
this means `docs/source/*.rst`,
`docs/Makefile`,
`docs/conf.py`,
and `docs/index.rst`.
We also need to create and save a
[Read the Docs configuration file](https://docs.readthedocs.io/en/stable/config-file/v2.html) in the root directory of our `pyzipf` package:

```bash
$ cd ~/pyzipf
$ cat .readthedocs.yml
```

```text
# .readthedocs.yml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html
# for details

# Required
version: 2

# Build documentation in the docs/ directory with Sphinx
sphinx:
  configuration: docs/conf.py

# Optionally set the version of Python and requirements required
# to build your docs
python:
  version: 3.7
  install:
    - requirements: requirements.txt
```

The configuration file uses the now-familiar **YAML** format
(Section [Configuration Formats](https://se-up.github.io/RSE-UP/chapters/configuration.html#configuration-file-formats) and Appendix [YAML](https://se-up.github.io/RSE-UP/chapters/yaml.html) to specify the location of the Sphinx configuration script (`docs/conf.py`) and the dependencies for our package (`requirements.txt`).

Amira has gone through this process and the documentation is now available at:

<https://pyzipf.readthedocs.io/>

## Software Journals 

As a final step to releasing our new package,
we might want to give it a **DOI** so that it can be cited by researchers. As we saw in Section [Provenance Code Scripts](https://se-up.github.io/RSE-UP/chapters/tracking_provenance.html#code-provenance),
GitHub [integrates with Zenodo](https://guides.github.com/activities/citable-code/) for precisely this purpose.

While creating a DOI using a site like Zenodo
is often the end of the software publishing process,
there is the option of publishing
a journal paper to describe the software in detail.
Some research disciplines have journals devoted
to describing particular types of software
(e.g., [*Geoscientific Model Development*](https://www.geoscientific-model-development.net/)),
and there are also a number of generic software journals such as the
[*Journal of Open Research Software*]( https://openresearchsoftware.metajnl.com/) and
the [*Journal of Open Source Software*]( https://joss.theoj.org/).
Packages submitted to these journals are typically assessed against a range of criteria
relating to how easy the software is to install
and how well it is documented,
so the peer review process can be a great way to get critical feedback
from people who have seen many research software packages come and go over the years.

Once you have obtained a DOI and possibly published with a software journal,
the last step is to tell users how to cite your new software package.
This is traditionally done by adding a `CITATION` file to the associated GitHub repository (alongside `README`, `LICENSE`, `CONDUCT` and similar files discussed in Section [Getting Started](https://se-up.github.io/RSE-UP/chapters/getting_started.html#standard-information)), containing a plain text citation that can be copied and pasted into email as well as entries formatted for various bibliographic systems like [BibTeX](http://www.bibtex.org/).

```bash
$ cat CITATION.md
```

```text
# Citation

If you use the pyzipf package for work/research presented in a
publication, we ask that you please cite:

YOUR last NAME, INITIAL YEAR
https://doi.org/10.21105/jois.02317

### BibTeX entry

@article{Khan2020,
    title={pyzipf: A Python package for word count analysis.},
    author={YOUR NAME},
    journal={Journal of Important Software},
    volume={5},
    number={51},
    eid={2317},
    year={2020},
    doi={10.21105/jois.02317},
    url={https://doi.org/10.21105/jois.02317},
}
```

## Summary 

Thousands of people have helped write the software that our Zipf's Law example relies on,
but their work is only useful because they packaged it
and documented how to use it.
Doing this is increasingly recognized as a credit-worthy activity
by universities, government labs, and other organizations,
particularly for research software engineers.
It is also deeply satisfying to make strangers' lives better,
if only in small ways.

## Keypoints

```{include} keypoints/packaging.md
  
```

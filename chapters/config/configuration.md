# Configuring Programs 

> Always be wary of any helpful item that weighs less than its operating manual.
>
> --- Terry Pratchett

In previous chapters we used command-line options to control our scripts and programs.
If they are more complex,
we may want to use up to four layers of configuration:

1.  A system-wide configuration file for general settings.
2.  A user-specific configuration file for personal preferences.
3.  A job-specific file with settings for a particular run.
4.  Command-line options to change things that commonly change.

This is sometimes called **overlay configuration**
because each level overrides the ones above it:
the user's configuration file overrides the system settings,
the job configuration overrides the user's defaults,
and the command-line options overrides that.
This is more complex than most research software needs initially {cite:p}`Xu2015`,
but being able to read a complete set of options from a file
is a big boost to reproducibility.

In this chapter,
we'll explore a number approaches for configuring our Zipf's Law project,
and ultimately decide to apply one of them.
That project should now contain:

```text
zipf/
├── .gitignore
├── CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── Makefile
├── README.md
├── bin
│   ├── book_summary.sh
│   ├── collate.py
│   ├── countwords.py
│   ├── plotcounts.py
│   ├── script_template.py
│   └── utilities.py
├── data
│   ├── README.md
│   ├── dracula.txt
│   └── ...
└── results
    ├── collate.csv
    ├── collate.png
    ├── dracula.csv
    ├── dracula.png
    └── ...
```

> **Be Careful When Applying Settings outside Your Project**
>
> This chapter's examples modify files outside of the Zipf's Law project
> in order to illustrate some concepts.
> If you alter these files while following along,
> remember to change them back later.

## Configuration File Formats 

Programmers have invented far too many formats for configuration files;
rather than creating one of your own,
you should adopt some widely used approach.
One is to write the configuration as a Python module
and load it as if it was a library.
This is clever,
but means that tools in other languages can't process it.

A second option is [Windows INI format](https://software-engineering-group-up.github.io/RSE-UP/chapters/),
which is laid out like this:

```ini
[section1]
key1=value1
key2=value2

[section2]
key3=value3
key4=value4
```

INI files are simple to read and write,
but the format is slowly falling out of use in favor of **YAML**.
A simple YAML configuration file looks like this:

```yaml
# Standard settings for thesis.
logfile: "/tmp/log.txt"
quiet: false
overwrite: false
fonts:
- Verdana
- Serif
```

Here,
the keys `logfile`, `quiet`, and `overwrite`
have the values `/tmp/log.txt`, `false`, and `false` respectively,
while the value associated with the key `fonts`
is a list containing `Verdana` and `Serif`.
For more discussion of YAML, see [Appendix](https://software-engineering-group-up.github.io/RSE-UP/chapters/appendix/yaml.html).

## Matplotlib Configuration 

To see overlay configuration in action,
let's consider a common task in data science:
changing the size of the labels on a plot.
The labels on our *Jane Eyre* word frequency plot are fine for viewing on screen
([Figure Config Jane Eyre Default](configuartion-jane-eyre-default)),
but they will need to be bigger if we want to include the figure in a slideshow or report.

```{figure} ../../figures/config/jane-eyre-default.png
:name: configuration-jane-eyre-default
Configuration example Jane Eyre
```

We could use any of the overlay options described above
to change the size of the labels:

-  Edit the system-wide Matplotlib configuration file
   (which would affect everyone using this computer).
-  Create a user-specific Matplotlib style sheet.
-  Create a job-specific configuration file to set plotting options in `plotcounts.py`.
-  Add some new command-line options to `plotcounts.py` .

Let's consider these options one by one.

## The Global Configuration File 

Our first configuration possibility is to edit the system-wide Matplotlib runtime configuration file, when we import Matplotlib,
it uses this file to set the default characteristics of the plot.
We can find it on our system by running this command:

```python
import matplotlib as mpl
mpl.matplotlib_fname()
```

```text
/Users/amira/anaconda3/lib/python3.7/site-packages/matplotlib/
mpl-data/matplotlibrc
```

In this case the file is located in the Python installation directory (`anaconda3`).
All the different Python packages installed with Anaconda
live in a `python3.7/site-packages` directory,
including Matplotlib.

`matplotlibrc` lists all the default settings as comments.
The default size of the X and Y axis labels is "medium",
as is the size of the tick labels:

```yaml
#axes.labelsize    : medium  ## fontsize of the x and y labels
#xtick.labelsize   : medium  ## fontsize of the tick labels
#ytick.labelsize   : medium  ## fontsize of the tick labels
```

We can uncomment those lines and change the sizes to "large" and "extra large":

```yaml
axes.labelsize     : x-large  ## fontsize of the x and y labels
xtick.labelsize    : large    ## fontsize of the tick labels
ytick.labelsize    : large    ## fontsize of the tick labels
```
and then re-generate the *Jane Eyre* plot with bigger labels
([Figure JE Labels](configuration-jane-eyre-big-labels)):

```python
$ python bin/plotcounts.py results/jane_eyre.csv --outfile
  results/jane_eyre.png
```

```{figure} ../../figures/config/jane-eyre-big-labels.png
:name: configuration-jane-eyre-big-labels
Jane Eyre Config labels
```

This does what we want,
but is usually the wrong approach.
Since the `matplotlibrc` file sets system-wide defaults,
we will now have big labels by default for all plotting we do in the future,
which we may not want.
Secondly,
we want to package our Zipf's Law code and make it available to other people (Chapter [packaging](https://software-engineering-group-up.github.io/RSE-UP/chapters/packaging/packaging.html)).
That package won't include our `matplotlibrc` file,
and we don't have access to the one on their computer,
so this solution isn't as reproducible as others.

A global options file *is* useful, though.
If we are using Matplotlib with **LaTeX** to generate reports
and the latter is installed in an unusual place on our computing cluster,
a one-line change in `matplotlibrc` can prevent a lot of failed jobs.

## The User Configuration File 

If we don't want to change the configuration for everyone,
we can change it for just ourself.
Matplotlib defines several carefully designed styles for plots:

```python
import matplotlib.pyplot as plt
print(plt.style.available)
```

```text
['seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks',
'fivethirtyeight', 'seaborn-whitegrid', 'classic',
'_classic_test', 'fast', 'seaborn-talk', 'seaborn-dark-palette',
'seaborn-bright', 'seaborn-pastel', 'grayscale',
'seaborn-notebook', 'ggplot', 'seaborn-colorblind',
'seaborn-muted', 'seaborn', 'Solarize_Light2', 'seaborn-paper',
'bmh', 'tableau-colorblind10', 'seaborn-white',
'dark_background', 'seaborn-poster', 'seaborn-deep']
```

In order to make the labels bigger in all of our Zipf's Law plots,
we could create a custom Matplotlib style sheet.
The convention is to store custom style sheets in a `stylelib` sub-directory
in the Matplotlib configuration directory.
That directory can be located by running the following command:

```python
mpl.get_configdir()
```

```text
/Users/amira/.matplotlib
```

Once we've created the new sub-directory:

```bash
$ mkdir /Users/amira/.matplotlib/stylelib
```

we can add a new file called `big-labels.mplstyle`
that has the same YAML format as the `matplotlibrc` file:

```python
axes.labelsize   : x-large  ## fontsize of the x and y labels
xtick.labelsize  : large    ## fontsize of the tick labels
ytick.labelsize  : large    ## fontsize of the tick labels
```

To use this new style,
we would just need to add one line to `plotcounts.py`:

```python
plt.style.use('big-labels')
```

Using a custom style sheet leaves the system-wide defaults unchanged,
and it's a good way to achieve a consistent look across our personal data visualization projects.
However,
since each user has their own `stylelib` directory,
it doesn't solve the problem of ensuring that other people can reproduce our plots.

## Adding Command-Line Options 

A third way to change the plot's properties
is to add some new command-line arguments to `plotcounts.py`.
The `choices` parameter of `add_argument` lets us tell `argparse`
that the user is only allowed to specify a value from a predefined list:

```python
mpl_sizes = ['xx-small', 'x-small', 'small', 'medium',
             'large', 'x-large', 'xx-large']
parser.add_argument('--labelsize', type=str, default='x-large',
                    choices=mpl_sizes,
                    help='fontsize of the x and y labels')
parser.add_argument('--xticksize', type=str, default='large',
                    choices=mpl_sizes,
                    help='fontsize of the x tick labels')
parser.add_argument('--yticksize', type=str, default='large',
                    choices=mpl_sizes,
                    help='fontsize of the y tick labels')
```

We can then add a few lines after the `ax` variable is defined in `plotcounts.py`
to update the label sizes according to the user input:

```python
ax.xaxis.label.set_fontsize(args.labelsize)
ax.yaxis.label.set_fontsize(args.labelsize)
ax.xaxis.set_tick_params(labelsize=args.xticksize)
ax.yaxis.set_tick_params(labelsize=args.yticksize)
```

Alternatively,
we can change the default runtime configuration settings before the plot is created.
These are stored in a variable called `matplotlib.rcParams`:

```python
mpl.rcParams['axes.labelsize'] = args.labelsize
mpl.rcParams['xtick.labelsize'] = args.xticksize
mpl.rcParams['ytick.labelsize'] = args.yticksize
```

Adding extra command-line arguments is a good solution
if we only want to change a small number of plot characteristics.
It also makes our work more reproducible:
if we use a Makefile to regenerate our plots ([Chapter](https://software-engineering-group-up.github.io/RSE-UP/chapters/automate/intro_make.md)),
the settings will all be saved in one place.
However,
`matplotlibrc` has hundreds of parameters we could change,
so the number of new arguments can quickly get out of hand
if we want to tweak other aspects of the plot.

## A Job Control File 

The final option for configuring our plots---the one we will actually adopt in this case---is
to pass a YAML file full of Matplotlib parameters to `plotcounts.py`.
First,
we save the parameters we want to change in a file inside our project directory.
We can call it anything,
but `plotparams.yml` seems like it will be easy to remember.
We'll store it in `bin` with the scripts that will use it:

```yaml
# Plot characteristics
axes.labelsize   : x-large  ## fontsize of the x and y labels
xtick.labelsize  : large    ## fontsize of the tick labels
ytick.labelsize  : large    ## fontsize of the tick labels
```

Because this file is located in our project directory
instead of the user-specific style sheet directory,
we need to add one new option to `plotcounts.py` to load it:

```python
parser.add_argument('--plotparams', type=str, default=None,
                    help='matplotlib parameters (YAML file)')
```

We can use Python's `yaml` library to read that file:

```python
with open('plotparams.yml', 'r') as reader:
    plot_params = yaml.load(reader, Loader=yaml.BaseLoader)
print(plot_params)
```

```text
{'axes.labelsize': 'x-large',
 'xtick.labelsize': 'large',
 'ytick.labelsize': 'large'}
```

and then loop over each item in `plot_params` to update Matplotlib's `mpl.rcParams`:

```python
for (param, value) in param_dict.items():
    mpl.rcParams[param] = value
```

`plotcounts.py` now looks like this:

```python
"""Plot word counts."""

import argparse

import yaml
import numpy as np
import pandas as pd
import matplotlib as mpl
from scipy.optimize import minimize_scalar


def nlog_likelihood(beta, counts):
    # ...as before...


def get_power_law_params(word_counts):
    # ...as before...


def set_plot_params(param_file):
    """Set the matplotlib parameters."""
    if param_file:
        with open(param_file, 'r') as reader:
            param_dict = yaml.load(reader,
                                   Loader=yaml.BaseLoader)
    else:
        param_dict = {}
    for param, value in param_dict.items():
        mpl.rcParams[param] = value


def plot_fit(curve_xmin, curve_xmax, max_rank, beta, ax):
    # ...as before...


def main(args):
    """Run the command line program."""
    set_plot_params(args.plotparams)
    df = pd.read_csv(args.infile, header=None,
                     names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                           method='max')
    ax = df.plot.scatter(x='word_frequency',
                         y='rank', loglog=True,
                         figsize=[12, 6],
                         grid=True,
                         xlim=args.xlim)

    word_counts = df['word_frequency'].to_numpy()
    alpha = get_power_law_params(word_counts)
    print('alpha:', alpha)

    # Since the ranks are already sorted, we can take the last
    # one instead of computing which row has the highest rank
    max_rank = df['rank'].to_numpy()[-1]

    # Use the range of the data as the boundaries
    # when drawing the power law curve
    curve_xmin = df['word_frequency'].min()
    curve_xmax = df['word_frequency'].max()

    plot_fit(curve_xmin, curve_xmax, max_rank, alpha, ax)
    ax.figure.savefig(args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Word count csv file name')
    parser.add_argument('--outfile', type=str,
                        default='plotcounts.png',
                        help='Output image file name')
    parser.add_argument('--xlim', type=float, nargs=2,
                        metavar=('XMIN', 'XMAX'),
                        default=None, help='X-axis limits')
    parser.add_argument('--plotparams', type=str, default=None,
                        help='matplotlib parameters (YAML file)')
    args = parser.parse_args()
    main(args)
```

## Summary 

Programs are only useful if they can be controlled,
and work is only reproducible if those controls are explicit and shareable.
If the number of controls needed is small,
adding command-line options to programs and setting those options in Makefiles
is usually the best solution.
As the number of options grows,
so too does the value of putting options in files of their own.
And if we are installing the software on large systems that are used by many people,
such as a research cluster,
system-wide configuration files let us hide the details
from people who just want to get their science done.

More generally,
the problem of configuring a program illustrates the difference
between "works for me on my machine"
and "works for everyone, everywhere."
From reproducible workflows ([Chapter make](https://software-engineering-group-up.github.io/RSE-UP/chapters/automate/intro_make.html) or [chapter workflows with snakemake](https://software-engineering-group-up.github.io/RSE-UP/chapters/workflows/snakemake.html) to logging ([Section Reporting Errors](https://software-engineering-group-up.github.io/RSE-UP/chapters/errors/error_handling.md#reporting-errors.html)),
this difference influences every aspect of a research software engineer's work.
We don't always have to design for large-scale re-use,
but knowing what it entails allows us to make a conscious, thoughtful choice.

## Keypoints

```{include} ../keypoints/configuration.md

```

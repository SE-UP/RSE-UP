# Snakemake Continued

Snakemake stands out among data processing tools for its versatility and user-friendliness. It empowers researchers to create reproducible and scalable analyses through a human-readable, Python-based language. If you're familiar with the make tool, picking up Snakemake will be a breeze.

## 1. Building the Workflow: The Snakefile

The heart of Snakemake lies in the Snakefile, acting as its build file. It defines a series of rules dictating the workflow's execution. Each rule details how to produce a specific target (output) using its required dependencies (inputs) and the necessary actions.

**In the intro chapter it was enough to call the pipeline from the ZIPF directory as root. For the following guide you need to change the directory for each section** 

### Getting started - Executing Snakemake:

if not already done create a new directory for example as the one provided `snakemake/1_the_snakefile`.
Depending on how you follow the guide the paths for your solution might be different!

By default, running Snakemake without specifying a target prompts it to search for a file named Snakefile. Upon execution, it provides details about the workflow, including the number of steps, involved rules, input and output files.
Therefore we need to create a `snakefile`. For the purpose of the course we start with an example that counts words. 

```python
# Count words in one of the books
rule count_words:
    input: '../../data/dracula.txt'
    output: '../../results/dracula.dat'
    shell: 'python ../wordcount.py ../../data/dracula.txt ../../results/dracula.dat'
```
This is a **build file**, which for Snakemake is called a
Snakefile - a file executed by Snakemake. Note that aside from a few keyword
additions like `rule`, it follows standard Python 3 syntax.

The parts included in to the snakefile are explained as follows:

- **Comments**: Lines starting with # provide explanations and are ignored by Snakemake.

- **Target**: This represents the desired outcome, denoted by a filename (e.g., dracula.dat).

- **Dependencies**: These are files (e.g., data/dracula.txt) needed to create or update the target.

- **Action**: This shell command (e.g., `python wordcount.py data/dracula.txt dracula.dat`) is responsible for generating or updating the target using the dependencies.

*Snakemake follows Python 3 syntax*, introducing keywords like rule. Indentation, whether using tabs or spaces, adheres to Python conventions. A rule combines target, dependencies, and actions, forming a "recipe" for a specific step in the workflow. 

The rule we just created describes how to build the output `dracula.dat` using
the action `python wordcount.py` and the input `dracula.txt`.

Information that was implicit in our shell script - that we are generating a
file called `dracula.dat` and that creating this file requires
`dracula.txt` - is now made explicit by Snakemake's syntax.

Let's first ensure we start from scratch and delete the `.dat`, `.png`, and
`results.txt` files we created earlier:

```bash
rm results/*.dat results/*.png results/results.txt
```

to run snakemake we just have to call it while being in the same directory:
```bash
snakemake
```
Depending on your system the following error message may appear:
```output
Assuming unrestricted shared filesystem usage for local execution.
Error: cores have to be specified for local execution (use --cores N with N being a number >= 1 or 'all')
```

Instead run the following:
```bash
snakemake --cores all
```

By default, Snakemake tells us what it's doing as it executes actions:

```output
Assuming unrestricted shared filesystem usage for local execution.
Building DAG of jobs...
Using shell: /usr/bin/bash
Provided cores: 8
Rules claiming more threads will be scaled down.
Job stats:
job            count
-----------  -------
count_words        1
total              1

Select jobs to execute...
Execute 1 jobs...

[Sun Feb 18 15:30:44 2024]
localrule count_words:
    input: ../data/dracula.txt
    output: ../data/dracula.dat
    jobid: 0
    reason: Missing output files: ../data/dracula.dat
    resources: tmpdir=/tmp

[Sun Feb  18 15:30:44 2024]
Finished job 0.
1 of 1 steps (100%) done
Complete log: .snakemake/log/2024-02-18T153044.591897.snakemake.log
```

If there are errors, check your syntax. Remember, aside from new keywords
like `rule` and `input`, Snakemake follows Python syntax. Let's see if we got
what we expected:

```bash
head -5 results/dracula.dat
```
The output should look like this:

```output
the 8089 4.836269931901207
and 5976 3.5729446301201144
i 4846 2.897337630114136
to 4745 2.836951517724221
of 3748 2.240862863736645
```

If you now try to rerun snakemake the following error will occur: 
```output
Assuming unrestricted shared filesystem usage for local execution.
Building DAG of jobs...
Nothing to be done (all requested files are present and up to date).
```

This basicly means that since the output files are already present the workflow is not re-run. To re-run the snakefile just delete the `.dat`.  

At the same time snakemake checks the last modification time, if `.dat` is younger than the input `.txt` file it won't rerun but if changes where done and save to the `.txt` file and there by make the modification *younger* than the `.dat`, snakemake will re-run the workflow. 

An argument for this approach would be that only rebuilding files when required, makes processing more efficient.  

It also important to note snakefiles do not need to be named `snakefile`, you only need to tell snakemake the name on usage. This means you can have snakefiles for multiple workflows stored in the same location. 

For example using the `-s` flag / option:
```bash
snakemake -s snakefile.txt
```

### Snakefiles as Documentation

By explicitly recording the inputs to and outputs from steps in our analysis and the dependencies between files, Snakefiles act as a type of documentation, reducing the number of things we have to remember.

We can add additional rules to the snakefile i.e.:
```python
rule count_words:
    input: '../../data/dracula.txt'
    output: '../../data/dracula.dat'
    shell: 'python ../wordcount.py ../../data/dracula.txt ../../results/dracula.dat'

rule count_words_moby_dick:
	input: 	'../../data/moby_dick.txt'
	output: '../../results/moby_dick.dat'
	shell: 	'python ../wordcount.py ../../data/moby_dick.txt ../../results/moby.dat'

```

If you run snakemake now, nothing will happen, since snakemake will by default choose the firt rule, ignoring the others. to change this you need to ru the following command instead:

```bash
snakemake --cores all ../../results/moby.dat
```
This will give the following output: 
```output
Assuming unrestricted shared filesystem usage for local execution.
Building DAG of jobs...
Using shell: /usr/bin/bash
Provided cores: 8
Rules claiming more threads will be scaled down.
Job stats:
job                      count
---------------------  -------
count_words_moby_dick        1
total                        1

Select jobs to execute...
Execute 1 jobs...

[Sun Feb  18 16:14:46 2024]
localrule count_words_moby_dick:
    input: ../data/moby_dick.txt
    output: ../data/moby.dat
    jobid: 0
    reason: Missing output files: ../data/moby.dat
    resources: tmpdir=/tmp

[Sun Feb  18 16:14:46 2024]
Finished job 0.
1 of 1 steps (100%) done
Complete log: .snakemake/log/2024-02-18T161446.301442.snakemake.log
```
### Nothing to be Done and MissingRuleException

As you might have seen earlier, if the output file already exists snakemake will return the sentence: '`nothing to be done`'.

But if you try to invoke a rule that does exists, the missing rule exception will be triggered. This looks like this:

```bash
$ snakemake what.dat

MissingRuleException:
No rule to produce what.dat (if you use input functions make sure that they
don't raise unexpected exceptions).
```
You need check the spelling of `what.dat` to fix this. 

### Remove all Rule

One could also create a rule that deletes all output, this could look like the following:

```Python
# delete everything so we can re-run things
rule clean:
    shell: 'rm -f ../../results/*.dat'
```

### Dependencies

Often workflows have dependencies or files that need be created before running a certain rule. In the following example, the rule `dats` relies on the input files dracula.dat and moby_dick.dat.  

```Python
rule dats:
    input:
          '../../results/dracula.dat',
          '../../results/moby_dick.dat'
```

If you run snakemake now, snakemake will first check whether or not the input files exist and if not snakemake will look for rules that generate the input files and run them. It is important to note that dependencies must form a directed acyclic graph. A target cannot depend on a dependency which itself, or one of its dependencies, depends on that target.

The output of 

```bash
snakemake --cores 1 dats
```
will look like this 
```Output
Provided cores: 1
Rules claiming more threads will be scaled down.
Job counts:
        count   jobs
        1       count_words
        1       count_words_moby_dick
        1       dats
        3

rule count_words_moby_dick:
    input: ../../data/moby_dick.txt
    output: ../../results/moby_dick.dat
    jobid: 1

Finished job 1.
1 of 3 steps (33%) done

rule count_words:
    input: ../../data/dracula.txt
    output: ../../results/dracula.dat
    jobid: 2

Finished job 2.
2 of 3 steps (67%) done

localrule dats:
    input: ../../data/dracula.dat, ../../data/moby_dick.dat
    jobid: 0

Finished job 0.
3 of 3 steps (100%) done
```

While the snakefile should look as follows:
```Python
rule dats:
     input:
         '../../results/dracula.dat',
         '../../results/moby_dick.dat'

# delete everything so we can re-run things
rule clean:
    shell:  'rm -f ../../results/*.dat'

# Count words in one of the books
rule count_words:
    input: 	'../../data/dracula.txt'
    output: '../../results/dracula.dat'
    shell: 	'python ../wordcount.py ../../data/dracula.txt ../../results/dracula.dat'

rule count_words_moby_dick:
    input: 	'../../data/moby_dick.txt'
    output: '../../results/moby_dick.dat'
    shell: 	'../python wordcount.py ../../data/moby_dick.txt ../../results/moby_dick.dat'
```
the directed graph of the dependencies looks like this: 

```{figure} ../figures/snakemake/dats_graph_1.svg
:name: dats graph
Dats Graph
```
### Debugging

At this point, it becomes important to see what snakemake is doing behind the scenes. What commands is snakemake actually running? Snakemake has a special option (-p), that prints every command it is about to run. Additionally, we can also perform a dry run with -n. A dry run does nothing, and simply prints out commands instead of actually executing them. Very useful for debugging!

```bash
snakemake clean
snakemake -n -p dracula.dat

```

```Output
Building DAG of jobs...
Job counts:
	count	jobs
	1	count_words
	1

rule count_words:
    input: ../../data/dracula.txt
    output: ../../results/dracula.dat
    jobid: 0 

python ../wordcount.py ../../data/dracula.txt ../../results/dracula.dat
Job counts:
	count	jobs
	1	count_words
	1
This was a dry-run (flag -n). The order of jobs does not reflect the order of execution.
```
**Before you continue with the book below, it is advised to first look at the exercise: [Write two new rules](https://se-up.github.io/RSE-UP/exercises/snakemake.html) since it would come in handy for the next section.** 

## 2 Wildcards

When you have completed the exercise, you notice that there is a lot of duplications and repetitions. It is always good practice to not repeat yourself. 
Let's start from the top on go rule by rule and refactor the snakefile.
```Python
rule zipf_test:
    input: '../../results/dracula.dat','../../results/frankenstein.dat', '../../results/sherlock_holmes.dat'
    output: '../../results/results.txt'
    shell: 'python ../zipf_test.py ../../results/frankenstein.dat ../../results/dracula.dat ../../results/sherlock_holmes.dat > ../../results/wildcards_results.txt'

```
Here we can shorten the shell command by using variables. 
This could look like the following, were we add an `{input}` and `{output}` **wildcards**.

```Python
rule zipf_test:
    input: '../../results/dracula.dat', '../../results/frankenstein.dat', '../../results/sherlock_holmes.dat'
    output: '../../results/wildcards_zipf_results.txt'
    shell: 'python ../zipf_test.py {input} > {output}'
  
```

### Handling dependencies differently

For many rules, we will need to make finer distinctions between inputs. It is not always appropriate to pass all inputs as a lump to your action. For example, our rules for `.dat` use their first (and only) dependency specifically as the input file to `wordcount.py`. If we add additional dependencies (as we will soon do) then we don't want these being passed as input files to `wordcount.py`: it expects just one input file.

Let's see this in action. We need to add `wordcount.py as a dependency of each of our data files so that the rules will be executed if the script changes. In this case, we can use `{input[0]}` to refer to the first dependency, and `{input[1]}` to refer to the second:

```Python
rule count_words:
    input: '../wordcount.py', '../../data/dracula.txt'
    output: '../../results/dracula.dat'
    shell: 'python {input[0]} {input[1]} {output}'
```

Alternatively, we can name our dependencies:
```Python
rule count_words_frankenstein:
    input:
        cmd='wordcount.py',
        book='data/frankenstein.txt'
    output: 'frankenstein.dat'
    shell: 'python {input.cmd} {input.book} {output}'
```

Let's mark `wordcount.py` as updated, and re-run the pipeline:

```bash
touch wordcount.py
snakemake
```
```Output
Assuming unrestricted shared filesystem usage for local execution.
Building DAG of jobs...
Using shell: /usr/bin/bash
Provided cores: 8
Rules claiming more threads will be scaled down.
Job stats:
job                         count
------------------------  -------
count_words                     1
count_words_frankenstein        1
count_words_sherlock            1
zipf_test                       1
total                           4

Select jobs to execute...
Execute 3 jobs...

localrule count_words:
    input: ../wordcount.py, ../../data/dracula.txt
    output: ../../results/dracula.dat
    jobid: 1
    reason: Missing output files: ../../results/dracula.dat
    resources: tmpdir=/tmp

localrule count_words_frankenstein:
    input: ../wordcount.py, ../../data/frankenstein.txt
    output: ../../results/frankenstein.dat
    jobid: 2
    reason: Missing output files: ../../results/frankenstein.dat
    resources: tmpdir=/tmp

localrule count_words_sherlock:
    input: ../wordcount.py, ../../data/sherlock_holmes.txt
    output: ../../results/sherlock_holmes.dat
    jobid: 3
    reason: Missing output files: ../../results/sherlock_holmes.dat
    resources: tmpdir=/tmp

Finished job 2.
1 of 4 steps (25%) done

Finished job 3.
2 of 4 steps (50%) done

Finished job 1.
3 of 4 steps (75%) done
Select jobs to execute...
Execute 1 jobs...

localrule zipf_test:
    input: ../../results/dracula.dat, ../../results/frankenstein.dat, ../../results/sherlock_holmes.dat
    output: ../../results/wildcards_zipf_results.txt
    jobid: 0
    reason: Missing output files: ../../results/wildcards_zipf_results.txt; Input files updated by another job: ../../results/frankenstein.dat, ../../results/dracula.dat, ../../results/sherlock_holmes.dat
    resources: tmpdir=/tmp

Finished job 0.
4 of 4 steps (100%) done
Complete log: .snakemake/log/2024-04-02T154614.819856.snakemake.log


```
In case a *.dat file such as `dracula.dat` does already exist, that pipeline will not be triggered.  

Intuitively, we should also add `wordcount.py` as dependency for `results.txt`, as the final table should be rebuilt if we remake the .dat files. However, it turns out we don't have to! Let's see what happens to `results.txt` when we update `wordcount.py`:
```Bash
touch wordcount.py # or make a change / save it so that it has a newer date
snakemake ../../results/results.txt
```

The whole pipeline is triggered, even the creation of the `results.txt` file! To understand this, note that according to the dependency graph, `results.txt` depends on the `.dat` files. The update of `wordcount.py` triggers an update of the *.dat files. Thus, Snakemake sees that the dependencies (the `.dat` files) are newer than the target file (`results.txt`) and it therefore recreates `results.txt`. This is an example of the power of Snakemake: updating a subset of the files in the pipeline triggers rerunning the appropriate downstream steps.

## 3 Patterns

Our Snakefile still has a ton of repeated content. The rules for each .dat file all follow a consistent pattern. We can replace these rules with a single pattern rule which can be used to build any `.dat` file from a `.txt` file in `data/`:

```Python
rule count_words:
    input:
        cmd='wordcount.py',
        book='data/{book}.txt'
    output: '{book}.dat'
    shell: 'python {input.cmd} {input.book} {output}'
```

Here `{book}` is an arbitrary wildcard that we can use as a placeholder for any generic book to analyze. Note that we don't have to use `{book}` as the name of our *wildcard* - it can be anything we want!

This rule can be interpreted as: "In order to build a file named `[something].dat` (the target) find a file named `data/[that same something].txt` (the dependency) and run `wordcount.py [the dependency] [the target]`."

### Update your Snakefile now
Replace all your `count_words` rules with the given pattern rule now.

Let's test the new pattern rule. We use the -p option to show that it is running things correctly:

```bash
snakemake clean
snakemake -p dats
```

We should see the same output as before. Note that we can still use snakemake to build individual `.dat` targets as before, and that our new rule will work no matter what stem is being matched.

```bash
snakemake -p dracula.dat
```

which gives the output below:

```Output
Provided cores: 1
Rules claiming more threads will be scaled down.
Job counts:
	count	jobs
	1	count_words
	1

rule count_words:
    input: ../wordcount.py, ../../data/dracula.txt
    output: ../../results/dracula.dat
    jobid: 0
    wildcards: file=dracula

python ../wordcount.py ../../data/dracula.txt ../../results/dracula.dat
Finished job 0.
1 of 1 steps (100%) done
```

### Using wildcards continued

Our arbitrary wildcards like `{book}` can only be used in input: and output: fields. They cannot be used directly in actions. If you need to refer to the current value of a wildcard in an action you need to qualify it with wildcards.. For example: `{wildcards.file}.`

Running Pattern Rules
Note that although Snakemake lets you execute a non-pattern rule by name, such as snakemake clean, you cannot execute a pattern rule this way:

```bash
snakemake count_words
```

```Output
Building DAG of jobs...
WorkflowError:
Target rules may not contain wildcards. Please specify concrete files or a rule without wildcards.

```


As the error message indicates, you need to ask for specific files. For example,
```bash
 snakemake ../../results/dracula.dat.

```

Our Snakefile is now much shorter and cleaner:
```Python
# generate summary table
rule zipf_test:
    input: '../../zipf_test.py', '../../results/sherlock_holmes.dat', '../../results/frankenstein.dat', '../../results/dracula.dat'
    output: '../../results/wildcard_2_results.txt'
    shell: 'python {input[0]} {input[1]} {input[2]} {input[3]} > {output}'

rule dats:
     input: '../../results/dracula.dat', '../../results/frankenstein.dat', '../../results/sherlock_holmes.dat'

# delete everything so we can re-run things
rule clean:
    shell: 'rm -f ../../results/*.dat ../../results/wild*.txt'

# count words in one of our "books"
rule count_words:
    input:
        cmd='../wordcount.py',
        book='../../data{book}.txt'
    output: '../../results{book}.dat'
    shell: 'python {input.cmd} {input.book} {output}'
```

Now all that is left to do is update your snakefile.

## 4 Snakefiles are Python code


Despite our efforts, our pipeline still has repeated content,
for instance the names of input and output files
(*dependencies and targets*).
Our `zipf_test` rule, for instance, is extremely clunky.
What happens if we want to analyze `data/frankenstein.txt` as well?

We'd have to update everything!

```Python
rule zipf_test:
    input:  'zipf_test.py', 'frankenstein.dat', 'jane_eyre.dat', 'dracula.dat'
    output: 'results.txt'
    shell:  'python {input[0]} {input[1]} {input[2]} {input[3]} > {output}'
```


Let's try to improve this rule. One thing you've probably noticed is that all
of our rules are using Python strings. Other data structures work too - let's
try a list:

```Python

rule zipf_test:
    input:
        cmd='../zipf_test.py',
        dats=['../../results/dracula.dat', '../../results/sherlock_holmes.dat', '../../results/frankenstein.dat']
    output: '../../results/results.txt'
    shell: 'python {input.cmd} {input.dats} > {output}'


```


After updating your rule, run `snakemake clean` and `snakemake -p` to confirm
that the pipeline still works.

### Named Dependencies
***Note that we also had to switch to using named dependencies.  This was required since the first input, `zipf_text.py`, **should not** be in the list of input files.***

### Inputs: named vs indexed?
***Having seen the use of both named and indexed dependencies, which approach do you prefer?
Which approach do you think leads to Snakefiles that are easier to read and maintain?***

The use of a list for the input files illustrates a key feature of Snakemake:
**Snakefiles are just Python code.**

We can make our list into a variable to demonstrate this. Let's create the
global variable DATS and use it in our `zipf_test` and `dats` rules:

```Python
DATS=['../../results/frankenstein.dat', '../../results/sherlock_holmes.dat', '../../results/dracula.dat']

# generate summary table
rule zipf_test:
    input:
        cmd='zipf_test.py',
        dats=DATS
    output: 'results.txt'
    shell: 'python {input.cmd} {input.dats} > {output}'

rule dats:
    input: DATS
```

Great! One more step towards reducing code duplication. Now there is just
one place to update the list of files to process.

#### Update your Snakefile
Update your Snakefile with the `DATS` global variable.

Try recreating both the `dats` and `results.txt` targets
(run `snakemake clean` in between).

#### Solution
See [Solution on Github](https://github.com/SE-UP/RSE-UP/tree/main/zipf/snakemake/4_snakefiles_python) for the full Snakefile. Otherwise, just refer to the code extracts above and modify your own file.

### When are Snakefiles executed?

The last example illustrated that we can use arbitrary Python code in our Snakefile. It's
important to understand when this code gets executed. Let's add a print
statement to the top of our Snakefile:

```Python
print('Snakefile is being executed!')

DATS=['frankenstein.dat', 'jane_eyre.dat', 'dracula.dat']

# generate summary table
rule zipf_test:
    input:
# more output below
```

Now let's clean up our workspace with `snakemake clean`:

```bash
snakemake clean
```

```Output
Snakefile is being executed!
Provided cores: 1
Rules claiming more threads will be scaled down.
Job counts:
	count	jobs
	1	clean
	1

rule clean:
    jobid: 0

Finished job 0.
1 of 1 steps (100%) done
```

Now let's re-run the pipeline...

```bash
snakemake
```


```Output
Snakefile is being executed!
Provided cores: 1
Rules claiming more threads will be scaled down.
Job counts:
	count	jobs
	3	count_words
	1	zipf_test
	4

rule count_words:
    input: wordcount.py, data/jane_eyre.txt
    output: data/jane_eyre.dat
    jobid: 3
    wildcards: file=last

Finished job 3.
1 of 4 steps (25%) done

rule count_words:
    input: wordcount.py, data/frankenstein.txt
    output: data/frankenstein.dat
    jobid: 1
    wildcards: file=abyss

Finished job 1.
2 of 4 steps (50%) done

rule count_words:
    input: wordcount.py, data/dracula.txt
    output: data/dracula.dat
    jobid: 2
    wildcards: file=isles

Finished job 2.
3 of 4 steps (75%) done

rule zipf_test:
    input: zipf_test.py, data/frankenstein.dat, data/jane_eyre.dat, data/dracula.dat
    output: results.txt
    jobid: 0

Finished job 0.
4 of 4 steps (100%) done
```


Let's do a dry-run:

```bash
snakemake -n
```

```Output
Snakefile is being executed!
Nothing to be done.
```

In every case, the `print()` statement ran before any of the actual pipeline
code. What we can take away from this is that Snakemake executes the entire
Snakefile every time we run `snakemake`, even for a dry-run. Because of this
we need to be careful and only put tasks that do "real work" (changing files
on disk) inside rules.

Common tasks, such as building lists of input files that will be reused in
multiple rules are a good fit for Python code that lives outside the rules.

### Is your `print` output appearing last?
>
> On some systems, output is buffered. This means that nothing is actually output
> until the buffer is full. While this is more efficient, it can delay the output
> from the `print` command.
>
> In my testing on Windows using the combination of Git Bash and Anaconda, the
> `print` statement is buffered, resulting in the text printing to the terminal
> ***after*** all the Snakemake output. If this is happening to you, tell the
> `print` statement to force a flush of the output buffer:
>
> ```Python
> print("Snakefile is being executed!", flush=True)
> ```
> 
>
> You should then see the printed text before the Snakemake output, confirming
> that this code executes first.


## Using functions in Snakefiles

In our example here, we only have 4 books (and just 3 are being processed).
But what if we had 700 books to be processed? It would be a massive effort to
update our `DATS` variable to add the name of every single book's
corresponding `.dat` filename.

Fortunately, Snakemake ships with several functions that make working with
large numbers of files much easier. The two most helpful ones are
`glob_wildcards()` and `expand()`. Let's start a Python session to see how
they work.

### This can be done in any Python environment

> You can use any Python environment for the following code exploring `expand()`
> and `glob_wildcards()`. The standard Python interpreter, ipython, or
> a Jupyter Notebook. It's up to personal preference and what you have installed.
>
> On Windows, calling `python` from Git Bash does not always work. It is better
> to use the Anaconda start menu entries to run a Python prompt and then run
> `python` from there.
>
> Make sure you change to your Snakefile directory before launching Python.


In this example, we will import these Snakemake functions directly in our
Python session.

### Importing is not required in a Snakefile
>
> You don't need to import the Snakemake utility functions within your Snakefile - they are
> always imported for you.


So in your chosen Python environment, run the following:

```Python
from snakemake.io import *
```


### Generating file names with expand()

The first function we'll use is `expand()`. `expand()` is used quite
literally, to expand snakemake wildcards into a set of filenames:

```Python
expand('folder/{wildcard1}_{wildcard2}.txt', wildcard1=['a', 'b', 'c'], wildcard2=[1, 2, 3])
```

```Output
['folder/a_1.txt',
 'folder/a_2.txt',
 'folder/a_3.txt',
 'folder/b_1.txt',
 'folder/b_2.txt',
 'folder/b_3.txt',
 'folder/c_1.txt',
 'folder/c_2.txt',
 'folder/c_3.txt']
```

In this case, `expand()` created every possible combination of filenames from
the two wildcards. Nice! Of course, this still leaves us needing to get the
values for `wildcard1` and `wildcard2` in the first place.

### Get wildcard values with glob_wildcards()

To get a set of wildcards from a list of files, we can use the
`glob_wildcards()` function. It matches the given pattern against files
on the file system, returning a named tuple containing all the matches. Let's
try grabbing all of the book titles in our `books` folder:

```Python
glob_wildcards('data/{example}.txt')
```

```Output
Wildcards(example=['dracula', 'jane_eyre', 'frankenstein', 'sherlock_holmes'])
```

In this case, there is only one wildcard, `{example}`.
We can extract the values for name by getting the `example`
property from the output of `glob_wildcards()`:

```Python
glob_wildcards('data/{example}.txt').example
```
```Output
['dracula', 'jane_eyre', 'frankenstein', 'sherlock_holmes']
```


### Using Python code as actions

One very useful feature of Snakemake is the ability to execute Python code
instead of just shell commands. Instead of `shell:` as an action, we can use
`run:` instead.

Add the following to your snakefile:

```Python
# at the top of the file
import glob
import os

# add as the last rule (we don't want it to be the default)
rule print_book_names:
    run:
        print('These are all the book names:')
        for book in glob.glob('../../data/*.txt'):
            print(book)
```

Upon execution of the corresponding rule, Snakemake runs our Python code
in the `run:` block:

```Bash
snakemake --quiet print_book_names
```

```Output
Provided cores: 1
Rules claiming more threads will be scaled down.
Job counts:
	count	jobs
	1	print_book_names
	1

rule print_book_names:
    jobid: 0

These are all the book names:
data/dracula.txt
data/jane_eyre.txt
data/frankenstein.txt
data/sherlock_holmes.txt
Finished job 0.
1 of 1 steps (100%) done
```

> Note the `--quiet` option
>
> `--quiet` or `-q` suppresses a lot of the rule progress output from Snakemake.
> This can be useful when you just want to see your own output.

### Cleaning House

It is common practice to have a `clean` rule that deletes all intermediate
and generated files, taking your workflow back to a blank slate.

We already have a `clean` rule, so now is a good time to check that it
removes all intermediate and output files. First do a `snakemake all` followed
by `snakemake clean`. Then check to see if any output files remain and add them
to the clean rule if required.


## Next steps

It would be best if you start doing some of the [exercises](https://se-up.github.io/RSE-UP/exercises/snakemake.html) now,
especially the exercises related to working with files and outputs before going to the next section!

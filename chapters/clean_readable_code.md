# Writing Readable Code 

Nothing in biology makes sense except in light of evolution {cite:p}`Dobz1973`.
Similarly, nothing in software development makes sense except in light of human psychology.
This is particularly true when we look at programming style.
Computers don't need to understand programs in order to execute them,
but people do if they are to create, debug, and extend them.

Throughout this book we have written code to analyze word counts in classic novels
using good Python style.
This appendix discusses the style choices we made,
presents guidelines for good Python programming style,
and introduces some language features that can make programs more flexible and more readable.

## Python Style 

The single most important rule of style is to be consistent,
both internally and with other programs {cite:p}`Kern1999`.
Python's standard style is called [PEP-8](https://www.python.org/dev/peps/pep-0008/);
the acronym "PEP" is short for "Python Enhancement Proposal,"
and PEP-8 lays out the rules that Python's own libraries use.
Some of its rules are listed below,
along with others borrowed from "[Code Smells and Feels]( https://github.com/jennybc/code-smells-and-feels)."

### Spacing

**Always indent code blocks using 4 spaces, and use spaces instead of tabs.**

Python doesn't actually require consistent indentation
so long as each block is indented the same amount,
which means that this is legal:

```python
def transpose(original):
  result = Matrix(original.numRow, original.numCol)
  for row in range(original.numRow):
              for col in range(original.numCol):
               result[row, col] = original[col, row]
  return result
```

The same block of code is much more readable when written as:

```python
def transpose(original):
    result = Matrix(original.numRow, original.numCol)
    for row in range(original.numRow):
        for col in range(original.numCol):
            result[row, col] = original[col, row]
    return result
```

The use of 4 spaces is a compromise between 2
(which we find perfectly readable, but some people find too crowded)
and 8
(which most people agree uses up too much horizontal space).
As for the use of spaces rather than tabs,
the original reason was that the most common interpretation of tabs
by the editors of the 1980s was 8 spaces,
which again was more than most people felt necessary.
Today,
almost all editors will auto-indent or auto-complete when the tab key is pressed
(or insert spaces, if configured to do so),
but the legacy of those ancient times lives on.

**Do not put spaces inside parentheses.**

Write `(1+2)` instead of `( 1+2 )`.
This applies to function calls as well:
write `max(a, b)` rather than `max( a, b )`.
(We will see a related rule when we discuss default parameter values
in Section [Python Features](https://se-up.github.io/RSE-UP/chapters/clean_readable_code.html#python-features).)

**Always use spaces around comparisons like `>` and `<=`.**

Python automatically interprets `a+b<c+d` as `(a+b)<(c+d)`,
but that's a lot of punctuation crowded together.
Using spaces around comparison operators makes it easier to see
what's being compared to what.
However,
we should use our own judgment for spacing around arithmetic operators like `+` and `/`.
For example,
`a+b+c` is perfectly readable,
but

```python
substrate[i, j] + overlay[i, j]
```

is easier for the eye to follow than the spaceless:

```python
substrate[i, j]+overlay[i, j]
```

Most programmers would also write:

```python
a*b + c*d
```

instead of:

```python
a*b+c*d
```

or:

```python
(a*b)+(c*d)
```

Adding spaces makes simple expressions more readable,
but does not change the way Python interprets them---when it encounters `a * b+c`,
for example,
Python still does the multiplication before the addition.

**Put two blank lines between each function definition.**

This helps the eye see where one ends and the next begins,
though the fact that functions always start in the first column helps as well.

**Add an empty line at the end of the script.**

Ending a file in a newline character is required for some other programming languages.
Although it's not required for Python code to function,
it does make it easier to view and edit code.

### Naming

**Use `ALL_CAPS_WITH_UNDERSCORES` for global variables.**

This convention is inherited from C, which was used to write the first version of Python.
In that language, upper case was used to indicate a constant whose value couldn't be modified; Python doesn't enforce that rule,
but `SHOUTING_AT_PROGRAMMERS` helps remind them that
some things shouldn't be messed with.

**Use `lower_case_with_underscores` for the names of functions and variables.**

Research on naming conventions has produced mixed results {cite:p}`Bink2012`; {cite:p}`Scha2018` but Python has (mostly) settled on underscored names for most things. 
This style is called **snake case** or **pothole case**;
we should only use **CamelCase** for classes,
which are outside the scope of this lesson.

**Avoid abbreviations in function and variable names.**

Abbreviations and acronyms can be ambiguous
(does `xcl` mean "Excel", "exclude", or "excellent"?),
and can be hard for non-native speakers to understand.
Following this rule doesn't necessarily require more typing:
a good programming editor will **auto-complete** names for us.

**Use short names for short-lived local variables and longer names for things with wider scope.**

Using `i` and `j` for loop indices is perfectly readable
provided the loop is only a few lines long {cite:p}`Beni2017`.
Anything that is used at a greater distance
or whose purpose isn't immediately clear
(such as a function) should have a longer name.

**Do not comment and uncomment sections of code to change behavior.**

If we need to do something in some runs of the program and not in others,
use an `if` statement to enable or disable that block of code:
it eliminates the risk of accidentally commenting out one too many lines.
If the lines we were removing or commenting out print debugging information,
we should replace them with logging calls (Section [Reporting Errors](https://se-up.github.io/RSE-UP/chapters/error_handling.html#reporting-errors)).
If they are operations that we want to execute,
we can add a configuration option (Chapter [Configuration](https://se-up.github.io/RSE-UP/chapters/configuration.html)),
and if we are sure we don't need the code,
we should take it out completely:
we can always get it back from version control
([Exercise on recovering older file version](https://se-up.github.io/RSE-UP/exercises/version_control.html#recovering-older-versions-of-a-file)).

## Order 

The order of items in each file should be:

-   The **shebang** line (because it has to be first to work).
-   The file's documentation string (Section [Python Documentation](https://se-up.github.io/RSE-UP/chapters/python_building_cli.html#documentation)).
-   All of the `import` statements, one per line.
-   Global variable definitions
    (especially things that would be constants in languages that support them).
-   Function definitions.
-   If the file can be run as a program,
    the `if __name__ == '__main__'` statement discussed in
    Section [Writing your own modules](https://se-up.github.io/RSE-UP/chapters/python_building_cli.html#writing-our-own-modules).

That much is clear,
but programmers disagree (strongly) on whether high-level functions should come first or last,
i.e.,
whether `main` should be the first function in the file or the last one.
Our scripts put it last,
so that it is immediately before the check on `__name__`.
Wherever it goes,
`main` tends to follow one of three patterns:

1.  Figure out what the user has asked it to do (Chapter [Configuration](https://se-up.github.io/RSE-UP/chapters/configuration.html)).
2.  Read all input data.
3.  Process it.
4.  Write output.

or:

1.  Figure out what the user has asked for.
2.  For each input file:
    1.  Read.
    2.  Process.
    3.  Write file-specific output (if any).
3.  Write summary output (if any).

or:

1.  Figure out what the user has asked for.
2.  Repeatedly:
    1.  Wait for user input.
    2.  Do what the user has asked.
3.  Exit when a "stop" command of some sort is received.

Each step in each of the outlines above usually becomes a function.
Those functions depend on others,
some of which are written to break code into comprehensible chunks and are then called just once,
others of which are utilities that may be called many times from many different places.

We put all of the single-use functions in the first half of the file
in the order in which they are likely to be called,
and then put all of the multi-use utility functions in the bottom of the file in alphabetical order.
If any of those utility functions are used by other scripts or programs,
they should go in a file of their own (Section [Collating Results](https://se-up.github.io/RSE-UP/chapters/python_building_cli.html#collating-results)).

In fact,
this is a good practice even if those functions are only used by one program,
since it signals even more clearly which are specific to this program
and which are likely to be reused elsewhere.
This is why we create `collate.py` in Section [Collating](https://se-up.github.io/RSE-UP/chapters/python_building_cli.html#collating-results):
we could have kept all of our code in `countwords.py`,
but collating felt like something we might want to do separately.

## Checking Style 

Checking that code conforms to guidelines like PEP-8 would be time consuming
if we had to do it manually,
but most languages have tools that will check style rules for us.
These tools are often called **linters**, after an early tool called [`lint`](https://en.wikipedia.org/wiki/Lint_(software)) that found lint (or fluff) in C code.

Python's linter used to be called `pep8` and is now called `pycodestyle`.
To see how it works,
let's look at this program,
which is supposed to count the number of **stop words** in a document:

```python
stops = ['a', 'A', 'the', 'The', 'and']

def count(ln):
    n = 0
    for i in range(len(ln)):
        line = ln[i]
        stuff = line.split()
        for word in stuff:
            # print(word)
            j = stops.count(word)
            if (j > 0) == True:
                n = n + 1
    return n

import sys

lines = sys.stdin.readlines()
# print('number of lines', len(lines))
n = count(lines)
print('number', n)
```

When we run:

```bash
$ pycodestyle count_stops.py
```

it prints:

```text
src/style/count_stops_before.py:3:1:
E302 expected 2 blank lines, found 1
src/style/count_stops_before.py:11:24:
E712 comparison to True should be
'if cond is True:' or 'if cond:'
src/style/count_stops_before.py:12:13:
E101 indentation contains mixed spaces and tabs
src/style/count_stops_before.py:12:13:
W191 indentation contains tabs
src/style/count_stops_before.py:15:1:
E305 expected 2 blank lines after class or function definition,
  found 1
src/style/count_stops_before.py:15:1:
E402 module level import not at top of file
```

which tells us that:

-   We should use two blank lines before the function definition on line 3
    and after it on line 15.
-   Using `== True` or `== False` is redundant
    (because `x == True` is the same as `x`
    and `x == False` is the same as `not x`).
-   Line 12 uses tabs instead of just spaces.
-   The `import` on line 15 should be at the top of the file.

Fixing these issues gives us:

```python
import sys


stops = ['a', 'A', 'the', 'The', 'and']


def count(ln):
    n = 0
    for i in range(len(ln)):
        line = ln[i]
        stuff = line.split()
        for word in stuff:
            # print(word)
            j = stops.count(word)
            if j > 0:
                n = n + 1
    return n


lines = sys.stdin.readlines()
# print('number of lines', len(lines))
n = count(lines)
print('number', n)
```

## Refactoring 

Once a program gets a clean bill of health from `pycodestyle`,
it's worth having a human being look it over and suggest improvements.
To **refactor** code
means to change its structure without changing what it does,
like simplifying an equation.
It is just as much a part of programming as writing code in the first place:
nobody gets things right the first time {cite:p}`Bran1995`,
and needs or insights can change over time.

Most discussions of refactoring focus on **object-oriented programming**
but many patterns can and should be used to clean up **procedural** code.
Knowing a few of these patterns helps us create better software
and makes it easier to communicate with our peers.

### Do not repeat values

The first and simplest refactoring is "replace value with name."
It tells us to replace magic numbers with names,
i.e., to define constants.
This can seem ridiculous in simple cases
(why define and use `inches_per_foot` instead of just writing 12?).
However,
what may be obvious to us when we're writing code won't be obvious to the next person,
particularly if they are working in a different context
(most of the world uses the metric system and doesn't know how many inches are in a foot).
It is also a matter of habit:
if we write numbers without explanation in our code for simple cases,
we are more likely to do so in complex cases,
and more likely to regret it afterward.

Using names instead of raw values also makes it easier to understand code when we read it aloud,
which is always a good test of its style.
Finally,
a single value defined in one place is much easier to change
than a bunch of numbers scattered throughout our program.
We may not think we will have to change it,
but then people want to use our software on Mars and we discover that constants aren't {cite:p}`Mak2006`.

```python
# ...before...
seconds_elapsed = num_days * 24 * 60 * 60
```

```python
# ...after...
SECONDS_PER_DAY = 24 * 60 * 60
# ...other code...
seconds_elapsed = num_days * SECONDS_PER_DAY
```

### Do not repeat calculations in loops

It's inefficient to calculate the same value over and over again.
It also makes code less readable:
if a calculation is inside a loop or a function,
readers will assume that it might change each time the code is executed.

Our second refactoring,
"hoist repeated calculation out of loop,"
tells us to move the repeated calculation out of the loop or function.
Doing this signals that its value is always the same.
And naming that common value helps readers understand what its purpose is.

```python
# ...before...
for sample in signals:
    output.append(2 * pi * sample / weight)
```

```python
# ...after...
scaling = 2 * pi / weight
for sample in signals:
    output.append(sample * scaling)
```

### Replace tests with flags to clarify repeated tests

Novice programmers frequently write conditional tests like this:

```python
if (a > b) == True:
    # ...do something...
```

The comparison to `True` is unnecessary because `a > b` is a Boolean value
that is itself either `True` or `False`.
Like any other value,
Booleans can be assigned to variables,
and those variables can then be used directly in tests:

```python
was_greater = estimate > 0.0
# ...other code that might change estimate...
if was_greater:
    # ...do something...
```

This refactoring is "replace repeated test with flag."
Again,
there is no need to write `if was_greater == True`:
that always produces the same result as `if was_greater`.
Similarly,
the equality tests in `if was_greater == False` is redundant:
the expression can simply be written `if not was_greater`.
Creating and using a **flag** instead of repeating the test
is therefore like moving a calculation out of a loop:
even if that value is only used once,
it makes our intention clearer.

```python
# ...before...
def process_data(data, scaling):
    if len(data) > THRESHOLD:
        scaling = sqrt(scaling)
    # ...process data to create score...
    if len(data) > THRESHOLD:
        score = score ** 2
```

```python
# ...after...
def process_data(data, scaling):
    is_large_data = len(data) > THRESHOLD
    if is_large_data:
        scaling = sqrt(scaling)
    # ...process data to create score...
    if is_large_data:
        score = score ** 2
```

If it takes many lines of code to process data and create a score,
and the test then needs to change from `>` to `>=`,
we are more likely to get the refactored version right the first time,
since the test only appears in one place and its result is given a name.

### Use in-place operators to avoid duplicating expression

An **in-place operator**,
sometimes called an **update operator**,
does a calculation with two values
and overwrites one of the values.
For example,
instead of writing:

```python
step = step + 1
```

we can write:

```python
step += 1
```

In-place operators save us some typing.
They also make the intention clearer,
and most importantly,
they make it harder to get complex assignments wrong.
For example:

```python
samples[least_factor,
        max(current_offset, offset_limit)] *= scaling_factor
```

is less difficult to read than the equivalent expression:

```python
samples[least_factor, max(current_offset, offset_limit)] = \
    scaling_factor * samples[least_factor,
                             max(current_limit,
                                 offset_limit)]
```

(The proof of this claim is that you probably didn't notice
that the long form uses different expressions to index `samples`
on the left and right of the assignment.)
The refactoring "use in-place operator" does what its name suggests:
converts normal assignments into their briefer equivalents.

```python
# ...before...
for least_factor in all_factors:
    samples[least_factor] = \
        samples[least_factor] * bayesian_scaling
```

```python
# ...after...
for least_factor in all_factors:
    samples[least_factor] *= bayesian_scaling
```

### Handle special cases first

A **short circuit test** is a quick check to handle a special case,
such as checking the length of a list of values
and returning `math.nan` for the average if the list is empty.
"Place short circuits early" tells us to put short-circuit tests near the start of functions
so that readers can mentally remove special cases from their thinking
while reading the code that handles the usual case.

```python
# ...before...
def rescale_by_average(values, factors, weights):
    a = 0.0
    for (f, w) in zip(factors, weights):
        a += f * w
    if a == 0.0:
        return
    a /= len(f)
    if not values:
        return
    else:
        for (i, v) in enumerate(values):
            values[i] = v / a
```

```python
# ...after...
def rescale_by_average(values, factors, weights):
    if (not values) or (not factors) or (not weights):
        return
    a = 0.0
    for (f, w) in zip(factors, weights):
        a += f * w
    a /= len(f)
    for (i, v) in enumerate(values):
        values[i] = v / a
```


> **Return Consistently**
>
> PEP-8 says, "Be consistent in `return` statements,"
> and goes on to say that either all `return` statements in a function should return a value,
> or none of them should.
> If a function contains any explicit `return` statements at all,
> it should end with one as well.

A related refactoring pattern is "default and override."
To use it,
assign a default or most common value to a variable unconditionally,
and then override it in a special case.
The result is fewer lines of code and clearer control flow;
however,
it does mean executing two assignments instead of one,
so it shouldn't be used if the common case is expensive
(e.g., involves a database lookup or a web request).

```python
# ...before..
if configuration['threshold'] > UPPER_BOUND:
    scale = 0.8
else:
    scale = 1.0
```

```python
# ...after...
scale = 1.0
if configuration['threshold'] > UPPER_BOUND:
    scale = 0.8
```

In simple cases,
people will sometimes put the test and assignment on a single line:

```python
scale = 1.0
if configuration['threshold'] > UPPER_BOUND: scale = 0.8
```

\newpage

Some programmers take this even further
and use a **conditional expression**:

```python
scale = 0.8 if configuration['threshold'] > UPPER_BOUND else 1.0
```

However,
this puts the default last instead of first,
which is less clear.

> **A Little Jargon**
>
> `X if test else Y` is called a **ternary expression**.
> Just as a binary expression like `A + B` has two parts,
> a ternary expression has three.
> Conditional expressions are the only ternary expressions in most programming languages.

### Use functions to make code more comprehensible

Functions were created so that programmers could re-use common operations,
but moving code into functions also reduces **cognitive load**
by reducing the number of things that have to be understood simultaneously.

A common rule of thumb is that
no function should be longer than a printed page (about 80 lines)
or have more than four levels of indentation because of nested loops and conditionals.
Anything longer or more deeply nested is hard for readers to understand,
so we should move pieces of long functions into small ones.

```python
# ...before...
def check_neighbors(grid, point):
    if (0 < point.x) and (point.x < grid.width-1) and \
       (0 < point.y) and (point.y < grid.height-1):
        # ...look at all four neighbors
```

```python
# ...after..
def check_neighbors(grid, point):
    if in_interior(grid, point):
        # ...look at all four neighbors...

def in_interior(grid, point):
    return \
    (0 < point.x) and (point.x < grid.width-1) and \
    (0 < point.y) and (point.y < grid.height-1)
```

We should *always* extract functions when code can be re-used.
Even if they are only used once,
multi-part conditionals,
long equations,
and the bodies of loops are good candidates for extraction.
If we can't think of a plausible name,
or if a lot of data has to be passed into the function after it's extracted,
the code should probably be left where it is.
Finally,
it's often helpful to keep using the original variable names as parameter names during refactoring
to reduce typing.

### Combine operations in functions

"Combine functions" is the opposite of "extract function."
If operations are always done together,
it can sometimes be be more efficient to do them together,
and might be easier to understand.
However,
combining functions often reduces their reusability and readability.
(One sign that functions shouldn't have been combined is
people using the combination and throwing some of the result away.)

The fragment below shows how two functions can be combined:

```python
# ...before...
def count_vowels(text):
    num = 0
    for char in text:
        if char in VOWELS:
            num += 1
    return num

def count_consonants(text):
    num = 0
    for char in text:
        if char in CONSONANTS:
            num += 1
    return num
```

```python
# ...after...
def count_vowels_and_consonants(text):
    num_vowels = 0
    num_consonants = 0
    for char in text:
        if char in VOWELS:
            num_vowels += 1
        elif char in CONSONANTS:
            num_consonants += 1
    return num_vowels, num_consonants
```

### Replace code with data

It is easier to understand and maintain lookup tables than complicated conditionals,
so the "create lookup table" refactoring tells us to turn the latter into the former:

```python
# ...before..
def count_vowels_and_consonants(text):
    num_vowels = 0
    num_consonants = 0
    for char in text:
        if char in VOWELS:
            num_vowels += 1
        elif char in CONSONANTS:
            num_consonants += 1
    return num_vowels, num_consonants
```

```python
# ...after...
IS_VOWEL = {'a' : 1, 'b' : 0, 'c' : 0, ... }
IS_CONSONANT = {'a' : 0, 'b' : 1, 'c' : 1, ... }

def count_vowels_and_consonants(text):
    num_vowels = num_consonants = 0
    for char in text:
        num_vowels += IS_VOWEL[char]
        num_consonants += IS_CONSONANT[char]
    return num_vowels, num_consonants
```

The more cases there are,
the greater the advantage lookup tables have over multi-part conditionals.
Those advantages multiply when items can belong to more than one category,
in which case the table is often best written as a dictionary with items as keys
and sets of categories as values:

```python
LETTERS = {
    'A' : {'vowel', 'upper_case'},
    'B' : {'consonant', 'upper_case'},
    # ...other upper-case letters...
    'a' : {'vowel', 'lower_case'},
    'b' : {'consonant', 'lower_case'},
    # ...other lower-case letters...
    '+' : {'punctuation'},
    '@' : {'punctuation'},
    # ...other punctuation...
}

def count_vowels_and_consonants(text):
    num_vowels = num_consonants = 0
    for char in text:
        num_vowels += int('vowel' in LETTERS[char])
        num_consonants += int('consonant' in LETTERS[char])
    return num_vowels, num_consonants
```

The expressions used to update `num_vowels` and `num_consonants` make use of the fact that
`in` produces either `True` or `False`,
which the function `int` converts to either 1 or 0.
We will explore ways of making this code more readable in the exercises.

## Code Reviews 

At the end of Section [Checking Style](https://se-up.github.io/RSE-UP/chapters/clean_readable_code.html#checking-style),
our stop-word program looked like this:

```python
import sys


stops = ['a', 'A', 'the', 'The', 'and']


def count(ln):
    n = 0
    for i in range(len(ln)):
        line = ln[i]
        stuff = line.split()
        for word in stuff:
            # print(word)
            j = stops.count(word)
            if j > 0:
                n = n + 1
    return n


lines = sys.stdin.readlines()
# print('number of lines', len(lines))
n = count(lines)
print('number', n)
```

This passes a PEP-8 style check,
but based on our coding guidelines and our discussion of refactoring,
these things should be changed:

-   The commented-out `print` statements should either be removed
    or turned into logging statements (Section [Error Logging](https://se-up.github.io/RSE-UP/chapters/error_handling.html#reporting-errors)).

-   The variables `ln`, `i`, and `j` should be given clearer names.

-   The outer loop in `count` loops over the indices of the line list
    rather than over the lines.
    It should do the latter
    (which will allow us to get rid of the variable `i`).

-   Rather than counting how often a word occurs in the list of stop words with `stops.count`,
    we can turn the stop words into a set and use `in` to check words.
    This will be more readable *and* more efficient.

-   There's no reason to store the result of `line.split` in a temporary variable:
    the inner loop of `count` can use it directly.

-   Since the set of stop words is a global variable,
    it should be written in upper case.

-   We should use `+=` to increment the counter `n`.

-   Rather than reading the input into a list of lines and then looping over that,
    we can give `count` a stream and have it process the lines one by one.

-   Since we might want to use `count` in other programs someday,
    we should put the two lines at the bottom that handle input into a conditional
    so that they aren't executed when this script is imported.

After making all these changes,
our program looks like this:

```python
import sys


STOPS = {'a', 'A', 'the', 'The', 'and'}


def count(reader):
    n = 0
    for line in reader:
        for word in line.split():
            if word in STOPS:
                n += 1
    return n


if __name__ == '__main__':
    n = count(sys.stdin)
    print('number', n)
```

Reading code in order to find bugs and suggest improvements like these
is called **code review**.
Multiple studies over more than 40 years have shown that
code review is the most effective way to find bugs in software
{cite:p}`Faga1976`; {cite:p}`Faga1986`; {cite:p}`Cohe2010`; {cite:p}`Bacc2013`.
It is also a great way to transfer knowledge between programmers:
reading someone else's code critically will give us lots of ideas about what we could do better,
and highlight things that we should probably stop doing as well.

Despite this,
code review still isn't common in research software development.
This is partly a chicken-and-egg problem:
people don't do it because other people don't do it {cite:p}`Sega2005`.
Code review is also more difficult to do in specialized scientific fields:
in order for review to be useful,
reviewers need to understand the problem domain well enough to comment on algorithms and design choices
rather than indentation and variable naming,
and the number of people who can do that for a research project is often very small {cite:p}`Petr2014`.

Section [Advanced Pull requests](https://se-up.github.io/RSE-UP/chapters/git_advanced.html#pull-requests) explained how to create and merge pull requests.
How we review these is just as important as what we look for:
being dismissive or combative are good ways to ensure that people don't pay attention to our reviews,
or avoid having us review their work {cite:p}`Bern2018`.
Equally,
being defensive when someone offers suggestions politely and sincerely is very human,
but can stunt our development as a programmer.

Lots of people have written guidelines for doing reviews that avoid these traps {cite:p}`Quen2018`; {cite:p}`Sank2018`.
A few common points are:

Work in small increments.
:   As {cite:p}`Cohe2010` and others have found,
    code review is most effective when done in short bursts.
    That means that change requests should also be short:
    anything that's more than a couple of screens long
    should be broken into smaller pieces.

Look for algorithmic problems first.
:   Code review isn't just (or even primarily) about style:
    its real purpose is to find bugs before they can affect anyone.
    The first pass over any change should therefore look for algorithmic problems.
    Are the calculations right?
    Are any rare cases going to be missed?
    Are errors being caught and handled (Chapter [Error Handling](https://se-up.github.io/RSE-UP/chapters/error_handling.html))?
    Using a consistent style helps reviewers focus on these issues.

Use a checklist.
:   Linters are great,
    but can't decide when someone should have used a lookup table instead of conditionals.
    A list of things to check for can make review faster and more comprehensible,
    especially when we can copy-and-paste or drag-and-drop specific comments
    onto specific lines
    (something that GitHub unfortunately doesn't yet support).

Ask for clarification.
:   If we don't understand something,
    or don't understand why the author did it,
    we should ask.
    (When the author explains it,
    we might suggest that the explanation should be documented somewhere.)

Offer alternatives.
:   Telling authors that something is wrong is helpful;
    telling them what they might do instead is more so.

Don't be sarcastic or disparaging.
:   "Did you maybe think about *testing* this garbage?"
    is a Code of Conduct violation in any well-run project.

Don't present opinions as facts.
:   "Nobody uses X anymore" might be true.
    If it is,
    the person making the claim ought to be able to point at download statistics
    or a Google Trends search;
    if they can't,
    they should say,
    "I don't think we use X anymore" and explain why they think that.

Don't feign surprise or pass judgment.
:   "Gosh, didn't you know [some obscure fact]?" isn't helpful;
    neither is, "Geez, why don't you [some clever trick] here?"

Don't overwhelm people with details.
:   If someone has used the letter `x` as a variable name in several places,
    and they shouldn't have,
    comment on the first two or three and simply put a check beside the others---the reader
    won't need the comment repeated.

Don't try to sneak in feature requests.
:   Nobody enjoys fixing bugs and style violations.
    Asking them to add entirely new functionality while they're at it is rude.

How we respond to reviews is just as important:

Be specific in replies to reviewers.
:   If someone has suggested a better variable name,
    we can probably simply fix it.
    If someone has suggested a major overhaul to an algorithm,
    we should reply to their comment to point at the commit that includes the fix.

Thank our reviewers.
:   If someone has taken the time to read our code carefully,
    thank them for doing it.

And finally:

**Don't let anyone break these rules just because they're frequent contributors or in positions of power.**
As {cite:p}`Grue2015` says,
the culture of any organization is shaped by the worst behavior it is willing to tolerate.
The main figures in a project should be *more* respectful than everyone else
in order to show what standards everyone else is expected to meet.

## Python Features 

**Working memory** can only hold a few items at once:
initial estimates in the 1950s put the number at 7±2 {cite:p}`Mill1956`,
and more recent estimates put it as low as 4 or 5.
High-level languages from Fortran to Python
are essentially a way to reduce the number of things programmers have to think about at once
so that they can fit what the computer is doing into this limited space.
The sections below describe some of these features;
as we become more comfortable with Python we will find and use others.

But beware:
the things that make programs more compact and comprehensible for experienced programmers
can make them less comprehensible for novices.
For example,
suppose we want to create this matrix as a list of lists:

```python
[[0, 1, 2, 3, 4],
 [1, 2, 3, 4, 5],
 [2, 3, 4, 5, 6],
 [3, 4, 5, 6, 7],
 [4, 5, 6, 7, 8]]
```

One way is to use loops:

```python
matrix = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(i+j)
    matrix.append(row)
```

Another is to use a nested **list comprehension**:

```python
[[i+j for j in range(5)] for i in range(5)]
```

An experienced programmer might recognize what the latter is doing;
the rest of us are probably better off reading and writing the more verbose solution.

### Provide default values for parameters

If our function requires two dozen parameters,
the odds are very good that users will frequently forget them
or put them in the wrong order.
One solution is to bundle parameters together so that (for example)
people pass three `point` objects instead of nine separate `x`, `y`, and `z` values.

A second approach (which can be combined with the previous one)
is to specify **default values** for some of the parameters.
Doing this gives users control over everything
while also allowing them to ignore details;
it also indicates what we consider "normal" for the function.

For example,
suppose we are comparing images to see if they are the same or different.
We can specify two kinds of tolerance:
how large a difference in color value to notice,
and how many differences above that threshold to tolerate
as a percentage of the total number of pixels.
By default,
any color difference is considered significant,
and only 1% of pixels are allowed to differ:

```python
def image_diff(left, right, per_pixel=0, fraction=0.01):
    # ...implementation...
```

When this function is called using `image_diff(old, new)`,
those default values apply.
However,
it can also be called like this:

-   `image_diff(old, new, per_pixel=2)`
    allows pixels to differ slightly without those differences being significant.
-   `image_diff(old, new, fraction=0.05)` allows more pixels to differ.
-   `image_diff(old, new, per_pixel=1, fraction=0.005)`
    raises the per-pixel threshold but decreases number of allowed differences.

Note that we do not put spaces around the `=` when defining a default parameter value.
This is consistent with PEP-8's rules about spacing in function definitions and calls
(Section [Python Style](https://se-up.github.io/RSE-UP/chapters/clean_readable_code.html#python-style)).

Default parameter values make code easier to understand and use,
but there is a subtle trap.
When Python executes a function definition like this:

```python
def collect(new_value, accumulator=set()):
    accumulator.add(new_value)
    return accumulator
```

it calls `set()` to create a new empty set
*when it is reading the function definition*,
and then uses that set as the default value for `accumulator`
every time the function is called.
It does *not* call `set()` once for each call,
so all calls using the default will share the same set:

```python
>>> collect('first')
{'first'}
>>> collect('second')
{'first', 'second'}
```

A common way to avoid this is to pass `None` to the function
to signal that the user didn't provide a value:

```python
def collect(new_value, accumulator=None):
    if accumulator is None:
        accumulator = set()
    accumulator.add(new_value)
    return accumulator
```

### Handle a variable number of arguments

We can often make programs simpler by writing functions that take
**a variable number of arguments**,
just like `print` and `max`.
One way is to require users to stuff those arguments into a list,
e.g.,
to write `find_limits([a, b, c, d])`.
However,
Python can do this for us.
If we declare a single argument whose name starts with a single `*`,
Python will put all "extra" arguments into a **tuple**
and pass that as the argument.
By convention,
this argument is called `args`:

```python
def find_limits(*args):
    print(args)

find_limits(1, 3, 5, 2, 4)
```

```text
(1, 3, 5, 2, 4)
```

This catch-all parameter can be used with regular parameters,
but must come last in the parameter list to avoid ambiguity:

```python
def select_outside(low, high, *values):
    result = []
    for v in values:
        if (v < low) or (v > high):
            result.add(v)
    return result

print(select_outside(0, 1.0, 0.3, -0.2, -0.5, 0.4, 1.7))
```

```text
[-0.2, -0.5, 1.7]
```

An equivalent special form exists for **keyword arguments**:
the catch-all variable's name is prefixed with `**` (i.e., two asterisks instead of one),
and it is conventionally called `kwargs` (for "keyword arguments").
When this is used,
the function is given a **dictionary** of names and values
rather than a list:

```python
def set_options(tag, **kwargs):
    result = f'<{tag}'
    for key in kwargs:
        result += f' {key}="{kwargs[key]}"'
    result += '/>'
    return result

print(set_options('h1', color='blue'))
print(set_options('p', align='center', size='150%'))
```

```text
<h1 color="blue"/>
<p align="center" size="150%"/>
```

Notice that the names of parameters are not quoted:
we pass `color='blue'` to the function,
not `'color'='blue'`.

### Unpacking variable arguments

We can use the inverse of `*args` and `**kwargs` to match a list of values to arguments.
In this case,
we put the `*` in front of a list and `**` in front of a dictionary when *calling* the function,
rather than in front of the parameter when *defining* it:

```python
def trim_value(data, low, high):
    print(data, "with", low, "and", high)

parameters = ['some matrix', 'lower bound']
named_parameters = {'high': 'upper bound'}
trim_value(*parameters, **named_parameters)
```

```text
some matrix with lower bound and upper bound
```

### Use destructuring to assign multiple values at once

One last feature of Python is
**destructuring assignment**.
Suppose we have a nested list such as `[1, [2, 3]]`,
and we want to assign its numbers to three variables
called `first`, `second`, and `third`.
Instead of writing this:

```python
first = values[0]
second = values[1][0]
third = values[1][1]
```

we can write this:

```python
[first, [second, third]] = [1, [2, 3]]
```

In general,
if the variables on the left are arranged in the same way as the values on the right,
Python will automatically unpack the values and assign them correctly.
This is particularly useful when looping over lists of structured values:

```python
people = [
    [['Kay', 'McNulty'], 'mcnulty@eniac.org'],
    [['Betty', 'Jennings'], 'jennings@eniac.org'],
    [['Marlyn', 'Wescoff'], 'mwescoff@eniac.org']
]
for [[first, last], email] in people:
    print('{first} {last} <{email}>')
```

```text
Kay McNulty <mcnulty@eniac.org>
Betty Jennings <jennings@eniac.org>
Marlyn Wescoff <mwescoff@eniac.org>
```

## Summary 

George Orwell laid out [six rules for good writing]( https://en.wikipedia.org/wiki/Politics_and_the_English_Language#Remedy_of_Six_Rules),
the last and most important of which is,
"Break any of these rules sooner than say anything outright barbarous."
PEP-8 conveys [the same message](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds):
there will always be cases where your code will be easier to understand
if you *don't* do the things described in this lesson,
but there are probably fewer of them than you think.



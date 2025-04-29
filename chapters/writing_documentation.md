# Documenting Programs 

An old proverb says, "Trust, but verify."
The equivalent in programming is, "Be clear, but document."
No matter how well software is written,
it always embodies decisions that aren't explicit in the final code
or accommodates complications that aren't going to be obvious to the next reader.
Putting it another way,
the best function names in the world aren't going to answer the questions
"Why does the software do this?"
and
"Why doesn't it do this in a simpler way?"

In this appendix we address some issues that commonly arise
when people start to think about documenting their software.
We start with tips for writing good docstrings,
before considering more detailed documentation
like tutorials, cookbooks and frequently asked question
(**FAQ**) lists.
Clearly defining your audience can make it easier to determine
which types of documentation you need to provide,
and there are a number of things you can do to reduce the
work involved in providing support for FAQs. 

## Writing Good Docstrings 

If we are doing **exploratory programming**,
a short **docstring** to remind ourselves of each function's purpose is probably as much documentation as we need.
(In fact, it's probably better than what most people do.)
That one- or two-liner should begin with an active verb and describe either
how inputs are turned into outputs,
or what side effects the function has;
as we discuss below,
if we need to describe both,
we should probably rewrite our function.

An active verb is something like "extract", "normalize", or "plot".
For example,
here's a function that calculates someone's age from their birthday,
which uses a one-line docstring beginning with the active verb "find": 

```python
import re
from datetime import date


def calculate_age(birthday):
    """Find current age from birth date."""
    valid_date = '([0-9]{4})-([0-9]{2})-([0-9]{2})$'
    if not bool(re.search(valid_date, birthday)):
        message = 'Birthday must be in YYYY-MM-DD format'
        raise ValueError(message)
    today = date.today()
    born = date.fromisoformat(birthday)
    no_bday_this_year_yet = (today.month,
                             today.day) < (born.month,
                                           born.day)
    age = today.year - born.year - no_bday_this_year_yet
    return age
```

Other examples of good one-line docstrings include:

-   "Create a list of capital cities from a list of countries."
-   "Clip signals to lie in [0...1]."
-   "Reduce the red component of each pixel."

We can tell our one-liners are useful if we can read them aloud in the order the functions are called
in place of the function's name and parameters.

Once we start writing code for other people (or our future selves)
our docstrings should include:

1.  The name and purpose of every public class, function, and constant in our code.
2.  The name, purpose, and default value (if any) of every parameter to every function.
3.  Any side effects the function has.
4.  The type of value returned by every function.
5.  What exceptions those functions can raise and when.

The word "public" in the first rule is important.
We don't have to write full documentation for helper functions
that are only used inside our package and aren't meant to be called by users,
but these should still have at least a comment explaining their purpose.

Here's the previous function with a more complete docstring:

```python
def calculate_age(birthday):
    """Find current age from birth date.
    
    :param birthday str: birth date
    :returns: age in years
    :rtype: int
    :raises ValueError: if birthday not in YYYY-MM-DD format
    """
```

We could format and organize the information in the docstring any way we like,
but here we've decided to use **reStructuredText**,
which is the default plain-text markup format supported by [Sphinx](https://www.sphinx-doc.org/en/master/)
(Section [Documenting Packages](https://se-up.github.io/RSE-UP/chapters/packaging/packaging.html#documenting-packages).
The [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists) describes the precise syntax for
parameters, returns, exceptions and other items that are typically included
in a docstring.

While the reStructuredText docstring format suggested in the Sphinx documentation
looks nice once Sphinx parses and converts it to HTML for the web,
the code itself is somewhat dense and hard to read.
To address this issue,
a number of different formats have been proposed.
Two of the most prominent are [Google style]( https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings):

```python
def calculate_age(birthday):
    """Find current age from birth date.
    
    Args:
        birthday (str): birth date.
    
    Returns:
        Age in years.
    
    Raises:
        ValueError: If birthday not in YYYY-MM-DD format.
    """
``` 

and [`numpydoc` style](https://numpydoc.readthedocs.io/en/latest/):

```python
def calculate_age(birthday):
    """Find current age from birth date.
    
    Parameters
    ----------
    birthday : string
        birth date

    Returns
    -------
    integer
        age in years

    Raises
    ------
    ValueError
        if birthday not in YYYY-MM-DD format
    """
```

These two formats have become so popular that a Sphinx extension
called [Napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/) has been released. It parses `numpydoc` and Google style docstrings and converts them to reStructuredText before Sphinx attempts to parse them.
This happens in an intermediate step while Sphinx is processing the documentation, so it doesn’t modify any of the docstrings in your actual source code files. The choice between the `numpydoc` and Google styles is largely aesthetic, but the two styles should not be mixed.
Choose one style for your project and be consistent with it.

## Defining Your Audience 

It's important to consider who documentation is for.
There are three kinds of people in any domain:
**novices**, **competent practitioners**, and **experts** {cite:p}`Wils2018`.
A novice doesn't yet have a **mental model** of the domain:
they don't know what the key terms are,
how they relate,
what the causes of their problems are,
or how to tell whether a solution to their problem is appropriate or not.

Competent practitioners know enough to accomplish routine tasks with routine effort: they may need to check [Stack Overflow](https://stackoverflow.com) every few minutes, but they know what to search for and what "done" looks like.

Or since 2023 and the rise of LLMs such as ChatGPT, Bard, many started asking the question there instead of on Stack overflow. 

Finally, experts have such a deep and broad understanding of the domain
that they can solve routine problems at a glance
and are able to handle the one-in-a-thousand cases
that would baffle the merely competent.

Each of these three groups needs a different kind of documentation:

-   A novice needs a tutorial that introduces her to key ideas one by one
    and shows how they fit together.

-   A competent practitioner needs reference guides, cookbooks, and Q&A sites;
    these give her solutions close enough to what she needs
    that she can tweak them the rest of the way.

-   Experts need this material as well---nobody's memory is perfect---but
    they may also paradoxically want tutorials.
    The difference between them and novices is that experts want tutorials on how things work
    and why they were designed that way.

The first thing to decide when writing documentation
is therefore to decide which of these needs we are trying to meet.
Tutorials like this book should be long-form prose that contain code samples and diagrams.
They should use **authentic tasks** to motivate ideas,
i.e.,
show people things they actually want to do rather than printing the numbers from 1 to 10,
and should include regular check-ins
so that learners and instructors alike can tell if they're making progress.

Tutorials help novices build a mental model,
but competent practitioners and experts will be frustrated by their slow pace and low information density.
They will want single-point solutions to specific problems,
like how to find cells in a spreadsheet that contain a certain string
or how to configure the web server to load an access control module.
They can make use of an alphabetical list of the functions in a library,
but are much happier if they can search by keyword to find what they need;
one of the signs that someone is no longer a novice is that
they're able to compose useful queries and tell if the results are on the right track or not.

> **False Beginners**
>
> A **false beginner** is someone who appears not to know anything,
> but who has enough prior experience in other domains
> to be able to piece things together much more quickly than a genuine novice.
> Someone who is proficient with MATLAB, for example,
> will speed through a tutorial on Python's numerical libraries
> much more quickly than someone who has never programmed before.
> Creating documentation for false beginners is especially challenging;
> if resources permit,
> the best option is often a translation guide
> that shows them how they would do a task with the system they know well
> and then how to do the equivalent task with the new system.

In an ideal world,
we would satisfy these needs with a chorus of explanations {cite:p}`Caul2016`,
some long and detailed, others short and to the point.
In our world, though, time and resources are limited, so all but the most popular packages must make do with single explanations.

## Creating an FAQ 

As projects grow,
documentation within functions alone may be insufficient for users to apply code to their own problems.
One strategy to assist other people with understanding a project is with
an **FAQ**:
a list of frequently asked questions and corresponding answers.
A good FAQ uses the terms and concepts that people bring to the software
rather than the vocabulary of its authors;
putting it another way,
the questions should be things that people might search for online,
and the answers should give them enough information to solve their problem.

Creating and maintaining an FAQ is a lot of work,
and unless the community is large and active,
a lot of that effort may turn out to be wasted,
because it's hard for the authors or maintainers of a piece of software
to anticipate what newcomers will be mystified by.
A better approach is to leverage sites like [Stack Overflow](https://stackoverflow.com),
which is where most programmers are going to look for answers anyway:

1.  Post every question that someone actually asks us,
    whether it's online, by email, or in person.
    Be sure to include the name of the software package in the question
    so that it's findable.

2.  Answer the question,
    making sure to mention which version of the software we're talking about
    (so that people can easily spot and discard stale answers in the future).

The **Stack Overflow** guide to [asking a good question](https://stackoverflow.com/help/how-to-ask) has been refined over many years, and is a good guide for any project:

Write the most specific title we can.
:   "Why does division sometimes give a different result in Python 2.7 and Python 3.5?"
    is much better than, "Help! Math in Python!!"

Give context before giving sample code.
:   A few sentences to explain what we are trying to do
    and why it will help people determine if their question is a close match to ours or not.

Provide a minimal reprex.
:   Section [Bug Reports](https://se-up.github.io/RSE-UP/chapters/work_teams/working_in_teams.html#bug-reports) explains the value of a **reproducible example**,
    and why reprexes should be as short as possible.
    Readers will have a much easier time figuring out if this question and its answers are for them
    if they can see *and understand* a few lines of code.

Tag, tag, tag.
:   Keywords make everything more findable,
    from scientific papers to left-handed musical instruments.

Use "I" and question words (how/what/when/where/why).
:   Writing this way forces us to think more clearly about
    what someone might actually be thinking when they need help.

Keep each item short.
:   The "minimal manual" approach to instructional design {cite:p}`Carr2014`
    breaks everything down into single-page steps,
    with half of that page devoted to troubleshooting.
    This may feel trivializing to the person doing the writing,
    but is often as much as a person searching and reading can handle.
    It also helps writers realize just how much implicit knowledge they are assuming.

Allow for a chorus of explanations.
:   As discussed earlier,
    users are all different from one another,
    and are therefore best served by a chorus of explanations.
    Do not be afraid of providing multiple explanations to a single question
    that suggest different approaches
    or are written for different prior levels of understanding.

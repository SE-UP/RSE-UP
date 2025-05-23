# Working in Teams 

> Evil begins when you begin to treat people as things.
>
> --- Terry Pratchett

Projects can run for years with poorly written code,
but none will survive for long if people are confused,
pulling in different directions,
or hostile to each other.
This chapter therefore looks at how to create a culture of collaboration
that will help people who want to contribute to your project 
and introduce a few ways to manage projects and teams as they develop.
Our recommendations draw on {cite:p}`Foge2005`, which describes how good open source software projects are run, and on 
{cite:p}`Boll2014`, which explains what a **commons** is and when it's the right model to use.

At this point, the Zipf's Law project should include:
```text
zipf/
├── .gitignore
├── README.md
├── bin
│   ├── book_summary.sh
│   ├── collate.py
│   ├── wordcount.py
│   ├── plotcounts.py
│   ├── template.py
├── data
│   ├── README.md
│   ├── dracula.txt
│   └── ...
└── results
    ├── dracula.csv
    ├── dracula.png
    └── ...
```

## What Is a Project? 

The first decision we have to make is what exactly constitutes a "project" 
{cite:p}`Wils2017`. Some examples are:

-   A dataset that is being used by several research projects.
    The project includes the raw data,
    the programs used to tidy that data,
    the tidied data,
    the extra files needed to make the dataset a package,
    and a few text files describing the data's authors, license, and 
    **provenance**.

-   A set of annual reports written for an **NGO**.
    The project includes several Jupyter notebooks,
    some supporting Python libraries used by those notebooks,
    copies of the HTML and PDF versions of the reports,
    a text file containing links to the datasets used in the report
    (which can't be stored on GitHub since they contain personal identifying information),
    and a text file explaining details of the analysis that the authors didn't include in the reports themselves.

-   A software library that provides an interactive glossary of data science terms in both Python and R.
    The project contains the files needed to create a package in both languages,
    a Markdown file full of terms and definitions,
    and a Makefile with targets to check cross-references, compile packages, and so on.

Some common criteria for creating projects are one per publication, one per deliverable piece of software, or one per
team. The first tends to be too small: a good dataset will result in several reports,
and the goal of some projects is to produce a steady stream of reports (such as monthly forecasts).
The second is a good fit for software engineering projects whose primary aim is to produce tools rather than results,
but can be an awkward fit for data analysis work. The third tends to be too large: a team of half a dozen people may
work on many different things at once, and a repository that holds them all quickly looks like someone's basement.

One way to decide what makes up a project is to ask what people have meetings about. If the same group needs to get
together on a regular basis to talk about something, that "something" probably deserves its own repository.
And if the list of people changes slowly over time but the meetings continue,
that's an even stronger sign.

## Include Everyone

Most research software projects begin as the work of one person,
who may continue to do the bulk of the coding and data analysis throughout its existence {cite:p}`Maju2019`.
As projects become larger, though, they eventually need more contributors to sustain them. Involving more people also
improves the functionality and robustness of the code, since newcomers bring their own expertise or see old problems in
new ways.

In order to leverage a group's expertise, a project must do more than *allow* people to contribute:
Its leaders must communicate that the project *wants* contributions, and that newcomers are welcome and 
valued {cite:p}`Shol2019`.
Saying "the door is open" is not enough: many potential contributors have painful personal experience of being less
welcome than others. In order to create a truly welcoming environment for everyone, the project must explicitly
acknowledge that some people are treated unfairly and actively take steps to remedy this. Doing this increases diversity
within the team, which makes it more productive {cite:p}`Zhan2020`. 
More importantly, it is the right thing to do.

> **Terminology**
>
> **Privilege** is an unearned advantage given to some people but not all,
> while **oppression** is systemic inequality that benefits the privileged
> and harms those without privilege {cite:p}`Auro2018`.
> In Europe, the Americas, Australia, and New Zealand,
> a straight, white, affluent, physically able male
> is less likely to be interrupted when speaking,
> more likely to be called on in class,
> and more likely to get a job interview based on an identical CV
> than someone who is outside these categories.
> People who are privileged are often not aware of it,
> as they've lived in a system that provides unearned advantages their entire lives.
> In John Scalzi's memorable phrase,
> they've been playing on the lowest difficulty setting there is
> their whole lives,
> and as a result don't realize how much harder things are for others {cite:p}`Scal2012`.
>
> The targets of oppression are often called "members of a marginalized group,"
> but targets don't choose to be marginalized:
> people with privilege marginalize them.
> Finally,
> an **ally** is a member of a privileged group
> who is working to understand their own privilege and end oppression.

Encouraging inclusivity is a shared responsibility.
If we are privileged,
we should educate ourselves and call out peers who are marginalizing others,
even if (or especially if) they aren't conscious of doing it.
As project leaders,
part of our job is to teach contributors how to be allies
and to ensure an inclusive culture {cite:p}`Lee1962`.

## Establish a Code of Conduct 

The starting point for making a project more inclusive is to establish a Code of Conduct.
This does four things:

1.  It promotes fairness within a group.
2.  It reassures members of marginalized groups
    who have experienced harassment or unwelcoming behavior before
    that this project takes inclusion seriously.
3.  It ensures that everyone knows what the rules are.
    (This is particularly important when people come from different cultural backgrounds.)
4.  It prevents anyone who misbehaves from pretending that
    they didn't know what they did was unacceptable.

More generally, a Code of Conduct makes it easier for people to contribute 
by reducing uncertainty about what behaviors are acceptable.
Some people may push back claiming that it's unnecessary,
or that it infringes freedom of speech, but what they usually mean is that thinking about how they might have benefited
from past inequity makes them feel uncomfortable.
If having a Code of Conduct leads to them going elsewhere, that will probably make the project run more smoothly.

By convention, we add a Code of Conduct to our project by creating a file called `CONDUCT.md` in the project's root
directory. Writing a Code of Conduct that is both comprehensive and readable is hard.
We therefore recommend using one that other groups have drafted, refined, and tested.
The [Contributor Covenant](https://www.contributor-covenant.org) is relevant for projects being developed online, such as those based on GitHub:

```text
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make
participation in our community a harassment-free experience for
everyone, regardless of age, body size, visible or invisible
disability, ethnicity, sex characteristics, gender identity and
expression, level of experience, education, socio-economic
status, nationality, personal appearance, race, religion, or
sexual identity and orientation.

We pledge to act and interact in ways that contribute to an
open, welcoming, diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment
for our community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and
  experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by
  our mistakes, and learning from the experience
* Focusing on what is best not just for us as individuals, but
  for the overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual
  attention or advances of any kind
* Trolling, insulting or derogatory comments, and personal or
  political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or
  email address, without their explicit permission
* Other conduct which could reasonably be considered
  inappropriate in a professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing
our standards of acceptable behavior and will take appropriate
and fair corrective action in response to any behavior that
they deem inappropriate, threatening, offensive, or harmful.

Community leaders have the right and responsibility to remove,
edit, or reject comments, commits, code, wiki edits, issues,
and other contributions that are not aligned to this
Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and
also applies when an individual is officially representing the
community in public spaces. Examples of representing our
community include using an official e-mail address, posting via
an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable
behavior may be reported to the community leaders responsible
for enforcement at [INSERT CONTACT METHOD]. All complaints will
be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and
security of the reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines
in determining the consequences for any action they deem in
violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other
behavior deemed unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community
leaders, providing clarity around the nature of the violation
and an explanation of why the behavior was inappropriate.
A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or
series of actions.

**Consequence**: A warning with consequences for continued
behavior. No interaction with the people involved, including
unsolicited interaction with those enforcing the Code of
Conduct, for a specified period of time. This includes avoiding
interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a
temporary or permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community
standards, including sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction
or public communication with the community for a specified
period of time. No public or private interaction with the
people involved, including unsolicited interaction with those
enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of
community standards, including sustained inappropriate
behavior, harassment of an individual, or aggression toward or
disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public
interaction within the community.

## Attribution

This Code of Conduct is adapted from the
[Contributor Covenant][covenant],
version 2.0, available at
www.contributor-covenant.org/version/2/0/code_of_conduct.html

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement
ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct,
see the FAQ at https://www.contributor-covenant.org/faq.
Translations are available at
https://www.contributor-covenant.org/translations.
```

As you can see,
the Contributor Covenant defines expectations for behavior,
the consequences of non-compliance,
and the mechanics of reporting and handling violations.
The third part is as important as the first two,
since rules are meaningless without a method to enforce them;
{cite:p}`Auro2018` is a short, practical guide that every project lead should read.

<!-->
> **In-Person Events**
>
> The Contributor Covenant works well for interactions that are largely online,
> which is the case for many research software projects.
> The best option for in-person events is
> the [model Code of Conduct](https://geekfeminism.wikia.com/wiki/Conference_anti-harassment/) from the [Geek Feminism Wiki](https://geekfeminism.wikia.com/),
> which is used by many open source organizations and conferences.
> If your project is sited at a university or within a company,
> it may already have Code of Conduct:
> the Human Resources department is usually the most helpful place to ask.

### Software 

In order to choose the right license for our software, we need to understand the difference between two kinds of license.
The **MIT License** (and its close sibling the BSD License) say that people can do whatever they want to with the
software as long as they cite the original source, and that the authors accept no responsibility if things go wrong.
The **GNU Public License** gives people similar rights, but requires them to share their own work on the same terms:

> You may copy, distribute, and modify the software as long as you track changes/dates in source files.
> Any modifications to or software including (via compiler) GPL-licensed code
> must also be made available under the GPL
> along with build and install instructions.
>
> --- [tl;dr](https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3))
In other words,
if someone modifies GPL-licensed software or incorporates it into their own project,
and then distributes what they have created,
they have to distribute the source code for their own work as well.

The GPL was created to prevent companies from taking advantage of open software
without contributing anything back.
The last thirty years have shown that this restriction isn't necessary:
many projects have survived and thrived without this safeguard.
We therefore recommend that projects choose the MIT license,
as it places the fewest restrictions on future action.

```text
MIT License

Copyright (c) 2020 Amira Khan

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
```

> **First, Do No Harm**
>
> The [Hippocratic License](https://firstdonoharm.dev/)
> is a newer license
> that is quickly becoming popular.
> Where the GPL requires people to share their work,
> the Hippocratic License requires them to do no harm.
> More precisely,
> it forbids people from using the software in ways that violate
> the [Universal Declaration of Human Rights](https://en.wikipedia.org/wiki/Universal_Declaration_of_Human_Rights).
> We have learned the hard way that software and science can be mis-used;
> adopting the Hippocratic License is a small step toward preventing this.

### Data and reports 

The MIT license, the GPL, and the Hippocratic License are intended for use with software. When it comes to data and
reports, the most widely used family of licenses are those produced by [Creative Commons](https://creativecommons.org/).
These have been written and checked by lawyers and are well understood by the community.

The most liberal option is referred to as **CC-0**, where the "0" stands for "zero restrictions." This puts work in the
public domain, i.e., allows anyone who wants to use it to do so, however they want, with no restrictions.
CC-0 is usually the best choice for data since it simplifies aggregate analysis involving datasets from different
sources. It does not negate the scholarly tradition and requirement of citing sources;
it just doesn't make it a legal requirement.

The next step up from CC-0 is the Creative Commons--Attribution license,
usually referred to as **CC-BY**.
This allows people to do whatever they want to with the work as long as they cite the original source. 
This is the best license to use for manuscripts: we want people to share them widely but also want to get credit for
our work.

Other Creative Commons licenses incorporate various restrictions 
and are usually referred to using two-letter abbreviations:

-   ND (no derivative works) prevents people from creating modified versions of our work.
    Unfortunately, this also inhibits translation and reformatting.

-   SA (share-alike) requires people to share work that incorporates ours
    on the same terms that we used.
    Again,
    it is fine in principle, but in practice it makes aggregation and recombination difficult.

-   NC (no commercial use) does *not* mean that people cannot charge money for something that includes our work,
    though some publishers still try to imply that in order to scare people away from open licensing.
    Instead,
    the NC clause means that people cannot charge for something that uses our work without our explicit permission,
    which we can give under whatever terms we want.

To apply these concepts to our Zipf's Law project,
we need to consider both our data (which other people created)
and our results (which we create).
We can view the license for the novels by looking in `data/README.md`,
which tells us that the Gutenberg Project books are in the public domain (i.e., CC-0).
This is a good choice for our results as well, but after reflection,
we decide to choose CC-BY for our papers so that everyone can read them (and cite them).

## Planning 

Codes of conduct and licenses are a project's constitution, but how do contributors know what they should actually be
doing on any given day?
Whether we are working by ourselves or with a group of people, the best way to manage this is to use an
**issue tracking system** to keep track of tasks we need to complete or problems we need to fix.
**Issues** are sometimes called **tickets**, so issue tracking systems are sometimes called **ticketing systems**.
They are also often called **bug trackers**, but they can be used to manage any kind of work, and are often a convenient
way to manage discussions as well.


Like other **forges**, GitHub allows participants to create issues for a project, comment on existing issues, and search
all available issues.
Every issue can hold:

-   A unique ID, such as `#123`, which is also part of its URL.
    This makes issues easy to find and refer to:
    GitHub automatically turns the expression `#123` in a **commit message** into a link to that issue.

-   A one-line title to aid browsing and search.

-   The issue's current status.
    In simple systems (like GitHub's) each issue is either open or closed,
    and by default,
    only open issues are displayed.
    Closed items are generally removed from default interfaces,
    so issues should only be closed when they no longer require any attention.

-   The user ID of the issue's creator.
    Just as `#123` refers to a particular issue,
    `@name` is automatically translated into a link to that person.
    The IDs of people who have commented on it or modified it are embedded in the issue's history,
    which helps figure out who to talk to about what.

-   The user ID of the person assigned to review the issue, if someone is assigned.

-   A full description that may include screenshots,
    error messages,
    and anything else that can be put on a web page.

-   Replies, counter-replies, and so on from people who are interested in the issue.

Broadly speaking,
people create three kinds of issues:

1.  **Bug reports** to describe problems they have encountered.
2.  **Feature requests** describing what could be done next,
    such as "add this function to this package" or "add a menu to the website."

3.  Questions about how to use the software, how parts of the project work,
    or its future directions. 
    These can eventually turn into bug reports or feature requests 
    and can often be recycled as documentation.

> **Helping Users Find Information**
>
> Many projects encourage people to ask questions on a mailing list or in a chat channel.
> However,
> answers given there can be hard to find later,
> which leads to the same questions coming up over and over again.
> If people can be persuaded to ask questions by filing issues,
> and to respond to issues of this kind,
> then the project's old issues become a customized [Stack Overflow](https://www.stackoverflow.com) for the project.
> Some projects go so far as to create a page of links
> to old questions and answers that are particularly helpful.

## Bug Reports 

One steady supply of work in any active project is **bug reports**. 
Unsurprisingly, a well-written bug report is more likely to get a fast response that actually addresses the 
problem {cite:p}`Bett2008`. To write a good bug report:

1.  Make sure the problem actually *is* a bug.
    It's always possible that we have called a function the wrong way
    or done an analysis using the wrong configuration file.
    If we take a minute to double-check,
    or ask someone else on our team to check our logic,
    we could well fix the problem ourselves.

2.  Try to come up with a **reproducible example** 
    or "reprex" that includes only the steps needed to make the problem happen,
    and that (if possible) uses simplified data rather than a complete dataset.
    Again,
    we can often solve the problem ourselves as we trim down the steps to create one.

3.  Write a one-line title for the issue
    and a longer (but still brief) description that includes relevant details.

4.  Attach any screenshots that show the problem,
    resulting errors,
    or (slimmed-down) input files needed to re-create it.

5.  Describe the version of the software we were using,
    the operating system we were running on,
    which version of the programming language we ran it with,
    and anything else that might affect behavior.
    If the software in question uses a logging framework in section [on error logging](https://se-up.github.io/RSE-UP/chapters/error_handling.html#reporting-errors),
    turn debugging output on and include it with the issue.

6.  Describe each problem separately so that each one can be tackled on its own.
    This parallels the rule about creating a branch in version control for each bug fix or feature
    discussed in Section [git advanced](https://se-up.github.io/RSE-UP/chapters/git_advanced.html).

An example of a well-written bug report with all of the components mentioned above
is shown in [Figure: bug report](teams-bug-report).

```{figure} ../figures/teams/bug-report.png
:name: teams-bug-report
Teams bug report
```

It takes time and energy to write a good error report.
If the report is being filed by a member of the development team, the incentive to document errors well is that
resolving the issue later is easier. You can encourage users from outside the project to write thorough error reports by
including an issue template for your project. An issue template is a file included in your GitHub repository that
proliferates each new issue with text that describes expectations for content that should be submitted.
You can't force new issues to be as complete as you might like, but you can use an issue template to make it easier for
contributors to remember and complete documentation about bug reports.

Sometimes the person creating the issue may not know or have the right answer for some of these things and will be doing
their best with limited information about the error. Responding with kindness and encouragement is important to maintain
a healthy community, and should be enforced by the project's Code of Conduct (Section [teams coc](https://se-up.github.io/RSE-UP/chapters/working_in_teams.html#establish-a-code-of-conduct)).

## Labeling Issues 

The bigger or older a project gets, the harder it is to find things---unless, that is, the project's members put in a
bit of work to make things findable {cite:p}`Lin2020`.
Issue trackers let project members add **labels** to issues to make things easier to search and organize. 
Labels are also often called **tags**; whatever term is used, each one is just a descriptive word or two.

GitHub allows project owners to define any labels they want.
A small project should always use some variation on these three:

-   *Bug*: something should work but doesn't.

-   *Enhancement*: something that someone wants added to the software.

-   *Task*: something needs to be done, but won't show up in code
    (e.g., organizing the next team meeting).

Projects also often use:

-   *Question*: where is something
    or how is something supposed to work?
    As noted above,
    issues with this label can often be recycled as documentation.

-   *Discussion* or *Proposal*: something the team needs to make a decision about
    or a concrete proposal to resolve such a discussion.
    All issues can have discussion:
    this category is for issues that start that way.
    (Issues that are initially labeled *Question*
    are often relabeled *Discussion* or *Proposal*
    after some back and forth.)

-   *Suitable for Newcomer* or *Beginner-Friendly*:
    to identify an easy starting point for someone who has just joined the project.
    If we help potential new contributors find places to start,
    they are more likely to do so {cite:p}`Stei2014`.

The labels listed above identify the kind of work an issue describes.
A separate set of labels can be used to indicate the state of an issue:

-   *Urgent*: work needs to be done right away.
    (This label is typically reserved for security fixes).

-   *Current*: this issue is included in the current round of work.

-   *Next*: this issue is (probably) going to be included in the next round.

-   *Eventually*: someone has looked at the issue and believes it needs to be tackled,
    but there's no immediate plan to do it.

-   *Won't Fix*: someone has decided that the issue isn't going to be addressed,
    either because it's out of scope or because it's not actually a bug.
    Once an issue has been marked this way, it is usually then closed.
    When this happens, send the issue's creator a note explaining why the issue won't be addressed and encourage them to
    continue working with the project.

-   *Duplicate*: this issue is a duplicate of one that's already in the system.
    Issues marked this way are usually also then closed;
    this is another opportunity to encourage people to stay involved.

Some of the labels that GitHub creates for repositories by default
are shown in [Figure team labels](teams-labels).
These labels can be modified or otherwise customized for each repository.

```{figure} ../figures/teams/issue-labels.png
:name: teams-labels
Team labels
```

Some projects use labels corresponding to upcoming software releases, journal issues, or conferences instead of 
*Current*, *Next*, and *Eventually*.
This approach works well in the short term, but becomes unwieldy as labels with names like `sprint-2020-08-01` and
`spring-2020-08-16` pile up.

Instead, a project team will usually create a **milestone**, which is a set of issues and pull requests in a single
project repository.
GitHub milestones can have a due date and display aggregate progress toward completion, so the team can easily see when
work is due and how much is left to be done. Teams can also create projects, which can include issues and pull requests
from several repositories as well as notes and reminders for miscellaneous tasks.

### Standardizing workflows 

Adding labels to issues also helps us standardize a workflow for the project.
Conventions about who can do what to issues with various labels,
and who can change those labels, let us define a workflow like the one shown in [Figure teams lifecycle](teams-lifecycle).

```{figure} ../figures/teams/lifecycle.png
:name: teams-lifecycle
Teams lifecycle
```

-   An *Open* issue becomes *Assigned* when someone is made responsible for it.

-   They can then move the issue to *Canceled* if they think it was filed mistakenly
    or doesn't need to be fixed.
    (This is different from closing the issue after working on it.)

-   An *Assigned* issue becomes *Active* when someone starts to work on it.

-   When work is done it becomes *Ready for Review*.

-   From there it is either *Assigned* again because it needs more work
    or moved to *Fixed*,
    which means the change is ready to be incorporated into the project.

-   When the change is actually merged,
    the issue's state is changed to reflect that.

Small projects do not need this much formality,
but when the team is distributed,
contributors need to be able to find out what's going on
without having to wait for someone to respond to email
(or wondering who they *should* have emailed).

## Prioritizing

Between bug reports, feature requests, and general cleanup,
there is always more work to do than time to do it,
so every project needs some way to figure out what to focus on.
Labeling issues helps with **triage**, which is the process of deciding what is a priority and what isn't.
This is never an easy job for software projects that need to balance fixing bugs with creating new features, and is even
more challenging for research projects for which "done" is hard to define or whose team members are widely distributed
or do not all work for the same institution.

Many commercial and open-source teams have adopted **agile development** as a solution to these problems.
Instead of carefully formulating long-term plans that could be derailed by changing circumstances,
agile development uses a sequence of short development **sprints**, each typically one or two weeks long.
Each sprint starts with a planning session lasting one or two hours
in which the successes and failures of the previous sprint are reviewed
and issues to be resolved in the current sprint are selected.
If team members believe an issue is likely to take longer than a single sprint to complete,
it should be broken into smaller pieces that *can* be finished
so that the team can track progress more accurately.
(Something large can be "90% done" for weeks;
with smaller items,
it's easier to see how much headway is being made.)

To decide which issues to work on in the next sprint,
a team can construct an **impact/effort matrix** ([Figure teams impact/effor matrix](teams-impact-effort)).
Impact measures how important the issue is to reaching the team's goals 
and is typically measured on a low--medium--high scale.
(Some teams use ratings from 1 to 10,
but this just leads to arguing over whether something is a 4 or a 5.)
Effort measures how much work the issue requires.
Since this can't always be estimated accurately,
it's common to classify things as "an hour," "a day," or "multiple days."
Again, anything that's likely to take longer than multiple days should be broken down so that planning
and progress tracking can be more accurate.

```{figure} ../figures/teams/effort-impact-matrix.png
:name: teams-impact-effort
Teams impact effort matrix
```

The impact/effort matrix makes the priorities for the coming sprint clear:
anything that is of high importance and requires little effort should be included, while things of low importance that
require a lot of effort should not. The team must still make hard decisions, though:

-   Should a single large high-priority item be done,
    or should several smaller low-priority items be tackled instead?
-   What should be done about medium-priority items that keep being put off?

Each team has to answer these questions for each sprint, but that begs the question of exactly who has the final say in
answering them. In a large project, a **product manager** decides how important items are, while a **project manager**
is responsible for estimating effort and tracking progress.
In a typical research software project, the principal investigator either makes the decision or delegates that
responsibility (and authority) to the lead developer.

Regardless of who is ultimately responsible, it is essential to include project participants in the planning and
decision-making. This may be as simple as having them add **up-votes** and **down-votes** to indicate their opinions on
importance, or as complex as asking them to propose a multi-sprint breakdown of a particularly complex feature.
Doing this shows people that their contributions are valued, which in turn increases their commitment to doing the work.
It also produces better plans, since everyone knows something that someone else doesn't.

## Meetings 

Pull requests and GitHub issues are good tools for asynchronous work,
but team meetings are often a more efficient way to make decisions 
and help build a sense of community.
Knowing how to run a meeting well is as important as knowing how to use version control;
the rules for doing so are simple but rarely followed:

Decide if there actually needs to be a meeting.
:   If the only purpose is to share information,
    have everyone send a brief email instead.
    Remember, people can read faster than they can speak:
    if someone has facts for the rest of the team to absorb,
    the most polite way to communicate them is to type them in.

Write an agenda.
:   If nobody cares enough about the meeting to prepare a point-form list of what's to be discussed,
    the meeting itself probably doesn't need to happen.
    Note that "the agenda is all the open issues in our GitHub repo" doesn't count.

Include timings in the agenda.
:   Timings help prevent early items stealing time from later ones.
    The first estimates with any new group are inevitably optimistic,
    so we should revise them upward for subsequent meetings.
    However,
    we shouldn't have a second or third meeting just because the first one ran over-time:
    instead, we should try to figure out *why* we're running over and fix the underlying problem.

Prioritize.
:   Tackle issues that will have high impact but take little time first,
    and things that will take more time but have less impact later.
    That way, if the first things run over time,
    the meeting will still have accomplished something.

Make one person responsible for keeping things moving.
:   One person should be made moderator
    and be responsible for keeping items to time,
    chiding people who are having side conversations or checking email,
    and asking people who are talking too much to get to the point.
    The moderator should *not* do all the talking:
    in fact,
    whoever is in charge will talk less in a well-run meeting than most other participants.
    This should be a rotating duty among members.

Require politeness.
:   No one gets to be rude,
    no one gets to ramble,
    and if someone goes off topic,
    it's the moderator's job to say,
    "Let's discuss that elsewhere."

No interruptions.
:   Participants should raise a finger, hand,
    put up a sticky note,
    or make another well understood gesture to indicate
    when they want to speak.
    The moderator should keep track of who wants to speak and give them time in turn.

No distractions.
:   Side conversations make meetings less efficient because
    nobody can actually pay attention to two things at once.
    Similarly,
    if someone is checking their email or texting a friend during a meeting,
    it's a clear signal that they don't think the speaker or their work is important.
    This doesn't mean a complete ban on technology---people may need accessibility aids,
    or may be waiting for a call from a dependent---but by default,
    phones should be face down and laptops should be closed
    during in-person meetings.

Take minutes.
:   Someone other than the moderator should take point-form notes
    about the most important information that was shared,
    and about every decision that was made or every task that was assigned to someone.
    This should be a rotating duty among members.

End early.
:   If the meeting is scheduled for 10:00--11:00,
    aim to end at 10:50 to give people a break before whatever they're doing next.

As soon as the meeting is over,
circulate the minutes by emailing them to everyone or adding a text file to the project's repository:

People who weren't at the meeting can follow what's going on.
:   We all have to juggle tasks from several projects or courses,
    which means that sometimes we can't make it to meetings.
    Checking a written record
    is a more accurate and efficient way to catch up than asking a colleague,
    "So, what did I miss?"

Everyone can check what was actually said or promised.
:   More than once,
    one of us has looked over the minutes of a meeting and thought,
    "Did I say that?" or,
    "I didn't promise to have it ready then!"
    Accidentally or not,
    people will often remember things differently;
    writing them down gives everyone a chance to correct mistakes,
    misinterpretations,
    or misrepresentations.

People can be held accountable at subsequent meetings.
:   There's no point making lists of questions and action items
    if we don't follow up on them later.
    If we are using an issue-tracking system,
    we should create a ticket for each new question or task right after the meeting
    and update those that are being carried forward.
    This helps a lot when the time comes to draw up the agenda for the next meeting.

### Air time 

One of the problems in a synchronous meeting
is the tendency of some people to speak far more than others.
Other meeting members may be so accustomed to this
that they don't speak up even when they have valuable points to make.

One way to combat this is to give everyone **three sticky notes** at the start of the meeting.
Every time they speak, they have to give up one sticky note.
When they're out of stickies,
they aren't allowed to speak until everyone has used at least one,
at which point everyone gets all of their sticky notes back.
This ensures that nobody talks more than three times as often as
the quietest person in the meeting,
and completely changes group dynamics.
People who have given up trying to be heard
suddenly have space to contribute,
and the overly frequent speakers realize how unfair they have been.

Another useful technique is called **interruption bingo**.
Draw a grid and label the rows and columns with the participants' names.
Each time one person interrupts another, add a tally mark to the appropriate cell; halfway through the meeting,
take a moment to look at the results.
In most cases it will be clear that
one or two people are doing all of the interrupting.
After that, saying, "All right, I'm adding another tally to the bingo card,"
is often enough to get them to throttle back.

### Online meetings 

Online meetings provide special challenges,
both in the context of regulating how often individuals speak,
as well as running meetings in general.
{cite:p}`Troy2018` discusses why online meetings are often frustrating and unproductive and
points out that in most online meetings,
the first person to speak during a pause gets the floor.
As a result,
"If you have something you want to say,
you have to stop listening to the person currently speaking
and instead focus on when they're gonna pause or finish
so you can leap into that nanosecond of silence and be the first to utter something.
The format...encourages participants who want to contribute
to say more and listen less."

The solution is to run a text chat besides the video conference
where people can signal that they want to speak.
The moderator can then select people from the waiting list.
This practice can be reinforced by having everyone mute themselves 
and only allowing the moderator to unmute people.
{cite:p}`Broo2016` has many other useful suggestions for managing meetings.

## Making Decisions 

The purpose of a well-run meeting is to make decisions,
so sooner or later,
the members of a project must decide who has a say in what.
The first step is to acknowledge that every team has a power structure:
the question is whether it's formal or informal---in other words,
whether it's accountable or unaccountable {cite:p}`Free1972`.
The latter can work for groups of up to half a dozen people
in which everyone knows everyone else.
Beyond that, groups need to spell out
who has the authority to make which decisions
and how to achieve consensus.
In short, they need explicit **governance**. **Martha's Rules** are a practical way to do this in groups of up to a few
dozen members {cite:p}`Mina1986`:

1.  Before each meeting, anyone who wishes may sponsor a proposal.
    Proposals must be filed at least 24 hours before a meeting
    in order to be considered at that meeting and must include:
    -   a one-line summary
    -   the full text of the proposal
    -   any required background information
    -   pros and cons
    -   possible alternatives

2.  A quorum is established in a meeting if half or more of voting members are present.

3.  Once a person has sponsored a proposal, they are responsible for it.
    The group may not discuss or vote on the issue unless the sponsor or their delegate is present.
    The sponsor is also responsible for presenting the item to the group.

4.  After the sponsor presents the proposal,
    a sense vote is cast for the proposal prior to any discussion:
    -   Who likes the proposal?
    -   Who can live with the proposal?
    -   Who is uncomfortable with the proposal?

5.  If all of the group likes or can live with the proposal,
    it passes with no further discussion.

6.  If most of the group is uncomfortable with the proposal,
    it is sent back to its sponsor for further work.
    (The sponsor may decide to drop it if it's clear that
    the majority isn't going to support it.)

7.  If some members are uncomfortable with the proposal,
    a timer is set for a brief discussion moderated by the meeting moderator.
    After 10 minutes or when no one has anything further to add,
    the moderator calls for a straight yes-or-no vote on the question:
    "Should we implement this decision over the stated objections?"
    If a majority votes "yes" the proposal is implemented.
    Otherwise, it is returned to the sponsor for further work.

Every group that uses Martha's Rules must make two procedural decisions:

How are proposals put forward?
:   In a software development project,
    the easiest way is to file an issue in the project's GitHub repository
    tagged *Proposal*,
    or to create a pull request containing a single file
    with the text of the proposal.
    Team members can then comment on the proposal,
    and the sponsor can revise it
    before bringing it to a vote.

Who gets to vote?
:   The usual answer is "whoever is working on the project,"
    but as it attracts more volunteer contributors,
    a more explicit rule is needed.
    One common method is for existing members to nominate new ones,
    who are then voted in (or not) using the process described above.

## Make All This Obvious to Newcomers 

Rules that people don't know about can't help them.
Once your team agrees on a project structure,
a workflow, how to get items on a meeting agenda, or how to make decisions, you should therefore take the time to
document this for newcomers. 
This information may be included as sections in the existing `README` file or put into files of their own:

-   `CONTRIBUTING`
    explains how to contribute,
    i.e.,
    what naming conventions to use for functions,
    what tags to put on issues (Section [teams planning]( https://se-up.github.io/RSE-UP/chapters/working_in_teams.html#planning)),
    or how to install and configure the software needed to start work on the project.
    These instructions can also be included as a section in `README`;
    wherever they go,
    remember that the easier it is for people to get set up and contribute,
    the more likely they are to do so {cite:p}`Stei2014`.
te
-   `GOVERNANCE`
    explains how the project is run (Section [teams martha](https://se-up.github.io/RSE-UP/chapters/working_in_teams.html#making-decisions)).
    It is still uncommon for this to be in a file of its own---it is more often included
    in `README` or `CONTRIBUTING`---but open communities have learned the hard way
    that *not* being explicit about who has a voice in decisions
    and how contributors can tell what decisions have been made
    causes trouble sooner or later.

Having these files helps new contributors orient themselves
and also signals that the project is well run.

## Handling Conflict

You just missed an important deadline, and people are unhappy.
The sick feeling in the pit of your stomach has turned to anger:
you did *your* part, but Sylvie didn't finish her stuff until the very last minute, which meant that no one else had
time to spot the two big mistakes she'd made. As for Cho, he didn't deliver at all---again.
If something doesn't change, contributors are going to start looking for a new project.

Conflicts like this come up all the time.
Broadly speaking, there are four ways we can deal with them:

1.  Cross our fingers and hope that things will get better on their own,
    even though they didn't the last three times.

2.  Do extra work to make up for others' shortcomings.
    This saves us the mental anguish of confronting others in the short run,
    but the time for that "extra" has to come from somewhere.
    Sooner or later,
    our personal lives or other parts of the project will suffer.

3.  Lose our temper.
    People often wind up displacing anger into other parts of their life:
    they may yell at someone for taking an extra thirty seconds to make a change
    when what they really need to do is tell their boss
    that they won't work through another holiday weekend
    to make up for management's decision to short-staff the project.

4.  Take constructive steps to fix the underlying problem.

Most of us find the first three options easiest, even though they don't actually fix the problem. The fourth option is
harder because we don't like confrontation. If we manage it properly, though,
it is a lot less bruising, which means that we don't have to be as afraid of initiating it. Also, if people believe that
we will take steps when they bully, lie, procrastinate, or do a half-assed job, they will usually avoid making it
necessary.

Make sure we are not guilty of the same sin.
:   We won't get very far complaining about someone else interrupting in meetings
    if we do it just as frequently.

Check expectations.
:   Are we sure the offender knows what standards they are supposed to be meeting?
    This is where things like job descriptions
    or up-front discussion of who's responsible for what
    come in handy.

Check the situation.
:   Is someone dealing with an ailing parent or immigration woes?
    Have they been put to work on three other projects that we don't know about?
    Use open questions like, "Can you help me understand this?" when checking in.
    This gives them the freedom to explain something you may not have expected,
    and avoids the pressure of being asked directly about something they don't want to explain.

Document the offense.
:   Write down what the offender has actually done and why it's not good enough.
    Doing this helps us clarify what we're upset about
    and is absolutely necessary if we have to escalate.

Check with other team members.
:   Are we alone in feeling that the offender is letting the team down?
    If so, we aren't necessarily wrong,
    but it'll be a lot easier to fix things if we have the support of the rest of the team.
    Finding out who else on the team is unhappy can be the hardest part of the whole process:
    We can't even ask the question without letting on that we are upset,
    and word will almost certainly get back to whoever we are asking about,
    who might then accuse us of stirring up trouble.

Talk with the offender.
:   This should be a team effort:
    put it on the agenda for a team meeting,
    present the complaint,
    and make sure that the offender understands it.
    Doing this once is often enough:
    if someone realizes that they're going to be called on their hitchhiking or bad manners,
    they will usually change their ways.

Escalate as soon as there's a second offense.
:   People who don't have good intentions
    count on us giving them one last chance after another
    until the project is finished and they can go suck the life out of their next victim.
    *Don't fall into this trap.*
    If someone stole a laptop, we would report it right away.
    If someone steals time,
    we are being foolish if we give them a chance to do it again and again.

In academic research projects,
"escalation" means "taking the issue to the project's principal investigator."
Of course,
the PI has probably had dozens of students complain to her over the years
about teammates not doing their share,
and it isn't uncommon to have both halves of a pair tell the supervisor that they're doing all the work.
(This is yet another reason to use version control:
it makes it easy to check who's actually written what.)
In order to get her to take us seriously and help us fix our problem,
we should send her an email signed by several people
that describes the problem and the steps we have already taken to resolve it.
Make sure the offender gets a copy as well,
and ask the supervisor to arrange a meeting to resolve the issue.

> **Hitchhikers**
>
> Hitchhikers who show up but never actually do anything
> are particularly difficult to manage,
> in part because they are usually very good at appearing reasonable.
> They will nod as we present our case,
> then say, "Well, yes, but..." and list a bunch of minor exceptions
> or cases where others on the team have also fallen short of expectations.
> Having collaborator guidelines (Section [teams coc](https://se-up.github.io/RSE-UP/chapters/working_in_teams.html#teams-coc))
> and tracking progress (Section [teams workflow](https://se-up.github.io/RSE-UP/chapters/working_in_teams.html#teams-workflow))
> are essential for handling them.
> If we can't back up our complaint,
> our supervisor will likely be left with the impression that the whole team is dysfunctional.

What can we do if conflict becomes more personal and heated,
especially if it relates to violations of our Code of Conduct?
A few simple guidelines will go a long way:

1.  Be short, simple, and firm.

2.  Don't try to be funny.
    It almost always backfires, or will later be used against us.

3.  Play for the audience.
    We probably won't change the person we are calling out,
    but we might change the minds or strengthen the resolve of people who are observing.

4.  Pick our battles.
    We can't challenge everyone, every time,
    without exhausting ourselves and deafening our audience.
    An occasional sharp retort will be much more effective than constant criticism.

5.  Don't shame or insult one group when trying to help another.
    For example,
    don't call someone stupid
    when what we really mean is that they're racist or homophobic.

[Captain Awkward](https://captainawkward.com/) has useful advice for discussions like these, and [Charles' Rules of Argument](https://geekfeminism.wikia.com/wiki/Charles%27_Rules_of_Argument)
are very useful online.

Finally, it's important to recognize that good principles sometimes conflict.
For example, consider this scenario:

> A manager consistently uses male pronouns to refer to software and people of unknown gender.
> When you tell them it makes you uncomfortable to treat maleness as the norm,
> they say that male is the default gender in their first language
> and you should be more considerate of people from other cultures.

On the one hand, we want to respect other people's cultures;
on the other hand, we want to be inclusive of women.
In this case, the manager's discomfort about changing pronouns
matters less than the career harm caused by them being exclusionary,
but many cases are not this clear-cut.

## Summary 

This chapter was the hardest in this book to write, but is probably also the most important. A project can survive bad
code or stumbles with Git, but not confusion and interpersonal conflict. Collaboration and management become easier with
practice, and everything you learn from taking part in research software projects will help other things you do as well.

## Keypoints

```{include} keypoints/teams.md

```

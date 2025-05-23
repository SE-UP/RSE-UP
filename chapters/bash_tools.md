# Building Tools with the Unix Shell 


> Wisdom comes from experience. Experience is often a result of lack of wisdom.
>
> --- Terry Pratchett

The shell's greatest strength is that
it lets us combine programs to create pipelines
that can handle large volumes of data.
This lesson shows how to do that,
and how to repeat commands to process as many files as we want automatically.

 

We'll be working with `zipf` project (found [here](https://gitup.uni-potsdam.de/se-up/rse_course/rse_course_materials)), which should contain the following files:

```text
zipf/
└── data
    ├── dracula.txt
    ├── frankenstein.txt
    ├── jane_eyre.txt
    ├── moby_dick.txt
    ├── sense_and_sensibility.txt
    ├── sherlock_holmes.txt
    └── time_machine.txt
```

## Combining Commands 

To see how the shell lets us combine commands, let's go into the `zipf/data` directory and count the number of lines in each file once again:

```bash
$ cd ~/zipf/data
$ wc -l *.txt
```

```text

  15975 dracula.txt
   7832 frankenstein.txt
  21054 jane_eyre.txt
  22331 moby_dick.txt
  13028 sense_and_sensibility.txt
  13053 sherlock_holmes.txt
   3582 time_machine.txt
  96855 total
```

Which of these books is shortest?
We can check by eye when there are only seven files, but what if there were eight thousand?

Our first step toward a solution is to run this command:

```bash
$ wc -l *.txt > lengths.txt
```

The greater-than symbol `>` tells the shell
to **redirect** the command's output to a file instead of printing it. 
Nothing appears on the screen; instead, everything that would have appeared has gone into the file `lengths.txt`. The shell creates this file if it doesn't exist, or overwrites it if it already exists.

We can print the contents of `lengths.txt` using `cat`, which is short for con**cat**enate (because if we give it the names of several files
it will print them all in order):

```bash
$ cat lengths.txt
```

```text
  15975 dracula.txt
   7832 frankenstein.txt
  21054 jane_eyre.txt
  22331 moby_dick.txt
  13028 sense_and_sensibility.txt
  13053 sherlock_holmes.txt
   3582 time_machine.txt
  96855 total
```

We can now use `sort` to sort the lines in this file:


```bash
$ sort -n lengths.txt
```

```text
   3582 time_machine.txt
   7832 frankenstein.txt
  13028 sense_and_sensibility.txt
  13053 sherlock_holmes.txt
  15975 dracula.txt
  21054 jane_eyre.txt
  22331 moby_dick.txt
  96855 total

```

Just to be safe,
we use `sort`'s `-n` option to specify that we want to sort numerically.
Without it,
`sort` would order things alphabetically
so that `10` would come before `2`.

`sort` does not change `lengths.txt`.
Instead,
it sends its output to the screen just as `wc` did.
We can therefore put the sorted list of lines in another temporary file called `sorted-lengths.txt`
using `>` once again:

```bash
$ sort -n lengths.txt > sorted-lengths.txt
```

> **Redirecting to the Same File**
>
> It's tempting to send the output of `sort` back to the file it reads:
>
> ```bash
> $ sort -n lengths.txt > lengths.txt
> ```
>
> However, all this does is wipe out the contents of `lengths.txt`.
> The reason is that when the shell sees the redirection,
> it opens the file on the right of the `>` for writing,
> which erases anything that file contained.
> It then runs `sort`, which finds itself reading from a newly empty file.

Creating intermediate files with names like `lengths.txt` and `sorted-lengths.txt` works,
but keeping track of those files and cleaning them up when they're no longer needed is a burden.
Let's delete the two files we just created:

```bash
$ rm lengths.txt sorted-lengths.txt
```

We can produce the same result more safely and with less typing
using a **pipe**.

```bash
$ wc -l *.txt | sort -n
```

```text
   3582 time_machine.txt
   7832 frankenstein.txt
  13028 sense_and_sensibility.txt
  13053 sherlock_holmes.txt
  15975 dracula.txt
  21054 jane_eyre.txt
  22331 moby_dick.txt
  96855 total
```

The vertical bar `|` between the `wc` and `sort` commands
tells the shell that we want to use the output of the command on the left
as the input to the command on the right.

Running a command with a file as input has a clear flow of information:
the command performs a task on that file and prints the output to the screen
([](bash_tools_piper) a).
When using pipes, however,
the information flows differently after the first (upstream) command.
The downstream command doesn't read from a file.
Instead,
it reads the output of the upstream command
([](bash_tools_piper) b).


```{figure} ../figures/bash-tools/pipe.png
:name: bash_toots_piper

Bash tool pipe
```

We can use `|` to build pipes of any length.
For example, we can use the command `head` to get just the first three lines of sorted data, which shows us the three shortest books:

```bash
$ wc -l *.txt | sort -n | head -n 3
```

```text
   3582 time_machine.txt
   7832 frankenstein.txt
  13028 sense_and_sensibility.txt
```

> **Options Can Have Values**
>
> When we write `head -n 3`,
> the value 3 is not input to `head`.
> Instead, it is associated with the option `-n`.
> Many options take values like this,
> such as the names of input files or the background color to use in a plot.
> Some versions of `head` may allow you to use `head -3` as a shortcut,
> though this can be confusing if other options are included.

We could always redirect the output to a file
by adding `> shortest.txt` to the end of the pipeline,
thereby retaining our answer for later reference.

In practice,
most Unix users would create this pipeline step by step,
just as we have:
by starting with a single command and adding others one by one,
checking the output after each change.
The shell makes this easy
by letting us move up and down in our **command history**
with the <kbd>↑</kbd> and <kbd>↓</kbd> keys.
We can also edit old commands to create new ones,
so a very common sequence is:

-   Run a command and check its output.
-   Use <kbd>↑</kbd> to bring it up again.
-   Add the pipe symbol `|` and another command to the end of the line.
-   Run the pipe and check its output.
-   Use <kbd>↑</kbd> to bring it up again.
-   And so on.

## How Pipes Work 

In order to use pipes and redirection effectively,
we need to know a little about how they work.
When a computer runs a program---any program---it creates a **process**
to hold the program's instructions and data.
Every process in Unix has an input channel called **stdin** - **standard input** and an output channel called **standard output** - **stdout**
(By now you may be surprised that their names are so memorable,
but don't worry: most Unix programmers call them "stdin" and "stdout",
which are pronounced "stuh-Din" and "stuh-Dout").

The shell is a program like any other,
and like any other,
it runs inside a process.
Under normal circumstances its standard input is connected to our keyboard
and its standard output to our screen,
so it reads what we type
and displays its output for us to see ([](standard_io) a).
When we tell the shell to run a program,
it creates a new process
and temporarily reconnects the keyboard and stream
to that process's standard input and output ([](standard_io) b).

```{figure} ../figures/bash-tools/standard-io.png
:name: standard_io

Bash tools stdio
```

If we provide one or more files for the command to read,
as with `sort lengths.txt`, the program reads data from those files.
If we don't provide any filenames, though, the Unix convention is for the program to read from standard input.
We can test this by running `sort` on its own, typing in a few lines of text,
and then pressing <kbd>Ctrl</kbd>+<kbd>D</kbd> to signal the end of input .
`sort` will then sort and print whatever we typed:

```bash
$ sort
one
two
three
four
^D
```

```text
four
one
three
two
```

Redirection with `>` tells the shell to connect the program's standard output to a file instead of the screen ([](bash_tools_stdio) c).

When we create a pipe like `wc *.txt | sort`, the shell creates one process for each command so that `wc` and `sort` will run simultaneously, and then connects the standard output of `wc` directly to the standard input of `sort` ([](bash_tools_stdio) d).

`wc` doesn't know whether its output is going to the screen, another program,
or to a file via `>`. 
Equally, `sort` doesn't know if its input is coming from the keyboard or another process; it just knows that it has to read, sort, and print.

> **Why Isn't It Doing Anything?**
>
> What happens if a command is supposed to process a file
> but we don't give it a filename?
> For example, what if we type:
>
> ```bash
> $ wc -l
> ```
>
> but don't type `*.txt` (or anything else) after the command?
> Since `wc` doesn't have any filenames,
> it assumes it is supposed to read from the keyboard,
> so it waits for us to type in some data.
> It doesn't tell us this;
> it just sits and waits.
>
> This mistake can be hard to spot,
> particularly if we put the filename at the end of the pipeline:
>
> ```bash
> $ wc -l | sort moby_dick.txt
> ```
>
> In this case,
> `sort` ignores standard input and reads the data in the file,
> but `wc` still just sits there waiting for input.
>
> If we make this mistake,
> we can end the program by typing <kbd>Ctrl</kbd>+<kbd>C</kbd>.
> We can also use this to interrupt programs that are taking a long time to run
> or are trying to connect to a website that isn't responding.



Just as we can redirect standard output with `>`,
we can connect standard input to a file using `<`.
In the case of a single file,
this has the same effect as providing the file's name to the `wc` command:

```bash
$ wc < moby_dick.txt
```

```text
    22331  215832 1276222
```

If we try to use redirection with a wildcard,
though,
the shell *doesn't* concatenate all of the matching files:

```bash
$ wc < *.txt
```

```text
-bash: *.txt: ambiguous redirect
```

It also doesn't print the error message to standard output,
which we can prove by redirecting:

```bash
$ wc < *.txt > all.txt
```

```text
-bash: *.txt: ambiguous redirect
```

```bash
$ cat all.txt
```

```text
cat: all.txt: No such file or directory
```

Instead, every process has a second output channel called **standard error**.
Programs use it for error messages so that their attempts to tell us something has gone wrong don't vanish silently into an output file.
There are ways to redirect standard error, but doing so is almost always a bad idea.

## Repeating Commands on Many Files 

A loop is a way to repeat a set of commands for each item in a list.
We can use them to build complex workflows out of simple pieces, and (like wildcards) they reduce the typing we have to do and the number of mistakes we might make.

Let's suppose that we want to take a section out of each book
whose name starts with the letter "s" in the `data` directory.
More specifically,
suppose we want to get the first 8 lines of each book
*after* the 9 lines of license information that appear at the start of the file.
If we only cared about one file,
we could write a pipeline to take the first 17 lines
and then take the last 8 of those:

```bash
$ head -n 17 sense_and_sensibility.txt | tail -n 8
```

```text
Title: Sense and Sensibility

Author: Jane Austen
Editor:
Release Date: May 25, 2008 [EBook #161]
Posting Date:
Last updated: February 11, 2015
Language: English
```

If we try to use a wildcard to select files,
we only get 8 lines of output,
not the 16 we expect:

```bash
$  head -n 17 s*.txt | tail -n 8
```

```text
Title: The Adventures of Sherlock Holmes

Author: Arthur Conan Doyle
Editor:
Release Date: April 18, 2011 [EBook #1661]
Posting Date: November 29, 2002
Latest Update:
Language: English
```

The problem is that `head` is producing a single stream of output
containing 17 lines for each file
(along with a header telling us the file's name):

```bash
$ head -n 17 s*.txt
```

```text
==> sense_and_sensibility.txt <==
The Project Gutenberg EBook of Sense and Sensibility, by ...

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it ...
re-use it under the terms of the Project Gutenberg License ...
with this eBook or online at www.gutenberg.net



Title: Sense and Sensibility

Author: Jane Austen
Editor:
Release Date: May 25, 2008 [EBook #161]
Posting Date:
Last updated: February 11, 2015
Language: English

==> sherlock_holmes.txt <==
Project Gutenberg's The Adventures of Sherlock Holmes, by Arthur
Conan Doyle

This eBook is for the use of anyone anywhere at no cost and ...
almost no restrictions whatsoever.  You may copy it, give ...
re-use it under the terms of the Project Gutenberg License ...
with this eBook or online at www.gutenberg.net



Title: The Adventures of Sherlock Holmes

Author: Arthur Conan Doyle
Editor:
Release Date: April 18, 2011 [EBook #1661]
Posting Date: November 29, 2002
Latest Update:
Language: English
```

Let's try this instead:

```bash
$ for filename in sense_and_sensibility.txt sherlock_holmes.txt
> do
>   head -n 17 $filename | tail -n 8
> done
```

```text
Title: Sense and Sensibility

Author: Jane Austen
Editor:
Release Date: May 25, 2008 [EBook #161]
Posting Date:
Last updated: February 11, 2015
Language: English
Title: The Adventures of Sherlock Holmes

Author: Arthur Conan Doyle
Editor:
Release Date: April 18, 2011 [EBook #1661]
Posting Date: November 29, 2002
Latest Update:
Language: English
```

As the output shows,
the loop runs our pipeline once for each file.
There is a lot going on here,
so we will break it down into pieces:

1.  The keywords `for`, `in`, `do`, and `done` create the loop,
    and must always appear in that order.

2.  `filename` is a variable just like a variable in Python.
    At any moment it contains a value,
    but that value can change over time.

3.  The loop runs once for each item in the list.
    Each time it runs,
    it assigns the next item to the variable.
    In this case, `filename` will be `sense_and_sensibility.txt`
    the first time around the loop
    and `sherlock_holmes.txt` the second time.

4.  The commands that the loop executes are called the **body** and
    appear between the keywords `do` and `done`.
    Those commands use the current value of the variable `filename`,
    but to get it,
    we must put a dollar sign `$` in front of the variable's name.
    If we forget and use `filename` instead of `$filename`,
    the shell will think that we are referring to a file
    that is actually called `filename`.

5.  The shell prompt changes from `$`
    to a **continuation prompt** `>` as we type in our loop.
    to remind us that we haven't finished typing a complete command yet.
    We don't type the `>`,
    just as we don't type the `$`.
    The continuation prompt `>` has nothing to do with redirection;
    it's used because there are only so many punctuation symbols available.

> **Continuation Prompts May Differ Too**
>
> As mentioned in Chapter [Bash Basics](https://se-up.github.io/RSE-UP/chapters/bash_basics.html),
> there is variation in how different shells look and operate.
> If you noticed the second, third, and fourth code lines
> in your for loop were prefaced with `for`,
> it's not because you did something wrong!
> That difference is one of the ways in which `zsh` differs from `bash`.

It is very common to use a wildcard to select a set of files
and then loop over that set to run commands:

```bash
$ for filename in s*.txt
> do
>   head -n 17 $filename | tail -n 8
> done
```

```text
Title: Sense and Sensibility

Author: Jane Austen
Editor:
Release Date: May 25, 2008 [EBook #161]
Posting Date:
Last updated: February 11, 2015
Language: English



Title: The Adventures of Sherlock Holmes

Author: Arthur Conan Doyle
Editor:
Release Date: April 18, 2011 [EBook #1661]
Posting Date: November 29, 2002
Latest Update:
Language: English
```

## Variable Names 

We should always choose meaningful names for variables,
but we should remember that those names don't mean anything to the computer.
For example,we have called our loop variable `filename`
to make its purpose clear to human readers, but we could equally well write our loop as:

```bash
$ for x in s*.txt
> do
>   head -n 17 $x | tail -n 8
> done
```

or as:

```bash
$ for username in s*.txt
> do
>   head -n 17 $username | tail -n 8
> done
```

*Don't do this.*
Programs are only useful if people can understand them,
so meaningless names like `x` and misleading names like `username`
increase the odds of misunderstanding.

## Redoing Things

Loops are useful if we know in advance what we want to repeat,
but we can also repeat commands that we have run recently.
One way is to use <kbd>↑</kbd> and <kbd>↓</kbd>
to go up and down in our command history as described earlier.
Another is to use `history` to get a list of the last few hundred commands we have run:

```bash
$ history
```

```text
  551  wc -l *.txt | sort -n
  552  wc -l *.txt | sort -n | head -n 3
  553  wc -l *.txt | sort -n | head -n 1 > shortest.txt
```

We can use an exclamation mark `!` followed by a number
to repeat a recent command:

```bash
$ !552
```

```bash
wc -l *.txt | sort -n | head -n 3
```

```text
   3582 time_machine.txt
   7832 frankenstein.txt
  13028 sense_and_sensibility.txt
```

The shell prints the command it is going to re-run to standard error
before executing it,
so that (for example) `!572 > results.txt`
puts the command's output in a file
*without* also writing the command to the file.

Having an accurate record of the things we have done
and a simple way to repeat them
are two of the main reasons people use the Unix shell.
In fact,
being able to repeat history is such a powerful idea
that the shell gives us several ways to do it:

-   `!head` re-runs the most recent command starting with `head`,
    while `!wc` re-runs the most recent starting with `wc`.
-   If we type <kbd>Ctrl</kbd>+<kbd>R</kbd> (for **r**everse search)
    the shell searches backward through its history for whatever we type next.
    If we don't like the first thing it finds,
    we can type <kbd>Ctrl</kbd>+<kbd>R</kbd> again to go further back.

If we use `history`, <kbd>↑</kbd>, or <kbd>Ctrl</kbd>+<kbd>R</kbd>
we will quickly notice that loops don't have to be broken across lines.
Instead,
their parts can be separated with semi-colons:

```bash
$ for filename in s*.txt; do head -n 17 $filename | tail -n 8;
done
```

This is fairly readable,
though it becomes more challenging if our for loop includes multiple commands.
For example,
we may choose to include the `echo` command,
which prints its arguments to the screen,
so we can keep track of progress or for debugging.
Compare this:

```bash
$ for filename in s*.txt
> do
>   echo $filename
>   head -n 17 $filename | tail -n 8
> done
```

with this:

```bash
$ for filename in s*.txt; do echo $filename; head -n 17 $filename
  | tail -n 8; done
```

Even experienced users have a tendency to (incorrectly) 
put the semi-colon after `do` instead of before it.
If our loop contains multiple commands,
though,
the multi-line format is much easier to read and troubleshoot.
Note that (depending on the size of your shell window)
the format separated by semi-colons may be printed onto more than one line,
as shown in the previous code example.
You can tell whether code entered into your shell 
is intended to be run as a single line based on the prompt:
both the original command prompt (`$`) and the continuation prompt (`>`) 
indicate the code is on separate lines;
the absence of either in shell commands indicates it is a single line of code.

## Creating New Filenames Automatically 

Suppose we want to create a backup copy of each book whose name ends in "e".
If we don't want to change the files' names,
we can do this with `cp`:

```bash
$ cd ~/zipf
$ mkdir backup
$ cp data/*e.txt backup
$ ls backup
```

```text
jane_eyre.txt  time_machine.txt
```

> **Warnings**
>
> If you attempt to re-execute the code chunk above,
> you'll end up with an error after the second line:
>
> ```text
> mkdir: backup: File exists
> ```
>
> This warning isn't necessarily a cause for alarm.
> It lets you know that the command couldn't be completed,
> but will not prevent you from proceeding.

But what if we want to append the extension `.bak` to the files' names?
`cp` can do this for a single file:

```bash
$ cp data/time_machine.txt backup/time_machine.txt.bak
```

but not for all the files at once:

```bash
$ cp data/*e.txt backup/*e.txt.bak
```

```text
cp: target 'backup/*e.txt.bak' is not a directory
```

`backup/*e.txt.bak` doesn't match anything---those files don't yet exist---so
after the shell expands the `*` wildcards,
what we are actually asking `cp` to do is:

```bash
$ cp data/jane_eyre.txt data/time_machine.txt backup/*e.bak
```

This doesn't work because `cp` only understands how to do two things:
copy a single file to create another file,
or copy a bunch of files into a directory.
If we give it more than two names as arguments,
it expects the last one to be a directory.
Since `backup/*e.bak` is not,
`cp` reports an error.

Instead,
let's use a loop to copy files to the backup directory
and append the `.bak` suffix:

```bash
$ cd data
$ for filename in *e.txt
> do
>   cp $filename ../backup/$filename.bak
> done
$ ls ../backup
```

```text
jane_eyre.txt.bak  time_machine.txt.bak
```

## Summary 

The Shell's greatest strength is the way it combines a few powerful ideas with pipes and loops.
The next chapter will show how we can make our work more reproducible
by saving commands in files that we can run over and over again.

## Exercises 

The exercises below involve creating and moving new files,
as well as considering hypothetical files.
Please note that if you create or move any files or directories in your Zipf's Law project,
you may want to reorganize your files following the outline at the beginning of the next chapter.
If you accidentally delete necessary files,
you can start with a fresh copy of the data files
by following the instructions in Section [Downloading the Data](https://se-up.github.io/RSE-UP/chapters/getting_started#downloading-the-data).

### What does `>>` mean? 

We have seen the use of `>`, but there is a similar operator `>>` which works slightly differently.
We'll learn about the differences between these two operators by printing some strings. We can use the `echo` command to print strings as shown below:


```bash
$ echo The echo command prints text
```

```text
The echo command prints text
```

Now test the commands below to reveal the difference between the two operators:

```bash
$ echo hello > testfile01.txt
```

and:

```bash
$ echo hello >> testfile02.txt
```

Hint: Try executing each command twice in a row and then examining the output files.

### Appending data 

Given the following commands,
what will be included in the file `extracted.txt`:

```bash
$ head -n 3 dracula.txt > extracted.txt
$ tail -n 2 dracula.txt >> extracted.txt
```

1. The first three lines of `dracula.txt`
2. The last two lines of `dracula.txt`
3. The first three lines and the last two lines of `dracula.txt`
4. The second and third lines of `dracula.txt`

### Piping commands

In our current directory, we want to find the 3 files which have the least number of
lines. Which command listed below would work?

1. `wc -l * > sort -n > head -n 3`
2. `wc -l * | sort -n | head -n 1-3`
3. `wc -l * | head -n 3 | sort -n`
4. `wc -l * | sort -n | head -n 3`

### Why does `uniq` only remove adjacent duplicates? 

The command `uniq` removes adjacent duplicated lines from its input.
Consider a hypothetical file `genres.txt` containing the following data:

```text
science fiction
fantasy
science fiction
fantasy
science fiction
science fiction
```

Running the command `uniq genres.txt` produces:

```text
science fiction
fantasy
science fiction
fantasy
science fiction
```

Why do you think `uniq` only removes *adjacent* duplicated lines?
(Hint: think about very large datasets.) What other command could
you combine with it in a pipe to remove all duplicated lines?

### Pipe reading comprehension 

A file called `titles.txt` contains a list of book titles and publication years:

```text
Dracula,1897
Frankenstein,1818
Jane Eyre,1847
Moby Dick,1851
Sense and Sensibility,1811
The Adventures of Sherlock Holmes,1892
The Invisible Man,1897
The Time Machine,1895
Wuthering Heights,1847
```

What text passes through each of the pipes and the final redirect in the pipeline below?

```bash
$ cat titles.txt | head -n 5 | tail -n 3 | sort -r > final.txt
```

Hint: build the pipeline up one command at a time to test your understanding

### Pipe construction 

For the file `titles.txt` from the previous exercise, consider the following command:

```bash
$ cut -d , -f 2 titles.txt
```

What does the `cut` command (and its options) accomplish?

### Which pipe? 

Consider the same `titles.txt` from the previous exercises.

The `uniq` command has a `-c` option which gives a count of the
number of times a line occurs in its input.
If `titles.txt` was in your working directory,
what command would you use to produce
a table that shows the total count of each publication year in the file?

1.  `sort titles.txt | uniq -c`
2.  `sort -t, -k2,2 titles.txt | uniq -c`
3.  `cut -d, -f 2 titles.txt | uniq -c`
4.  `cut -d, -f 2 titles.txt | sort | uniq -c`
5.  `cut -d, -f 2 titles.txt | sort | uniq -c | wc -l`

### Doing a dry run 

A loop is a way to do many things at once---or to make many mistakes at
once if it does the wrong thing. One way to check what a loop *would* do
is to `echo` the commands it would run instead of actually running them.

Suppose we want to preview the commands the following loop will execute
without actually running those commands
(`analyze` is a hypothetical command):

```bash
$ for file in *.txt
> do
>   analyze $file > analyzed-$file
> done
```

What is the difference between the two loops below,
and which one would we want to run?

```bash
$ for file in *.txt
> do
>   echo analyze $file > analyzed-$file
> done
```

or:

```bash
$ for file in *.txt
> do
>   echo "analyze $file > analyzed-$file"
> done
```

### Variables in loops

Given the files in `data/`,
what is the output of the following code?

```bash
$ for datafile in *.txt
> do
>    ls *.txt
> done
```

Now, what is the output of the following code?

```bash
$ for datafile in *.txt
> do
>	ls $datafile
> done
```

Why do these two loops give different outputs?

### Limiting sets of files

What would be the output of running the following loop in your `data/` directory?

```bash
$ for filename in d*
> do
>    ls $filename
> done
```

How would the output differ from using this command instead?

```bash
$ for filename in *d*
> do
>    ls $filename
> done
```

### Saving to a file in a loop 

Consider running the following loop in the  `data/` directory:

```bash
for book in *.txt
> do
>     echo $book
>     head -n 16 $book > headers.txt
> done
```

Why would the following loop be preferable?

```bash
for book in *.txt
> do
>     head -n 16 $book >> headers.txt
> done
```



### Why does `history` record commands before running them? 

If you run the command:

```bash
$ history | tail -n 5 > recent.sh
```

the last command in the file is the `history` command itself, i.e.,
the shell has added `history` to the command log before actually
running it. In fact, the shell *always* adds commands to the log
before running them. Why do you think it does this?

## Key Points

```{include} keypoints/bash_tools.md

```

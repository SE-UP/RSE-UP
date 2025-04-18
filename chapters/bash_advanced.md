# Bash Advanced 

> There isn't a way things should be. There's just what happens, and what we do.
>
> --- Terry Pratchett

The previous chapters explained how we can use the command line
to do all of the things we can do with a GUI,
and how to combine commands in new ways using pipes and redirection.
This chapter extends those ideas to show
how we can create new tools by saving commands in files
and how to use a more powerful version of **wildcards** to extract data from files.

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

> **Deleting Extra Files**
>
> You may have additional files
> if you worked through all of the exercises in the previous chapter.
> Feel free to delete them or move them to a separate directory.
> If you have accidentally deleted files you need,
> you can download them again by following the instructions in Section [Downloading the Data](https://se-up.github.io/RSE-UP/chapters/getting_started.html#downloading-the-data).

## Creating New Commands 

Loops let us run the same commands many times,
but we can go further and save commands in files
so that we can repeat complex operations with a few keystrokes.
For historical reasons,
a file full of shell commands is usually called a **shell script** but it is really just another kind of program.

Let's start by creating a new directory for our runnable programs called `bin/`,
consistent with the project structure described in Section [Organizing the Project Content](https://se-up.github.io/RSE-UP/chapters/getting_started.html#organizing-project-content). 

```bash
$ cd ~/zipf
$ mkdir bin
$ cd bin
```

Edit a new file called `book_summary.sh` to hold our shell script:

```bash
$ nano book_summary.sh
```

and insert this line:

```text
head -n 17 ../data/moby_dick.txt | tail -n 8
```

Note that we do *not* put the `$` prompt at the front of the line.
We have been showing that to highlight interactive commands,
but in this case we are putting the command in a file rather than running it immediately.

> **Empty Line at the End of a File?**
> 
> You'll often see scripts from many languages that end in an empty line.
> What you are seeing, though,
> is the last line of code ending in a newline character.
> This indicates to the computer that the code has ended. 
> While this newline character is not *required* for shell scripts to work,
> and sometimes isn't shown by coding tools,
> it does make it easier to view and modify scripts.
> When you are copying code from this book,
> remember to add an empty line at the end!

Once we have added this line,
we can save the file with <kbd>Ctrl</kbd>+<kbd>O</kbd>
and exit with <kbd>Ctrl</kbd>+<kbd>X</kbd>.
`ls` shows that our file now exists:

```bash
$ ls
```

```text
book_summary.sh
```

We can check the contents of the file using `cat book_summary.sh`.
More importantly,
we can now ask the shell to run this file:

```bash
$ bash book_summary.sh
```

```text
Title: Moby Dick
       or The Whale
Author: Herman Melville
Editor:
Release Date: December 25, 2008 [EBook #2701]
Posting Date:
Last Updated: December 3, 2017
Language: English
```

Sure enough,
our script's output is exactly the same text we would get if we ran the command directly.
If we want,
we can pipe the output of our shell script to another command to count how many lines it contains:

```bash
$ bash book_summary.sh | wc -l
```

```text
     8
```

What if we want our script to print the name of the book's author?
The command `grep` finds and prints lines that match a pattern.
We'll learn more about `grep` in Section [finding thins in files](https://se-up.github.io/RSE-UP/chapters/bash_advanced.html#finding-things-in-files),
but for now we can edit the script:

```bash
$ nano book_summary.sh
```

and add a search for the word "Author":

```text
head -n 17 ../data/moby_dick.txt | tail -n 8 | grep Author
```

Sure enough,
when we run our modified script:

```bash
$ bash book_summary.sh
```

we get the line we want:

```text
Author: Herman Melville
```

And once again
we can pipe the output of our script into other commands
just as we would pipe the output from any other program.
Here,
we count the number of words in the author line:

```bash
$ bash book_summary.sh | wc -w
```

```text
      3
```

## Making Scripts More Versatile 

Getting the name of the author for only one of the books isn't particularly useful.
What we really want is a way to get the name of the author from any of our files.
Let's edit `book_summary.sh` again
and replace `../data/moby_dick.txt` with
a special variable `$1`. 
Once our change is made, `book_summary.sh` should contain:

```text
head -n 17 $1 | tail -n 8 | grep Author
```

Inside a shell script,
`$1` means "the first argument on the command line."
If we now run our script like this:

```bash
$ bash book_summary.sh ../data/moby_dick.txt
```

then `$1` is assigned `../data/moby_dick.txt`
and we get exactly the same output as before.
If we give the script a different filename:

```bash
$  bash book_summary.sh ../data/frankenstein.txt
```

we get the name of the author of that book instead:

```text
Author: Mary Wollstonecraft (Godwin) Shelley
```

Our small script is now doing something useful,
but it may take the next person who reads it a moment to figureout exctly what. We can improve our script by adding a **comment**:

```text
# Get author information from a Project Gutenberg eBook.
# Usage: bash book_summary.sh /path/to/file.txt
head -n 17 $1 | tail -n 8 | grep Author
```

As in Python,
a comment starts with a `#` character and runs to the end of the line.
The computer ignores comments,
but they help people (including our future self) understand and use what we've created.

Let's make one more change to our script.
Instead of always extracting the author name,
let's have it select whatever information the user specified:

```text
# Get desired information from a Project Gutenberg eBook.
# Usage: bash book_summary.sh /path/to/file.txt what_to_look_for
head -n 17 $1 | tail -n 8 | grep $2
```

The change is very small: we have replaced the fixed string 'Author' with a reference to the special variable `$2`, which is assigned the value of the second command-line argument we give the script when we run it.

> **Update Your Comments**
>
> As you update the code in your script,
> don't forget to update the comments that describe the code.
> A description that sends readers in the wrong direction is worse than none at all,so do your best to avoid this common oversight.

Let's check that it works by asking for *Frankenstein*'s release date:

```bash
$ bash book_summary.sh ../data/frankenstein.txt Release
```

```text
Release Date: June 17, 2008 [EBook #84]
```

## Turning Interactive Work into a Script 

Suppose we have just run a series of commands that did something useful,
such as summarizing all books in a given directory:

```bash
$ for x in ../data/*.txt
> do
>   echo $x
>   bash book_summary.sh $x Author
> done > authors.txt
$ for x in ../data/*.txt
> do
>   echo $x
>   bash book_summary.sh $x Release
> done > releases.txt
$ ls
```
```text
authors.txt        book_summary.sh      releases.txt
```
```bash
$ mkdir ../results
$ mv authors.txt releases.txt ../results
```

Instead of typing those commands into a file in an editor
(and potentially getting them wrong)
we can use `history` and redirection to save recent commands to a file.
For example,we can save the last six commands to `summarize_all_books.sh`:

```bash
$ history 6 > summarize_all_books.sh
$ cat summarize_all_books.sh
```

```text
297 for x in ../data/*.txt; do echo $x;
  bash book_summary.sh $x Author; done > authors.txt
298 for x in ../data/*.txt; do echo $x;
  bash book_summary.sh $x Release; done > releases.txt
299 ls
300 mkdir ../results
301 mv authors.txt releases.txt ../results
302 history 6 > summarize_all_books.sh
```

We can now open the file in an editor, remove the serial numbers at the start of each line, and delete the lines we don't want to create a script that captures exactly what we actually did. This is how we usually develop shell scripts: run commands interactively a few times to make sure they are doing the right thing, then save our recent history to a file and turn that into a reusable script.

## Finding Things in Files

We can use `head` and `tail` to select lines from a file by position,
but we also often want to select lines that contain certain values.
This is called **filtering**, and we usually do it in the shell with the command `grep` that we briefly met in Section [creating new commands](https://se-up.github.io/RSE-UP/chapters/bash_advanced.html#creating-new-commands).
Its name is an acronym of "global regular expression print,"
which was a common sequence of operations in early Unix text editors.

To show how `grep` works,
we will use our sleuthing skills to explore `data/sherlock_holmes.txt`.
First,
let's find lines that contain the word "Sherlock".
Since there are likely to be hundreds of matches,
we will pipe `grep`'s output to `head` to show only the first few:

```bash
$ cd ~/zipf
$ grep Sherlock data/sherlock_holmes.txt | head -n 5
```

Here, `Sherlock` is our (very simple) pattern.
`grep` searches the file line by line
and shows those lines that contain matches,
so the output is:

```text
Project Gutenberg's The Adventures of Sherlock Holmes, by Arthur
Conan Doyle
Title: The Adventures of Sherlock Holmes
To Sherlock Holmes she is always THE woman. I have seldom heard
as I had pictured it from Sherlock Holmes' succinct description,
"Good-night, Mister Sherlock Holmes."
```

If we run `grep sherlock` instead, we get no output
because `grep` patterns are case-sensitive.
If we wanted to make the search case-insensitive,
we can add the option `-i`:

```bash
$ grep -i sherlock data/sherlock_holmes.txt | head -n 5
```

```text
Project Gutenberg's The Adventures of Sherlock Holmes, by Arthur
Conan Doyle
Title: The Adventures of Sherlock Holmes
*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF
SHERLOCK HOLMES ***
THE ADVENTURES OF SHERLOCK HOLMES
To Sherlock Holmes she is always THE woman. I have seldom heard
```

This output is different from our previous output
because of the lines containing "SHERLOCK" near the top of the file.

Next, let's search for the pattern `on`:

```bash
$ grep on data/sherlock_holmes.txt | head -n 5
```

```text
Project Gutenberg's The Adventures of Sherlock Holmes, by Arthur
Conan Doyle
This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away
or with this eBook or online at www.gutenberg.net
Author: Arthur Conan Doyle
```

In each of these lines,
our pattern ("on") is part of a larger word such as "Conan".
To restrict matching to lines containing `on` by itself,
we can give `grep` the `-w` option (for "match words"):

```bash
$ grep -w on data/sherlock_holmes.txt | head -n 5
```

```text
One night--it was on the twentieth of March, 1888--I was
put on seven and a half pounds since I saw you."
that I had a country walk on Thursday and came home in a dreadful
"It is simplicity itself," said he; "my eyes tell me that on the
on the right side of his top-hat to show where he has secreted
```

What if we want to search for a phrase rather than a single word?

```bash
$ grep on the data/sherlock_holmes.txt | head -n 5
```

```text
grep: the: No such file or directory
data/sherlock_holmes.txt:Project Gutenberg's The Adventures of
  Sherlock Holmes, by Arthur Conan Doyle
data/sherlock_holmes.txt:This eBook is for the use of anyone
  anywhere at no cost and with
data/sherlock_holmes.txt:almost no restrictions whatsoever.
  You may copy it, give it away or
data/sherlock_holmes.txt:with this eBook or online at
  www.gutenberg.net
data/sherlock_holmes.txt:Author: Arthur Conan Doyle
```

In this case,
`grep` uses `on` as the pattern
and tries to find it in files called `the` and `data/sherlock_holmes.txt`.
It then tells us that the file `the` cannot be found,
but prints `data/sherlock_holmes.txt` as a prefix to each other line of output
to tell us which file those lines came from.
If we want to give `grep` both words as a single argument,
we must wrap them in quotation marks as before:

```bash
$ grep "on the" data/sherlock_holmes.txt | head -n 5
```

```text
One night--it was on the twentieth of March, 1888--I was
drug-created dreams and was hot upon the scent of some new
"It is simplicity itself," said he; "my eyes tell me that on the
on the right side of his top-hat to show where he has secreted
pink-tinted note-paper which had been lying open upon the table.
```

> **Quoting**
>
> Quotation marks aren't specific to `grep`:
> the shell interprets them before running commands,
> just as it expands wildcards to create filenames
> no matter what command those filenames are being passed to.
> This allows us to do things like `head -n 5 "My Thesis.txt"`
> to get lines from a file that has a space in its name.
> It is also why many programmers write `"$variable"` instead of just `$variable`
> when creating loops or shell scripts:
> if there's any chance at all that the variable's value will contain spaces,
> it's safest to put it in quotes.

One of the most useful options for `grep` is `-n`,
which numbers the lines that match the search:

```bash
$ grep -n "on the" data/sherlock_holmes.txt | head -n 5
```

```text
105:One night--it was on the twentieth of March, 1888--I was
118:drug-created dreams and was hot upon the scent of some new
155:"It is simplicity itself," said he; "my eyes tell me ...
165:on the right side of his top-hat to show where he has ...
198:pink-tinted note-paper which had been lying open upon ...
```

`grep` has many options---so many,
in fact,
that almost every letter of the alphabet means something to it:

```bash
$ man grep
```

```text
GREP(1)           BSD General Commands Manual         GREP(1)

NAME
     grep, egrep, fgrep, zgrep, zegrep, zfgrep -- file pattern
      searcher

SYNOPSIS
     grep [-abcdDEFGHhIiJLlmnOopqRSsUVvwxZ] [-A num] [-B num]
          [-C[num]] [-e pattern] [-f file] [--binary-files=value]
          [--color[=when]] [--colour[=when]] [--context[=num]]
          [--label] [--line-buffered]
          [--null] [pattern] [file ...]
...more...
```

We can combine options to `grep` as we do with other Unix commands.
For example,
we can combine two options we've covered previously with `-v`
to invert the match---i.e.,
to print lines that *don't* match the pattern:

```bash
$ grep -i -n -v the data/sherlock_holmes.txt | head -n 5
```

```text
2:
4:almost no restrictions whatsoever. You may copy it, give ...
6:with this eBook or online at www.gutenberg.net
7:
8:
```

As we learned in Section [moving around](https://se-up.github.io/RSE-UP/chapters/bash_basics.html#moving-around),
we can write this command as `grep -inv`,
but probably shouldn't for the sake of readability.

If we want to search several files at once, all we have to do is give `grep` all of their names. The easiest way to do this is usually to use wildcards.
For example, this command counts how many lines contain "pain" in all of our books:

```bash
$ grep -w pain data/*.txt | wc -l
```

```text
     122
```

Alternatively, the `-r` option (for "recursive") tells `grep` to search all of the files in or below a directory:

```bash
$ grep -w -r pain data | wc -l
```

```text
     122
```

`grep` becomes even more powerful
when we start using **regular expressions** which are sets of letters, numbers, and symbols that define complex patterns. For example, this command finds lines that start with the letter 'T':

```bash
$ grep -E "^T" data/sherlock_holmes.txt | head -n 5
```

```text
This eBook is for the use of anyone anywhere at no cost and with
Title: The Adventures of Sherlock Holmes
THE ADVENTURES OF SHERLOCK HOLMES
To Sherlock Holmes she is always THE woman. I have seldom heard
The distinction is clear. For example, you have frequently seen
```

The `-E` option tells `grep` to interpret the pattern as a regular expression,
rather than searching for an actual circumflex followed by an upper-case 'T'.
The quotation marks prevent the shell from treating special characters in the pattern as wildcards, and the `^` means that a line only matches
if it begins with the search term---in this case, `T`.

Many tools support regular expressions:
we can use them in programming languages, database queries, online search engines, and most text editors (though not Nano---its creators wanted to keep it as small as possible).
A detailed guide of regular expressions is outside the scope of this book,
but a wide range of tutorials are available online,
and {cite:p}`Goyv2012` is a useful companion if you need to go further.

## Finding Files 

While `grep` finds things in files,
the `find` command finds files themselves.
It also has a lot of options, but unlike most Unix commands they are written as full words rather than single-letter abbreviations.
To show how it works, we will use the entire contents of our `zipf` directory,
including files we created earlier in this chapter:

```text
zipf/
├── bin
│   ├── book_summary.sh
│   ├── summarize_all_books.sh
├── data
│   ├── dracula.txt
│   ├── frankenstein.txt
│   ├── jane_eyre.txt
│   ├── moby_dick.txt
│   ├── sense_and_sensibility.txt
│   ├── sherlock_holmes.txt
│   └── time_machine.txt
└── results
    ├── authors.txt
    └── releases.txt
```

For our first command,
let's run `find .` to find and list everything in this directory.
As always,
`.` on its own means the current working directory,
which is where we want our search to start.

```bash
$ cd ~/zipf
$ find .
```

```text
.
./bin
./bin/summarize_all_books.sh
./bin/book_summary.sh
./results
./results/releases.txt
./results/authors.txt
./data
./data/moby_dick.txt
./data/sense_and_sensibility.txt
./data/sherlock_holmes.txt
./data/time_machine.txt
./data/frankenstein.txt
./data/dracula.txt
./data/jane_eyre.txt
```

If we only want to find directories,
we can tell `find` to show us things of type `d`:

```bash
$ find . -type d
```

```text
.
./bin
./results
./data
```

If we change `-type d` to `-type f`
we get a listing of all the files instead:

```bash
$ find . -type f
```

```text
./bin/summarize_all_books.sh
./bin/book_summary.sh
./results/releases.txt
./results/authors.txt
./data/moby_dick.txt
./data/sense_and_sensibility.txt
./data/sherlock_holmes.txt
./data/time_machine.txt
./data/frankenstein.txt
./data/dracula.txt
./data/jane_eyre.txt
```

Now let's try matching by name:

```bash
$ find . -name "*.txt"
```

```text
./results/releases.txt
./results/authors.txt
./data/moby_dick.txt
./data/sense_and_sensibility.txt
./data/sherlock_holmes.txt
./data/time_machine.txt
./data/frankenstein.txt
./data/dracula.txt
./data/jane_eyre.txt
```

Notice the quotes around `"*.txt"`.
If we omit them and type:

```bash
$ find . -name *.txt
```

then the shell tries to expand the `*` wildcard in `*.txt`
*before* running `find`.
Since there aren't any text files in the current directory,
the expanded list is empty,
so the shell tries to run the equivalent of

```bash
$ find . -name
```

and gives us the error message:

```text
find: -name: requires additional arguments
```

We have seen before how to combine commands using pipes.
Let's use another technique to see how large our books are:

```bash
$ wc -l $(find . -name "*.txt")
```

```text
14 ./results/releases.txt
14 ./results/authors.txt
22331 ./data/moby_dick.txt
13028 ./data/sense_and_sensibility.txt
13053 ./data/sherlock_holmes.txt
3582 ./data/time_machine.txt
7832 ./data/frankenstein.txt
15975 ./data/dracula.txt
21054 ./data/jane_eyre.txt
96883 total
```

When the shell executes our command,
it runs whatever is inside `$(...)` and then replaces `$(...)` with that command's output. Since the output of `find` is the paths to our text files,
the shell constructs the command:

```bash
$ wc -l ./results/releases.txt ... ./data/jane_eyre.txt
```

(We are using `...` in place of seven files' names in order to fit things neatly on the printed page.)
This results in the output as seen above.
It is exactly like expanding the wildcard in `*.txt`,
but more flexible.

We will often use `find` and `grep` together.
The first command finds files whose names match a pattern,
while the second looks for lines inside those files that match another pattern.
For example,
we can look for `Authors` in all our text files:

```bash
$ grep "Author:" $(find . -name "*.txt")
```

```text
./results/authors.txt:Author: Bram Stoker
./results/authors.txt:Author: Mary Wollstonecraft (Godwin)
Shelley
./results/authors.txt:Author: Charlotte Bronte
./results/authors.txt:Author: Herman Melville
./results/authors.txt:Author: Jane Austen
./results/authors.txt:Author: Arthur Conan Doyle
./results/authors.txt:Author: H. G. Wells
./data/moby_dick.txt:Author: Herman Melville
./data/sense_and_sensibility.txt:Author: Jane Austen
./data/sherlock_holmes.txt:Author: Arthur Conan Doyle
./data/time_machine.txt:Author: H. G. Wells
./data/frankenstein.txt:Author: Mary Wollstonecraft (Godwin)
Shelley
./data/dracula.txt:Author: Bram Stoker
./data/jane_eyre.txt:Author: Charlotte Bronte
```

We can also use `$(...)` expansion to create a list of filenames to use in a loop:

```bash
$ for file in $(find . -name "*.txt")
> do
> cp $file $file.bak
> done
$ find . -name "*.bak"
```

```text
./results/releases.txt.bak
./results/authors.txt.bak
./data/frankenstein.txt.bak
./data/sense_and_sensibility.txt.bak
./data/dracula.txt.bak
./data/time_machine.txt.bak
./data/moby_dick.txt.bak
./data/jane_eyre.txt.bak
./data/sherlock_holmes.txt.bak
```

## Configuring the Shell

As Section [repeating commands on many files](https://se-up.github.io/RSE-UP/chapters/bash_tools.html#repeating-commands-on-many-files) explained,
the shell is a program, and it has variables like any other program.
Some of those variables control the shell's operations;
by changing their values we can change how the shell and other programs behave.

Let's run the command `set`and look at some of the variables the shell defines:

**DEPENDING ON THE SYSTEM YOU RUN OR WHETHER OR NOT YOU USE ANACONDA THE FOLLOWING WILL LOOK DIFFERENT**
**EXAMPLES BASED ON WINDOWS AND USING ANACONDA**

```bash
$ set
```

```text
COMPUTERNAME=TURING
HOME=/Users/amira
HOMEDRIVE=C:
HOSTNAME=TURING
HOSTTYPE=i686
NUMBER_OF_PROCESSORS=4
OS=Windows_NT
PATH=/Users/amira/anaconda3/bin:/usr/bin:
  /bin:/usr/sbin:/sbin:/usr/local/bin
PWD=/Users/amira
UID=1000
USERNAME=amira
...
```

There are many more than are shown here---roughly a hundred
in our current shell session.
And yes,
using `set` to *show* things might seem a little strange,
even for Unix,
but if we don't give it any arguments,
the command might as well show us things we *could* set.

By convention,
**shell variables** that are always present have upper-case names.
All shell variables' values are strings,
even those (such as `UID`) that look like numbers.
It's up to programs to convert these strings to other types when necessary.
For example,
if a program wanted to find out how many processors the computer had,
it would convert the value of `NUMBER_OF_PROCESSORS` from a string to an integer.

Similarly, some variables (like `PATH`) store lists of values. In this case, the convention is to use a colon ':' as a separator.
If a program wants the individual elements of such a list, it must split the variable's value into pieces.

Let's have a closer look at `PATH`.
Its value defines the shell's **search path**,
which is the list of directories that the shell looks in for programs
when we type in a command name without specifying exactly where it is.
For example,
when we type a command like `analyze`,
the shell needs to decide whether to run `./analyze` (in our current directory)
or `/bin/analyze` (in a system directory).
To do this,
the shell checks each directory in the `PATH` variable in turn.
As soon as it finds a program with the right name,
it stops searching and runs what it has found.

To show how this works,
here are the components of `PATH` listed one per line:

```bash
/Users/amira/anaconda3/bin
/usr/bin
/bin
/usr/sbin
/sbin
/usr/local/bin
```

Suppose that our computer has three programs called `analyze`:
`/bin/analyze`,
`/usr/local/bin/analyze`,
and `/Users/amira/analyze`.
Since the shell searches the directories in the order in which they're listed in `PATH`,
it finds `/bin/analyze` first and runs that.
Since `/Users/amira` is not in our path,
Bash will *never* find the program `/Users/amira/analyze`
unless we type the path in explicitly
(for example,
as `./analyze` if we are in `/Users/amira`).

If we want to see a variable's value, we can print it using the `echo` command
introduced at the end of Section [redoing things](https://se-up.github.io/RSE-UP/chapters/bash_tools.html#redoing-things).
Let's look at the value of the variable `HOME`, which keeps track of our home directory:

```bash
$ echo HOME
```

```text
HOME
```

Whoops: this just prints "HOME", which isn't what we wanted.
Instead,
we need to run this:

```bash
$ echo $HOME
```

```text
/Users/amira
```


As with loop variables (Section [redoing thins](https://se-up.github.io/RSE-UP/chapters/bash_tools.html#redoing-things),
the dollar sign before the variable names tells the shell
that we want the variable's value.
This works just like wildcard expansion---the shell replaces
the variable's name with its value *before* running the command we've asked for.
Thus,
`echo $HOME` becomes `echo /Users/amira`,
which displays the right thing.

Creating a variable is easy: we assign a value to a name using "=",
putting quotes around the value if it contains spaces or special characters:

```bash
$ DEPARTMENT="Library Science"
$ echo $DEPARTMENT
```

```text
Library Science
```

To change the value, we simply assign a new one:

```bash
$ DEPARTMENT="Information Science"
$ echo $DEPARTMENT
```

```text
Information Science
```

If we want to set some variables automatically every time we run a shell,
we can put commands to do this in a file called `.bashrc` in our home directory.
For example, here are two lines in `/Users/amira/.bashrc`:

```text
export DEPARTMENT="Library Science"
export TEMP_DIR=/tmp
export BACKUP_DIR=$TEMP_DIR/backup
```

These three lines create the variables `DEPARTMENT`,
`TEMP_DIR`, and `BACKUP_DIR`, and **export** them so that any programs the shell runs can see them as well.
Notice that `BACKUP_DIR`'s definition relies on the value of `TEMP_DIR`,
so that if we change where we put temporary files, our backups will be relocated automatically.

However, this will only happen once we restart the shell,
because `.bashrc` is only executed when the shell starts up.

> **What's in a Name?**
>
> The '.' character at the front of the name `.bashrc`
> prevents `ls` from listing this file
> unless we specifically ask it to using `-a`.
> The "rc" at the end is an abbreviation for "run commands",
> which meant something really important decades ago,
> and is now just a convention everyone follows without understanding why.

While we're here,
it's also common to use the `alias` command to create shortcuts for things we frequently type. For example, we can define the alias `backup`
to run `/bin/zback` with a specific set of arguments:

```bash
alias backup=/bin/zback -v --nostir -R 20000 $HOME $BACKUP_DIR
```

Aliases can save us a lot of typing, and hence a lot of typing mistakes.
The name of an alias can be the same as an existing command,
so we can use them to change the behavior of a familiar command:

```bash
# Long list format including hidden files
alias ls='ls -la'

# Print the file paths that were copied/moved
alias mv='mv -v'
alias cp='cp -v'

# Request confirmation to remove a file and
# print the file path that is removed
alias rm='rm -iv'
```

We can find interesting suggestions for other aliases
by searching online for "sample bashrc".

While searching for additional aliases, you're likely to encounter references to other common shell features to customize, such as the color of your shell's background and text.

As mentioned in Chapter [bash basics](https://se-up.github.io/RSE-UP/chapters/bash_basics.html), another important feature to consider customizing is your shell prompt.
In addition to a standard symbol (like `$`), your computer may include other information as well, such as the working directory, username, and/or date/time.
If your shell does not include that information and you would like to see it,
or if your current prompt is too long and you'd like to shorten it,
you can include a line in your `.bashrc` file that defines `$PS1`:

```bash
PS1="\u \w $ "
```

This changes the prompt to include your username and current working directory:

```bash
amira ~/Desktop $
```

## Summary 

As powerful as the Unix shell is, it does have its shortcomings: dollar signs, quotes, and other punctuation can make a complex shell script look as though
it was created by a cat dancing on a keyboard.
However, it is the glue that holds data science together:
shell scripts are used to create pipelines from miscellaneous sets of programs,
while shell variables are used to do everything from
specifying package installation directories to managing database login credentials.
And while `grep` and `find` may take some getting used to,
they and their cousins can handle enormous datasets very efficiently.
If you would like to go further,
{cite:p}`Ray2014` is an excellent general introduction,
while {cite:p}`Jans2014` looks specifically at how to process data on the command line.


## Key Points 

```{include } keypoints/bash_advanced.md

```

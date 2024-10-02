# Course concept

The end goal is to *understand* how to use git & Github.
This means building our castle of Github-knowledge, but we don't want to build it in the air.
Rather we build up the foundations layer by layer:

- Terminal and shells: what are they and how can we use them
- Crypto in computers: hashes, SSL, public-private keys, PKI
- Version Control Systems: from cvs to git (focus on git)
- Github, Github flow, other Github tools

---

# Questions

The idea is to build from the ground up.
This means that questions like "why it it like this", or "what is that based on" are very much allowed and encouraged.

I don't know what you don't know, so please stop me if I assume that something is known!

---

# Layers

![Layers](1/shrek.webp)
---

# Computers are complex

- No single computer / program does everything
- Each program (and even each piece of hardware) is just a layer, talking to the layers above and below it, through an API.
- This means (in an ideal world) that each layer can be swapped out, as long as it has the same API.
- E.g. when you write R code, it will run on Standard R, FastR, Microsoft Open R, Rcpp.
- Likewise, Standard R will run on Linux, on MacOS, on Windows
- Windows runs on Dell, Lenovo, etc.

---

# CLI, Terminal, Shell

- Command-line-interface, terminal and shell are being used interchangeably.
- In reality:
    - Terminal is top layer that displays characters on screen (API1) and gets input from keyboard (API2). Terminal is also called "console"
    - Shell is a lower layer. Simple version: start other programs. More complex: full programming language. Example: `bash`
    - Command line interface (CLI): the API that a certain program (e.g. `git`) exposes to the shell (command line) that controls what the program does.

---

# Command line ecosystem

- Unix-like systems (incl MacOS and `git-bash`) provide hundreds of small command line programs.
- Each program can be thought of as a built-in function in R.
- Additional programs can be installed (like additional packages)
- Quite often, one CLI program will call another program.
- Like with layers, this also often means they can be swapped out.

---

# Command line interface

Simply speaking, each CLI program gets a list of parameters (command line parameters).
These are like function parameters.
Some change on which file(s) the program works (e.g. `ls file1.txt file2.txt`), some change the output (`ls -l`), some tell the command what to do (`git commit`)

Parameters are separated by space. If you want a parameter with a space inside the parameter (e.g. a filename with a space), you put it between quotes, or use backslash:
```shell
ls "this file has a long name.txt"
ls 'this file has a long name.txt'
ls this\ file\ has\ a\ long\ name.txt
```

vvvvvv

# Parameters and flags

In *most* unix command-line tools the following conventions are used (however there are exceptions):

- *Flags* switch on certain functionality (e.g. `ls -l`).
    - Single letter flags are preceded by a single dash (e.g. `ls -l`)
    - Long-form flags have double dash (e.g. `grep --help`)
    - Often flags can be both long and short form: (e.g. `grep --help` == `grep -h`)
    - Multiple single-letter flags can be used together (e.g. `ls -l -a` == `ls -la`)
    - NOTE: `ls -la` is `ls` with two flags. `ls --la` is `ls` with a single long flag.
- *Named parameters* are a flag followed by a value:
    - `git --worktree=/Users/reinoud/test` == `git --worktree /Users/reinoud/test`
    - Each program defines which double-dash things are flags, which are named params
- Anything else is a non-named parameter

vvvvvv

# Slashes

In the whole world backslash (`\`) is an escape character, and forward slash (`/`) is a directory separator:

```shell
ls long\ dir\ name/long\ file\ name.txt
https://n2g.claude-apps.com/index.html`
```

```R
double_quote <- "\"This is a quote\""
single_quote <- 'It\'s a sunny day'
path <- "C:\\Users\\YourName\\Documents"
```

However historically in Microsoft shells (DOS (`cmd.exe`), PowerShell, *not* `git-bash`):

- backslash is path separator
- forward slash is to indicate flags
- Caret (`^`) *sometimes* escapes spaces (\*sigh\*)

```
C:\Documents
dir /x
```

vvvvvv


# Examples


```asciiart
mkdir -v -m 0777 project1 project2
||||| || || |||| |||||||| ^^^^^^^-- positional argument 2
||||| || || |||| ^^^^^^^-- positional argument 1
||||| || ^^ ^^^^----- flag with argument
||||| ^^-- flag without argument (verbose)
^^^^^--- program name
```

```asciiart
mkdir -v -m 0777 "project1 project2"
||||| || || ||||  ^^^^^^^^^^^^^^^^^-- positional argument 1
||||| || ^^ ^^^^----- flag with argument
||||| ^^-- flag without argument (verbose)
^^^^^--- program name
```

```shell
git log --follow --date=iso8601-strict --pretty=format:'%H %ad %d' main lessons/index.html
```

---

# A step back

## `git`

`git` is a command-line *program* that runs on your computer, allowing to do version control.
It can send your changes to other computers and retrieve them from other computers (`push` and `pull`), but can certainly work 100% locally as well. `git` is free and open source.

Site: https://git-scm.com/ (git source code management)

vvvvvv

## Github

Github is a website (launched 2008, owned by Microsoft since 2018). It allows `git` to `push` and `pull` to a central location. In addition, it offers other tools for cooperation (bug tracking, project planning, etc). Basic use of Github is free, however there is controversy that code on Github is being used to train AI.

There are alternatives to Github, GitLab and BitBucket being the most used.

Site: https://github.com/

vvvvvv

## `git` ≠ Github
---

# Why command-line

`git` started as a terminal program.

These days there are lots of GUI alternatives, but to really understand how `git` works, you need to understand it's command line interface.

Also, the command line is the most wide-spread version of `git` and has the most descriptions on how to do things online.


---

# Install term/shell/git

## MacOS
- (optionally) install iTerm2 (from https://iterm2.com/); alternatively use built-in `Terminal.app`
- Install HomeBrew (go to https://brew.sh/ and copy-paste that line into the terminal. **NB: normally never do this**
- Install a new `git` version: `brew install git`
- Check `git` version: `git --version`


## Windows
- Install Terminal + Shell (`bash`) + `git`: https://gitforwindows.org/

---

# Why use Terminal / Shell

- Repeatable / easy to describe
- Expressive
- Programmable
- Keyboard only
- Steep learning curve

*Personally, I do most of my things in terminal (including coding / making this presentation / etc) but this is excessive*

Not well suited for graphical applications (photo/video editing / web browsing (usually) / etc)

---

# With great power ...

⚠️You can break things very much⚠️

- There are not (always) "are you sure" questions
- When you delete a file, it's gone (no "get back from trash can")
- A single typo can make your command mean something very different!!!
- Many OS level protections are not present (there are some protections)

`rm -r mydir/` vs `rm -r mydir /`

⚠️Generally be weary when copy-pasting things into your terminal⚠️
(or typing things other people tell you to type)

On the other hand, if you're careful, things will be ok

---

# What is the shell

- Programming environment
- type a line and execute it
- each (correct) line (command) either runs a program from start to end, starts a program (after which you can interact with the program).
- After a program has run, you can type the next line and execute it.

Works in the same environment as GUI (files and directories)

**shell is always "in" some directory (called working directory).
Commands are usually relative to working directory,
so it's important to know where you are**

---

# Interaction with shell commands (programs)

Most (basic) commands are supposed to run non-interactive
*(this is because that way they could be used in scripts)*

```asciiart
           command line parameters
                      |
                      |
                      V
                  *-------*
     (stdin --->) |PROGRAM|----> stdout
                  |       |----> stderr
                  *-------*
                      |
                      |
                      V
                return code
```

---

# Hands on: let's start

1. Open your terminal. Terminal will start default shell.
1. You should see your prompt. A "prompt" gives some status info, and lets you know you can type your next line.
1. Try some things. Suggestions: `pwd`, `ls -la`, `cd ..`, `cd #dirname#`.

A unix shell is a fully fledged programming language, and we could fill a 10 week course with just the shell basics. Instead, we will introduce new concepts as we get to them.


---

# Cheat sheet 1: commands

- `pwd`: print working directory
- `ls`: list directory
- `cd`: change directory (e.g. `cd project`)
- `mkdir`: make directory (e.g. `mkdir project` or `mkdir -p project/A`
- `rmdir`: remove **empty** directory (e.g. `rmdir project`)

vvvvvv

- `touch`: creates an empty file (e.g. `touch README.md`)
- `cat`: print out a file (e.g. `cat README.md`)
- `cp`: copy a file (e.g. `cp README.md README2.md` or `cp README.md project`)
- `mv`: move (rename) a file (e.g. `mv README.md README2.md` or `mv README.md project`)
- `rm`: remove (delete) a file (e.g. `rm README.md`)
- `nano`: simple text editor (may or may not be installed)

vvvvvv

- `history`: shows previous commands
- `exit`: quit *this shell*
- `echo`: print (e.g. `echo "hello gdansk"`)

---

# Cheat sheet 1 extras (advanced)

### Redirects

- `>`: redirect stdout to file (overwrite; e.g. `echo hello > test.txt`)
- `>>`: append stdout to file (e.g. `echo hello again >> test.txt`)
- `|`: send stdout as stdin of next command

vvvvvv

### Separators between commands on same line

- `;`: end of command
- `&&`: "and"; next command only runs if previous succeeded
- `||`: "or"; next command only runs if previous failed

vvvvvv

### Subshell

- `$(cmd)` execute `cmd` and put the output in place of this. e.g `echo "I'm in $(pwd)"`

---

# Cheat sheet 2: files and directory names

- `~`: home directory
- `/`: directory separator; if at start: absolute directory. if by itself: root
- `/root`: home directory for root user (note: NOT root directory)
- `/home/NAME/` or `~NAME/`: home directory for NAME user
- `.`: current (or same) directory
- `..`: one directory up
- `/tmp`: place for temporary files (e.g. removed after restart)
- `.xxxx`: hidden file / directory (starts with `.`)

vvvvvv

### wildcards:
- `*`: 0 or more characters
- `?`: 1 character
- `[abc]`, [a-z]: any of the characters in `a`, `b` and `c` or between `a` and `z`
- `{mp4,MTS}`: either `mp4` or `MTS`

---

# Cheat sheets notes

- Note: in \*nix stuff *generally* is case-sensitive
- general idea `filename.ext`; extension no special meaning in linux

- `-h` / `--help`: (usually) shows some help about a command. (e.g. `mkdir -h`)
- `man`: shows manual page (if available; e.g. `man mkdir`)

- `<TAB>` is your friend

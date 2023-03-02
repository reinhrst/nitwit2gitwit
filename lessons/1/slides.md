---
marp: true
paginate: true
---

# Course concept

The end goal is to *understand* how to use github.
This means buiding our castle of github-knowledge, but we don't want to build it in the air.
Rather we build up the foundations layer by layer:

- Terminal and shells: what are they and how can we use them
- Crypto in computers: hashes, SSL, public-private keys, PKI
- Version Control Systems: from csv to git (focus on git)
- Github, github flow, other github tools

----

# Questions

The idea is to build from the ground up.
This means that questions like "why it it like this", or "what is that based on" are very much allowed and encouraged.

<!-- Also: please interrupt me if something is not clear, or rather already clear. guide me
I don't know what you know, and many of these things are second nature to me by now
I have no clear plan how fast we should go, so we'll go as fast as we go
-->

----

# WHY?

`git` started as a terminal program.

These days there are lots of GUI alternatives, but to really understand how `git` works, you need to understand it's command line interface

----

# Shell

- Shell is a *shell* around a bunch of functionality; specifically core computer functionality.
  - DOS prompt (`cmd.exe`)
  - PowerShell
  - \*nix shell (bash / zsh / csh)
  - Note: *Secure shell (`ssh`)* is not actually a shell :)

*In this course we will use \*nix shell*

----

# Terminal

- A *terminal* (endpoint) is the thing that shows the interface
  - Early version would communicate with computer
  - These days usually a program (macOS Terminal, iTerm2, linux xTerm, windows PowerShell?)
  - Usually text-only, although there are some exceptions
  - Mouse-support more and more present, but try to avoid it (select-copy and scroll)
  - Terminal can run shell (or any other commandline program; but usually shell, or shell-manager)

Shell/terminal is also being called *console* or *cli (command line interface)*

<!-- although the term "console" is also used to describe many other things -->

----

# Why use Terminal / Shell

- Repeatable / easy to describe
- Expressive
- Programmable
- Keyboard only
- Steep learning curve

*Personally, I do most of my things in terminal (including coding / making this presentation / etc) but this is excessive*

Not well suited for graphical applications (photo/video editing / web browsing (usually) / etc)

----

# With great power comes great responsibility

⚠️You can break things very much⚠️

- There are not (always) "are you sure" questions
- When you delete a file, it's gone (no "get back from trash can")
- A single typo can make your command mean something very different!!!
- Many OS level protections are not present (there are some protections)

`rm -r mydir/` vs `rm -r mydir /`

⚠️Generally be weary when copy-pasting things into your terminal⚠️
(or typing things other people tell you to type)

On the other hand, if you're careful, things will be ok

----

# What is the shell

- Programming environment
- type a line and execute it
- interact with local data (variables) and global data (files)
- functions are other programs(\*)

Works in the same environment as GUI (files and directories)

**shell is always "in" some directory (called working directory).
Commands are usually relative to working directory,
so it's important to know where you are**
<!-- quickly explain *nix directory structure -->

----

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
                  |       |----> stdout
                  *-------*
                      |
                      |
                      V
                return code
```

----

# Interaction with shell commands (cont.)

Programs are called with command line parameters:
e.g.

```asciiart
mkdir -v -m 0777 project
||||| || || |||| ^^^^^^^-- positional argument
||||| || ^^ ^^^^----- flag with argument
||||| ^^-- flag without argument (verbose)
^^^^^--- program name
```

*Usually* command arguments work like this:

- Positional arguments (without `-`)
- Flags without argument (e.g. `-v`; flags *can* often be combined; i.e. `-v -p` = `-vp`)
- Flags with argument (can only be combined if last: `-v -m 0777` = `-vm 0777`)
- *Usually* flags have short and long format (`-v` and `--verbose`)

counter example `find . -s -iname test.mp4 -size +2GB`

----

# Hands on: let's start

*for now we will open a shell in the browser*

1. Open [link][1] (or see below for url) and wait for `[root@localhost ~]#`
1. Make a user account and log in: `useradd testuser && su -l testuser`
Note `-l` is a dash `-` followed by a lowercase `L`.
It should now say `[testuser@localhost ~]$`

Let's understand the prompt

1. See how the prompt is defined: `echo $PS1`
1. Update the prompt: `PS1="\w \$ "`
1. Find out what directory we're in: `pwd`

<!-- make sure you open dir with ctrl-click in new window --->

[https://bellard.org/jslinux/vm.html?cpu=riscv64&url=fedora33-riscv.cfg&mem=256][1]

[1]: https://bellard.org/jslinux/vm.html?cpu=riscv64&url=fedora33-riscv.cfg&mem=256

<!-- Shell in the browser:
- Everyone has the same
- No local file access
- No risk
- Easy to start again cleanly
--->
----

# Cheat sheet 1: commands

`pwd`: print working directory
`ls`: list directory
`cd`: change directory (e.g. `cd project`)
`mkdir`: make directory (e.g. `mkdir project` or `mkdir -p project/A`
`rmdir`: remove **empty** directory (e.g. `rmdir project`)

`touch`: creates an empty file (e.g. `touch README.md`)
`cat`: print out a file (e.g. `cat README.md`)
`cp`: copy a file (e.g. `cp README.md README2.md` or `cp README.md project`)
`mv`: move (rename) a file (e.g. `mv README.md README2.md` or `mv README.md project`)
`rm`: remove (delete) a file (e.g. `rm README.md`)
`nano`: simple text editor

`history`: shows previous commands
`exit`: quit *this shell*
`echo`: print (e.g. `echo "hello gdansk"`)

<!-- Note: mv and cp either take a directory or filename as second argument, and behave differently -->
----

# Cheat sheet 1 extras

### Redirects

`>`: redirect stdout to file (overwrite; e.g. `echo hello > test.txt`)
`>>`: append stdout to file (e.g. `echo hello again >> test.txt`)
`|`: send stdout as stdin of next file

### Separators between commands on same line

`;`: end of command
`&&`: "and"; next command only runs if previous succeeded
`||`: "or"; next command only runs if previous failed

### Subshell

`$(cmd)` execute `cmd` and put the output in place of this. e.g `echo "I'm in $(pwd)"`

----

# Cheat sheet 2: files and directory names

`~`: home directory
`/`: directory separator; if at start: absolute directory. if by itself: root
`/root`: home directory for root user (note: NOT root directory)
`/home/NAME/` or `~NAME/`: home directory for NAME user
`.`: current (or same) directory
`..`: one directory up
`/tmp`: place for temporary files (e.g. removed after restart)
`.xxxx`: hidden file / directory (starts with `.`)
`-`: stdin / stdout (sometimes)

wildcards:
`*`: 0 or more characters
`?`: 1 character
`[abc]`, [a-z]: any of the characters in `a`, `b` and `c` or between `a` and `z`
`{mp4,MTS}`: either `mp4` or `MTS`

----

# Cheat sheets notes

- Note: in \*nix stuff *generally* is case-sensitive
- general idea `filename.ext`; extension no special meaning in linux
- **directorynames / filenames with spaces / special chars need escaping**
  (put them between `""` or `''`)

- `-h`: (usually) shows some help about a command. (e.g. `mkdir -h`)
- `man`: shows manual page (if available; e.g. `man mkdir`)

- `<TAB>` is your friend

----

# Play time

Let's make sure we're in our home directory
Now make a directory "project"
Go to directory "project"
Make a directory "A"
Make a file "test.txt" in this new directory with content "hello everyone"
Print the contents of this file to the console

Make a directory B next to directory A
In this directory make a file "manyhellos.txt", containing 10 lines with the word "hello"
Now print in 1 command the contents of both `~/project/A/test.txt` and `~/project/B/manyhellos.txt`

----

# Play time 2

Copy `test.txt` to the `B` directory
Rename the `test.txt` file to `onehello.txt`
Delete `onehello.txt`
Now, in one command, copy `test.txt` to the `B` directory with name `onehello.txt`
List all files in the `B` directory
Print the content of both files

Try to remove the `A` directory
Remove the files in the `A` directory and remove it

Print the working directory and store it in `~/projects/mydir.txt`
Print the working directory twice and store it in `~/projects/mydirs.txt`

----

# Homework

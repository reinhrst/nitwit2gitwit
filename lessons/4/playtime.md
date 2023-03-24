## Playtime

- Each page has one assignment.
- There are (hidden) hints and solutions on the page, that you can unhide with the button
- The solutions work as follows:
  - lines starting with `$` are commands to type
  - Anything after `#` is a comment (so no need to type it in)
  - lines starting with something else are expected results
  - things like usernames may be different in your results
- The solutions may contain more `ls` and `pwd` and `git status` and `md5sum` commands than necessary, however this so that the student can check they have the same thing
- Sometimes there is a vertical slide with extra deep-dive info

vvvvvvvv

Congratulations, you found the vertical slide. Some exercises will have these vertical slides, and you can find more info, or deep-dive info in there.

There may be solutions or hints to the exercise in the vertical scroll, so only go there after you have solved the exercise.

---

Create a new directory in your home directory named `minions` and move to this new directory

```bash
$ cd ~  # make sure we're in the home directory
$ # if there already is a directory "minions" (i.e. you want to start again), remove it: `rm -r minions`
$ mkdir minions
$ cd minions
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Start a new git respository in this directory

```bash
$ pwd
/home/claude/minions
$ ls -la # see vertical slide for more info on the `-la` part
total 12
drwxr-xr-x 2 claude claude 4096 Mar 24 10:56 .
drwxr-x--- 1 claude claude 4096 Mar 24 10:56 ..
$ git init # starts new, empty, respository in current directory
Initialized empty Git repository in /home/claude/minions/.git/
$ git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
$ ls -la
total 16
drwxr-xr-x 3 claude claude 4096 Mar 24 11:01 .
drwxr-x--- 1 claude claude 4096 Mar 24 11:01 ..
drwxr-xr-x 7 claude claude 4096 Mar 24 11:04 .git
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

- `ls -la` is a short form for `ls -l -a` (in lesson 2 we saw that often two short flas (`-l` and `-a`) can be pulled together into `-la`).

- `-a` means that we want to see *a*ll files, including hidden files (the ones starting with `.` -- see one more vertical slide for more info).

- `-l` (lower-case L) means *l*ong format. It lists one file per line, and adds some info:

- The exact format differs per system, but usually contains the same information

vvvvvvvv

```
total 12
drwxr-xr-x 2 claude claude 4096 Mar 24 10:56 .
drwxr-x--- 1 claude claude 4096 Mar 24 10:56 ..
```

- As you may remember, `.` is the current dir and `..` the parent dir. These are always present (so this, in effect, is an empty directory).
- The first line says that 12 blocks (of disk space) are used for the directory information (not to store the _files_ in the directory, just the list of links to the files).
- each file/directory is one line
- the start `drwxr-xr-x` explains that it is a directory (`d`), and next who has rights to read/write/access it (you can ignore this for now)
- `claude claude` describes the owner (and group) of the file
- `4096` is the disk size of this file or directory
- `Mar 24 10:56` is the modified time (last time something changed). It depends on the system which timezone this is in (in our case: UTC)
- The `1` and `2` are number of links, please ignore :)

vvvvvvvv

#### hidden files

- In Windows, each file has a small flag (piece of metadata) that descibes if a file is hidden or not. You can have a file `bananas.txt` and make it a hidden file (and it won't show in your explorer, unless you switch it to show hidden files).
- In \*nix systems (incl Linux and MacOS) this works differently. A hidden file is any file with a name starting with with a `.` (dot).
- This includes `.` and `..`, the current and parent directory (which is why you normally don't see them if you do `ls` without `-a`).
- This also explains why if you use a USB stick from Mac on Windows, you will see files like `.DS_Store`, which you don't see on mac. These are hidden files on mac, but not on windows.
- The directory `.git` is therefore also a hidden directory. Even though it's a good idea to ignore `.git` directory, there are many hidden files that are useful to be aware of.

---

Remove repository in `minions` directory

Literally the only thing that makes the directory a git repository, is the presence of the .git directory

<!-- .element class="hidden-answer" -->

<button>show hint</button>

```bash
$ pwd
/home/claude/minions
$ ls -la
total 16
drwxr-xr-x 3 claude claude 4096 Mar 24 11:01 .
drwxr-x--- 1 claude claude 4096 Mar 24 11:01 ..
drwxr-xr-x 7 claude claude 4096 Mar 24 11:04 .git
$ rm -r .git # -r means "recursive", it will delete a whole directory
$ ls -la
total 12
drwxr-xr-x 2 claude claude 4096 Mar 24 11:06 .
drwxr-x--- 1 claude claude 4096 Mar 24 11:01 ..
# as you can see, no more .git directory
$ git status
fatal: not a git repository (or any of the parent directories): .git
# also git knows it's not a git repository anymore
#(it looks in the current director, and ALL parents (until it gets to /)
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

Deleting the repo means you lose all info (commits, log messages, history) in the repo (unless it's e.g. in github)

In "normal life" there is little reason to ever delete the repo; this exercise is mostly to show that the repository is no magic, just a directory and nothing more.

---

Recreate git repository and check the log (note, checking the log may fail at this time)

```bash
$ pwd
/home/claude/minions
$ ls -la
total 12
drwxr-xr-x 2 claude claude 4096 Mar 24 11:06 .
drwxr-x--- 1 claude claude 4096 Mar 24 11:01 ..
$ git init
Initialized empty Git repository in /home/claude/minions/.git/
$ git init
Reinitialized existing Git repository in /home/claude/minions/.git/
# So if you type git init in an already existing repo, it does nothing much
$ git log
fatal: your current branch 'main' does not have any commits yet
# makes sense, the branch is empty, there is nothing to show
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Create a simple file `bananas.txt`, write some text (minimal 5 lines) and save the file

```bash
$ pwd
/home/claude/minions
$ ls -la
total 16
drwxr-xr-x 3 claude claude 4096 Mar 24 11:17 .
drwxr-x--- 1 claude claude 4096 Mar 24 11:01 ..
drwxr-xr-x 7 claude claude 4096 Mar 24 11:17 .git
$ nano bananas.txt  # save with CTRL-O and exit with CTRL-X when done
# see slide "below" to see alternative way to create the file
$ ls -la
total 20
drwxr-xr-x 3 claude claude 4096 Mar 24 11:24 .
drwxr-x--- 1 claude claude 4096 Mar 24 11:22 ..
drwxr-xr-x 7 claude claude 4096 Mar 24 11:17 .git
-rw-r--r-- 1 claude claude  145 Mar 24 11:23 bananas.txt
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

```bash
# alternative way to create the file
$ echo "Ba Ba Ba, Ba Ba Na Na
Ba Ba Ba, Ba Ba Na Na
Bananahahaaa
Potatoo nahahaaa

Tokadido Pokatoli
Kalimanomani
Tanotika
Ba Ba Ba, Ba Ba Na Na" > bananas.txt
```

Because we used a quote ("), we can use multiple lines in our echo statement (the statement won't end until the quote is closed).
Watch out in this method, that if the thing you paste contains quotes by itself, it will be interpreted as endquote and it won't always work.

E.g (don't run this, it will give errors)

```bash
$ echo "Tomorrow's weather in Bergen will be "rainy,
windy
and a chance of snow"" > weather_report.txt
```

---

Run git status. What does it tell you?

```bash
$ pwd
/home/claude/minions
$ ls -la
total 20
drwxr-xr-x 3 claude claude 4096 Mar 24 11:24 .
drwxr-x--- 1 claude claude 4096 Mar 24 11:22 ..
drwxr-xr-x 7 claude claude 4096 Mar 24 11:17 .git
-rw-r--r-- 1 claude claude  145 Mar 24 11:23 bananas.txt
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        bananas.txt

nothing added to commit but untracked files present (use "git add" to track)
# It says that there is one untracked files. Untracked means "it is present in your working directory, but not in (the currently checked out) git revision.
# Think of "track changed" in Word; untracked means that changes are not being tracked (and remember, everything, including creation of a file, is a change).
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Move the file (or technically the changes) into the index

The `add` subcommand takes a filename as parameter

<!-- .element class="hidden-answer" -->

<button>show hint</button>

```bash
$ pwd
/home/claude/minions
$ ls -la
total 20
drwxr-xr-x 3 claude claude 4096 Mar 24 11:24 .
drwxr-x--- 1 claude claude 4096 Mar 24 11:22 ..
drwxr-xr-x 7 claude claude 4096 Mar 24 11:17 .git
-rw-r--r-- 1 claude claude  145 Mar 24 11:23 bananas.txt
$ git add bananas.txt
# That's it :)) -- next exercise we confirm whether it worked
# alternatively you can do `git add *` to add all (non-hidden) files
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Run git status again. What does it tell you now?

```bash
$ pwd
/home/claude/minions
$ ls -la
total 20
drwxr-xr-x 3 claude claude 4096 Mar 24 11:24 .
drwxr-x--- 1 claude claude 4096 Mar 24 11:22 ..
drwxr-xr-x 7 claude claude 4096 Mar 24 11:17 .git
-rw-r--r-- 1 claude claude  145 Mar 24 11:23 bananas.txt
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   bananas.txt

# It shows that the bananas.txt file is not longer untracked, but now ready to be committed
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

If you got to here, you're quicker in making the homework than I'm in creating it. Below more things to do (but not worked out yet)

- Commit index into repo. Create a commit message
- Create another file, add it to the index
- Run git status
- Also edit the first file a bit
- Run git status
- Make a third file
- Run git status
- commit the current index (only file nr 2)
- add and commit file nr 1
- add and commit file nr 3
- delete file nr 1
- What does git status show now?
- add the delete-change to the index. What does git status show
- commit the delete
- Check git log
- Checkout a previous revision (let's say the second)
- Check the content of the directory and the files. Is it what you expect?
- Go back to the end of the branch

For this playtime, we start in an empty git repository (so create an empty directory and a git repository)

```console
$ pwd
/Userss/reinoud
$ mkdir playtime
$ cd playtime
$ git init
Initialized empty Git repository in /Users/reinoud/playtime/.git/
$ ls -la
total 0
drwxr-xr-x@  3 reinoud  staff    96 Apr 13 09:46 .
drwxr-x---+ 45 reinoud  staff  1440 Apr 13 09:46 ..
drwxr-xr-x@  6 reinoud  staff   192 Apr 13 09:46 .git
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Let's see the log (history) of this repository


Use `git log` to see the log

<!-- .element class="hidden-answer" -->

<button>show hint</button>


```console
$ git log
fatal: your current branch 'main' does not have any commits yet
# Actually, this makes lots of sense, since it's a new repo
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Let's make 5 files

```console
$ echo "hello 1" > 1.txt
$ echo "hello 2" > 2.txt
$ echo "hello 3" > 3.txt
$ echo "hello 4" > 4.txt
$ echo "hello 5" > 5.txt
# actually you could have done the above in a loop:
# for i in {1..5}; do echo "hello $i" > $i.txt; done
$ ls -la
total 40
drwxr-xr-x@  8 reinoud  staff   256 Apr 13 09:52 .
drwxr-x---+ 45 reinoud  staff  1440 Apr 13 09:46 ..
drwxr-xr-x@  6 reinoud  staff   192 Apr 13 09:46 .git
-rw-r--r--@  1 reinoud  staff     8 Apr 13 09:52 1.txt
-rw-r--r--@  1 reinoud  staff     8 Apr 13 09:52 2.txt
-rw-r--r--@  1 reinoud  staff     8 Apr 13 09:52 3.txt
-rw-r--r--@  1 reinoud  staff     8 Apr 13 09:52 4.txt
-rw-r--r--@  1 reinoud  staff     8 Apr 13 09:52 5.txt
$ git status -s
?? 1.txt
?? 2.txt
?? 3.txt
?? 4.txt
?? 5.txt
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

We commit them in 2 steps: first file 1, then file 2 & 3, (leaving 4 and 5 uncommitted)

```console
$ git add 1.txt
$ git status -s
A  1.txt
?? 2.txt
?? 3.txt
?? 4.txt
?? 5.txt
$ git commit -m "file 1"
[main (root-commit) 42303e9] file 1
 1 file changed, 1 insertion(+)
 create mode 100644 1.txt
$ git add 2.txt 3.txt
$ git commit -m "file 2 and 3"
[main 47722c3] file 2 and 3
 2 files changed, 2 insertions(+)
 create mode 100644 2.txt
 create mode 100644 3.txt
 $ git status -s
?? 4.txt
?? 5.txt
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Now make a file so that git will ignore `1.txt` and `5.txt`


Use  the `.gitignore` file

<!-- .element class="hidden-answer" -->

<button>show hint</button>


```console
$ echo "1.txt" >> .gitignore
$ echo "5.txt" >> .gitignore
$ cat .gitignore
1.txt
5.txt
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Check the git status and explain what you see

```console
$ git status -s
?? .gitignore
?? 4.txt
# files .gitignore and 4.txt are untracked
$ 5.txt is not here anymore because it's ignored by git
# Note that even though the .gitignore is not committed yet,
# it is already working
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Commit all files

```console
$ git add .
$ git commit -m "4.txt and gitignore"
[main de1eebe] 4.txt and gitignore
 2 files changed, 3 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 4.txt
$ git status -s
# nothing, so no local changes (5.txt is still ignored)
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Try to add `5.txt` to in the index (but don't force)

```console
$ git add 5.txt
The following paths are ignored by one of your .gitignore files:
5.txt
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false"
# You see that 5.txt is not being added, even though you could force it if you really wanted.
# Also note that you only get this message if you mention 5.txt by name;
# if you just do "git add .", you will not get any message
$ git status -s
# nothing, so 5.txt was not added to index
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

See the history of this repository

```console
$ git log
commit de1eebe51860ac5ea8b3803a4c613a0520fbb1e4 (HEAD -> main)
Author: Claude <github@claude.nl>
Date:   Thu Apr 13 10:02:47 2023 +0200

    4.txt and gitignore

commit 47722c394b1900b03ae109f7a6ab754ef07ab50a
Author: Claude <github@claude.nl>
Date:   Thu Apr 13 09:56:48 2023 +0200

    file 2 and 3

commit 42303e9dee9ccde68c07fdc02ca1661a1dc3a13f
Author: Claude <github@claude.nl>
Date:   Thu Apr 13 09:55:25 2023 +0200

    file 1
# You see the three commits. Note that the top-level commit has the (HEAD -> main) tag
# I actually have to press "q" to exit this view, but this depends on your settings
# vertical-scroll to see more "git log" magic
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

- `git log` is your workhorse to see what went on in your repository. It has endless configuration options to get what you want
- `git log | head -n 100` uses the `head` command to only show the first 100 lines
- `git log --pretty=FORMAT` allows you to choose from one of the built-in "pretty-formatting" options. Try some:
  - `git log --pretty=oneline`
  - `git log --pretty=short`
  - `git log --pretty=full`
  - `git log --pretty=oneline --abbrev-commit`  also makes the sha's shorter
  - `git log --oneline` is another way to do the previous command
- `git log --stat` gives you a nice overview about which commit changed what files

---

- Add one line to `1.txt`, `2.txt` and `5.txt` and explain the git status (with help of `.gitignore`)
- Commit `1.txt` and `2.txt`

```console
$ echo "bye 1" >> 1.txt
$ echo "bye 2" >> 2.txt
$ echo "bye 5" >> 5.txt
$ cat .gitignore
1.txt
5.txt
$ git status -s
 M 1.txt
 M 2.txt
# 1.txt and 2.txt are modified (but not in index yet, hence M in second column)
# 5.txt is still ignored
# Note that 1.txt is un-ignored; as soon as a file is part of git it's
# unignored, even if it's in .gitignore
$ git add .
# can use "git add ." since 5.txt is ignored anyways
$ git commit -m "changes"
[main 7141dae] changes
 2 files changed, 2 insertions(+)
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Remove `1.txt` from git (although not from working directory)

Use `git rm --cached FILENAME` to remove a file only from git (not from working directory)

<!-- .element class="hidden-answer" -->

<button>show hint</button>


```console
$ git rm --cached 1.txt
rm '1.txt'
$ git status -s
D  1.txt
# D in first column shows that it's Deleted from the index
$ git commit -m "remove 1.txt since it should not have been checked in"
[main 257c5ae] remove 1.txt since it should not have been checked in
 1 file changed, 2 deletions(-)
 delete mode 100644 1.txt
$ ls -la
total 48
drwxr-xr-x@  9 reinoud  staff   288 Apr 13 09:59 .
drwxr-x---+ 45 reinoud  staff  1440 Apr 13 09:46 ..
drwxr-xr-x@  9 reinoud  staff   288 Apr 13 10:29 .git
-rw-r--r--@  1 reinoud  staff    12 Apr 13 09:59 .gitignore
-rw-r--r--@  1 reinoud  staff    14 Apr 13 10:21 1.txt
-rw-r--r--@  1 reinoud  staff    14 Apr 13 10:21 2.txt
-rw-r--r--@  1 reinoud  staff     8 Apr 13 09:52 3.txt
-rw-r--r--@  1 reinoud  staff     8 Apr 13 09:52 4.txt
-rw-r--r--@  1 reinoud  staff    14 Apr 13 10:21 5.txt
# 1.txt is still there
$ git status -s
# 1.txt doesn't show up since it's in gitignore
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Do the same with `2.txt`; what are the differences

```console
$ git rm --cached 2.txt
rm '2.txt'
$ git status -s
D  2.txt
?? 2.txt
# Hey! we get something new. First line shows that 2.txt is removed in the index.
# Second line shows that we have an untracked 2.txt file
# This makes sense, since 2.txt is NOT in the gitignore file
$ git commit -m "remove 2.txt"
[main f683d45] remove 2.txt
 1 file changed, 2 deletions(-)
 delete mode 100644 2.txt
$ git status -s
?? 2.txt
# Still the untracked 2.txt
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

You're done. Let's keep the "playtime" directory for later.

Well.... almost done. There is a hrrible typo in this sheet!

Better go to Github and make an issue (normally you should first check if someone else already made an issue, but in this case, both of you make an issue)

- Go to github
- Find the reinhrst/nitwit2gitwit repo
- find this file in "lessons/6/playtime" (and click "code" to see the markdown)
- find the line with the problem, click on the line number before the line, and then on the three dots
- Choose "reference in new issue"
- Write a title and some more info, and click "submit new issue"

<!-- .element class="hidden-answer" -->

<button>show answer</button>

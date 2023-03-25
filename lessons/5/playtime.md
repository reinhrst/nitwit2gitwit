Create `unicorns.txt`, add it to the index (but don't commit!)

```console
$ pwd
/home/claude/minions
$ echo "Unicorns I love them,
Unicorns i love them,
Uni-Uni-Unicorns, I loove them!

Uni-Unicorns I could pet one
if they were really real..
And they are.
So i bought one so i could pet it.
" > unicorns.txt
$ ls -la
total 24
drwxr-xr-x 3 claude claude 4096 Mar 25 07:29 .
drwxr-x--- 1 claude claude 4096 Mar 24 17:50 ..
drwxr-xr-x 8 claude claude 4096 Mar 24 18:16 .git
-rw-r--r-- 1 claude claude  145 Mar 24 11:47 bananas.txt
-rw-r--r-- 1 claude claude   15 Mar 25 07:01 fluffy.txt
-rw-r--r-- 1 claude claude  183 Mar 25 07:29 unicorns.txt
$ git status -s
?? unicorns.txt
$ git add unicorns.txt
$ git status -s
A  unicorns.txt
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Make an edit (no matter what) to `bananas.txt`

```console
$ nano bananas.txt
# It doesn't matter what we do, I literally just added an `a` to  Bananahahaaa
# CTRL-O - enter - CTRL-X to quit

# We don't do git status now, because this is the next exercise
# But one star for you if you did :)
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Run `git status` (both with and without `-s`); explain what you see

```console
$ git status -s
 M bananas.txt
A  unicorns.txt
# Remember, first column is "what is happening in the index",
# Second "what is happening in local directory (relative to index)
# So bananas.txt is unchanged in the index (nothing will happen if you try to commit now)
# but there is a local change.
# unicorns.txt is added (as new file) to the index, and does not have local changes
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   unicorns.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   bananas.txt
# (Obviously) the same, but with more text :))
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Stage your changed in `bananas.txt` (and confirm with `git status` that all changed are staged now)

- To "stage" means "to add to the index". Also note that you're staging _your changes_ (you're adding _your changes_ to the index), you're not staging your file unless it's a new file (although, people often say "I'm staging my file").

<!-- .element class="hidden-answer" -->

<button>show hint</button>

```console
$ git add bananas.txt
$ git status -s
M  bananas.txt
A  unicorns.txt
# M is in the first column now!
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Make some more changes to both `unicorns.txt` and `bananas.txt` (still no commit)

```console
$ git status -s
M  bananas.txt
A  unicorns.txt
$ echo "One more unicorn" >> unicorns.txt
$ echo "One more banana" >> bananas.txt
# Remember, >> adds lines to a file, so the file will be one line longer now.
# (just here to show different ways to edit files; editing it with nano is completely fine as well)
# See below for more info

# again, git status is for the next exercise :)
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

- There are many ways do "edit a file".
- Nano is only one of the editors (actually the traditional editors on \*nix systems are `vi` or `vim` and `emacs`. Both are very very powerfull (quite a lot of programmers swear by them for all their work) but they are not very user-friendly (steep learning curve). So `nano` is used for people who don't want to start with 10 lessons of "how to use vim" :)
- In this example we used `>>` to add text to a file (usually one or more lines, but it could just be more text on the last line); this mode is called "append". You could also use a single `>` but this will overwrite the whole file (so the file would only be the one line).
- You could try to do something like (don't do this) `cat bananas.txt | tr a b > bananas.txt`. As we saw in lesson 2, `tr a b` replaces every `a` with a `b`. This will fail, because since all commands will run at the same time, so it will write to the file while reading from it, and the result is an empty file.....
- So you _could_ do something like `cat bananas.txt | tr a b > bananas1.txt && rm bananas.txt && mv bananas1.txt bananas.txt`

---

Run `git status`; explain what you see (or, if you want to get an extra star: predict what you will see before you run `git status` :))

```console
$ git status -s
MM bananas.txt
AM unicorns.txt
# So bananas.txt is modified in the index, and modified locally.
# unicorns.txt is added to the index, and modified locally
# so if we were to commit now..... (I won't tell you, because this is
# exactly what we'll be doing soon :))
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

- Run git status
- Also edit the first file a bit
- Run git status
- Make a third file
- Run git status
- commit the current index (only file nr 2)
- add and commit file nr 1
- add and commit file nr 3
- delete f

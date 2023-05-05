We'll continue in the playtime repository that we made last week.
- If you don't have this anymore, or want to make sure you start afresh, download the [zipfile containing that state here](https://www.dropbox.com/s/kt9ws03kipdqlo9/playtime.zip?dl=1)
- Make sure you do the above in a place where you don't already have a directory called "playtime".
- Remember that a git repository is nothing but a directory with a `.git` subdirectory (in a special format). So you can zip a whole repository and save the exact state (including what is in the working directory and in the index) and move it to a new computer, or email it to someone, etc.
- Tip: if you ever want to do something on a repository and you're not 100% sure that you won't destroy it all, you can just zip the whole directory and if you destroy everything, you can unzip and try again (or just copy the whole directory, rather than zipping it).
- If you want to be a commandline-guru, you can actually do `wget "https://www.dropbox.com/s/kt9ws03kipdqlo9/playtime.zip?dl=1" -O playtime.zip` to download the file, and `unzip playtime.zip` to unzip it. `wget` and `unzip` are installed on most (but not all) systems.

(see vertical-scroll for more)

vvvvvvvv

```console
$ pwd
/Users/reinoud
$ cd playtime
$ ls -la
total 48
drwxr-xr-x@  9 reinoud  staff   288 Apr 13 09:59 .
drwxr-x---+ 45 reinoud  staff  1440 Apr 13 09:46 ..
drwxr-xr-x@  9 reinoud  staff   288 Apr 16 18:02 .git
-rw-r--r--@  1 reinoud  staff    12 Apr 13 09:59 .gitignore
-rw-r--r--@  1 reinoud  staff    14 Apr 13 10:21 1.txt
-rw-r--r--@  1 reinoud  staff    14 Apr 13 10:21 2.txt
-rw-r--r--@  1 reinoud  staff     8 Apr 13 09:52 3.txt
-rw-r--r--@  1 reinoud  staff     8 Apr 13 09:52 4.txt
-rw-r--r--@  1 reinoud  staff    14 Apr 13 10:21 5.txt
$ git status -s
?? 2.txt
$ git ls-files
.gitignore
3.txt
4.txt
$ cat .gitignore
1.txt
5.txt
```

vvvvvvvv

- Last week we ended with 6 files:
  - 3 of which were checked in (`.gitignore`, `3.txt` and `4.txt`),
  - 2 were ignored (`1.txt` and `5.txt`),
  - and one was not tracked (`2.txt`).
- `git ls-files` works like the `ls` command but it lists the files in `HEAD` (remember, `HEAD` is the name of the currently checked out version)

vvvvvvvv

- You may be wondering why I provided a zip file, and not a GitHub repository to clone. Reasons are:
  - I want to end in the same spot where we left off.
    - A cloned repo will have a `remote` set.
    - A cloned repo only contains the checked-in files, here we have three files that are not checked in.
- But mostly it's to show how flexible this idea is that git is just files in a directory, and that you can just copy and share repos around by zipping them and copying directories.

---

Let's first commit `2.txt`


```console
$ git add 2.txt
$ git commit -m "checking in 2.txt again"
[main 6edd0b5] checking in 2.txt again
 1 file changed, 2 insertions(+)
 create mode 100644 2.txt
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

We need all files for this exercise, so let's not ignore any files anymore.

The easiest way to do this is to remove the `.gitignore` file (alternatively you can also make it empty).

<!-- .element class="hidden-answer" -->

<button>show hint</button>

To remove a file, easiest is just remove it from the working directory, and then do `git add .gitignore`; note that `git add .gitignore`, adds all _changes_ in that file, and removing a file is a change (so it's not a contradiction to use `add`).

<!-- .element class="hidden-answer" -->

<button>show hint2</button>

(answer: scroll down)

vvvvvvvv

```console
$ rm .gitignore
$ git status -s
 D .gitignore
?? 1.txt
?? 5.txt
# Note that we also have 1.txt and 5.txt now in here, since we're not ignoring them anymore
$ git add .gitignore
git status -s
D  .gitignore
?? 1.txt
?? 5.txt
# D in first column shows that the delete-change is now in the index
$ git commit -m "un-ignoring all files"
[main 6c51e89] un-ignoring all files
 1 file changed, 2 deletions(-)
 delete mode 100644 .gitignore
# If you accidentally also committed 1.txt and 5.txt, you learned a lesson now why you should always do
# git status and git diff --cached before committing. But for now no need to fix it, you can skip the next
# exercise.
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

- Another way to delete a file in git is using `git rm`.
- `git rm` deletes the file both in the index and in the working directory
- (you can also do `git rm --cached` to only delete in the index (keep the file in the working directory), remember `cached` is the old name for the index)
- `git rm --cached` is very useful if you accidentally added a file to git (e.g. a data file), and you now added to the file to `.gitignore`, but you still need to delete the file in git (but want to keep it locally).

vvvvvvvv

Below a solution to the exercise using `git rm`


```console
$ git rm .gitignore  # not --cached, we want to delete it in the working dir too
$ git status -s
D  .gitignore
?? 1.txt
?? 5.txt
# D in first column shows that the delete-change is already in the index
$ git commit -m "un-ignoring all files"
[main 6c51e89] un-ignoring all files
 1 file changed, 2 deletions(-)
 delete mode 100644 .gitignore
```

---

Now commit `1.txt` and `5.txt`

```console
$ git add .
$ git status -s
A  1.txt
A  5.txt
$ git commit -m "remaining files"
[main 86c3234] remaining files
 2 files changed, 4 insertions(+)
 create mode 100644 1.txt
 create mode 100644 5.txt
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

So now we're (finally) ready to do some branching!

We want to build this:

<pre class="mermaid">
gitGraph
    commit id: "1"
    commit id: "2"
    commit id: "3"
    branch dangerous-experiment
    checkout main
    commit id: "M1"
    commit id: "M2"
    checkout dangerous-experiment
    commit id: "A1"
    commit id: "A2"
    checkout main
    commit id: "M3"
</pre>

We're assuming we're now at commit `3`.

(continued below)

vvvvvvvv

Check which branch we're on

```console
$ git status
On branch main
nothing to commit, working tree clean
$ git status -sb
## main
$ git branch
* main
# There are many ways to check your current branch; above you see some examples
# `git status -sb` is actually `git status -s -b` or `git status --short --branch`
# `git branch` shows all (local) branches, with a star * in front of your current branch
# depending on your git version, `git log` may also show you your branch
# and probably there are 25 other ways :)
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Since we're in commit `3` in the diagram, we now want to make a new branch `dangerous-experiment` but not commit anything in that branch. Do so :)

```console
$ git checkout -b dangerous-experiment
Switched to a new branch 'dangerous-experiment'
# Using `-b` you create a new branch (without -b, you just switch branch)
# note that (as it says) it also switched to the new branch
$ git branch
* dangerous-experiment
  main
# The * denotes that we're on branch "dangerous-experiment"
# Since we will want to make the next commit to the "main" branch, let's switch back to main
$ git checkout main
Switched to branch 'main'
$ git branch
  dangerous-experiment
* main
# So we're back on main
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

Nine out of ten times that you make a new branch, you will want to commit something to that new branch, so it makes sense that the command switches to that new branch.
Often you already have lots of changes in your local directory, and only then decide that you don't want to commit to the main branch. It's completely ok to call `git checkout -b NEWBRANCH` with a lot of stuff in your working directory (or even in the index). Only when you commit, the changes in the index are being written to the branch that's active at that time.

You can actually use `git branch`  (with some options) to create a new branch without switching to it, but we'll skip that for now.

---

Check the history, and look at the three most recent commits. Now switch to branch `dangerous-experiment` and do the same. Explain what you see.

Use `git log` to see the history

<!-- .element class="hidden-answer" -->

<button>show hint</button>

```console
$ git log
[.... some output ...]
$ git checkout dangerous-experiment
Switched to branch 'dangerous-experiment'
$ git log
[.... almost the same output ...]
# The results are the same. Even though we like to draw the diagrams (and also have this mental
# image) that there are a bunch on commits in "main" and none in "dangerous-experiment",
# this is not true. A branch is just a label pointing to the most recent commit, and at this
# point both the "main" and the "dangerous-experiment" commit point to the same sha.
# This sha (obviously) has the same commits, regardless of which branch we're viewing.
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Make 2 commits on main (change `1.txt` for the first commit and `2.txt` for the second commit

```console
$ git checkout main
Switched to branch 'main'
# Let's make sure we're on main. Note that even when we're already on "main", there is no
# problem in calling "git checkout main"; it will just stay on main. Let's just call it again for fun.
$ git co main
Already on 'main'
$ git status
On branch main
nothing to commit, working tree clean
# OK, where we want to be
$ echo "one new line" >> 1.txt
$ git add 1.txt
$ git diff --cached
diff --git a/1.txt b/1.txt
index ebed9cc..9562d38 100644
--- a/1.txt
+++ b/1.txt
@@ -1,2 +1,3 @@
 hello 1
 bye 1
+one new line
# Looks good, let's go
$ git commit -m "M1"
[main 4981ad3] M1
 1 file changed, 1 insertion(+)
$ echo "also one more line" >> 2.txt
$ git add 2.txt
$ git diff --cached
diff --git a/2.txt b/2.txt
index e737809..488b74e 100644
--- a/2.txt
+++ b/2.txt
@@ -1,2 +1,3 @@
 hello 2
 bye 2
+also one more line
$ git commit -m "M2"
[main d1112f6] M2
 1 file changed, 1 insertion(+)
# As you can see, I use M1 and M2 as commit messages; they match the names used in the diagram
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Check the history (again), and look at the three most recent commits. Now switch to branch `dangerous-experiment` and do the same. Explain what you see now.

```console
$ git log
[.... some output with M1 and M2 commits ...]
$ git checkout dangerous-experiment
Switched to branch 'dangerous-experiment'
$ git log
[.... No M1 and M2 commits ...]
# Since we switched branch, M1 and M2 are not in "git log" anymore.
# "git log" shows the current HEAD commit and all parents (so in practice: the current branch)
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

Print the content of 1.txt. Where did the line we just added (in M1) go?

```console
$ git status -sb
## dangerous-experiment
$ cat 1.txt
hello 1
bye 1
# The line we added is not here. It was committed in M1 and M1 is not a parent of the current commit (is not in the current branch).
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Make 2 commits on branch "dangerous-experiment" (change `3.txt` for the first commit and `4.txt` for the second commit)

```console
$ git checkout dangerous-experiment
Already on branch 'dangerous-experiment'
$ echo "one more line nr 3" >> 3.txt
$ git add 3.txt
$ git commit -m "A1"
[dangerous-experiment 2380c8f] A1
 1 file changed, 1 insertion(+)
$ echo "one more line 4" >> 4.txt
$ git add 4.txt
$ git commit -m "A2"
[dangerous-experiment ab666d9] A2
 1 file changed, 1 insertion(+)
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

The good student will complain that I did not do `git status` and `git diff --cached` in my solution. They are right. In real life you should always do that, however the solutions become very large and unreadable with all that extra stuff. In rare cases (when the commits I'm doing are very trivial) I may sometimes skip them in real life (but really only very occasionally!)...

vvvvvvvv

It helps to keep a mental map of what we're doing with branches at all time; we're now here

<pre class="mermaid">
gitGraph
    commit id: "1"
    commit id: "2"
    commit id: "3"
    branch dangerous-experiment
    checkout main
    commit id: "M1"
    commit id: "M2"
    checkout dangerous-experiment
    commit id: "A1"
    commit id: "A2" tag: "HEAD"
</pre>

There is actually a git command that can show this:
```console
$ git log --graph --oneline --all --decorate
```

Run this and try to understand what you see (scroll vertically to see explanation).

vvvvvvvv

```console
$ git log --graph --oneline --all --decorate
* ab666d9 (HEAD -> dangerous-experiment) A2
* 2380c8f A1
| * e599eb3 (main) M2
| * 4ee7994 M1
|/
* cebab9c new files
* b928972 remove gitignore
* dff3a76 add 2.txt again
* f683d45 remove 2.txt
* 257c5ae remove 1.txt since it should not have been checked in
* 7141dae changes
* de1eebe 4.txt and gitignore
* 47722c3 file 2 and 3
* 42303e9 file 1
# It may take some effort to understand what we see here. I explained before that the idea
# that the main branch has 11 commits and the dangerous-experiment branch has 2 commits (as we
# like to show in the colourful diagrams) is actually not how it works in git.
# In git, both branches have 11 commits, of which the first 9 are the same (and then each branch
# has 2 different commits)
# In this output you see the tree grow from the bottom (42303e9) up until cebab9c. Then it splits
# into two branches.
# It may help to run the same command without the --oneline parameter; it will take much more
# space, but the tree structure is clearer.
```

---

Now on the main branch, change and commit `5.txt`. Print the full tree again and try to understand.


```console
$ git checkout main
Switched to branch 'main'
$ echo "and the fifth extra line" >> 5.txt
$ git add 5.txt
$ git commit "M3"
[main aab1e86] M3
 1 file changed, 1 insertion(+)
$ git log --graph --oneline --all --decorate
* aab1e86 (HEAD -> main) M3
* e599eb3 M2
* 4ee7994 M1
| * ab666d9 (dangerous-experiment) A2
| * 2380c8f A1
|/
* cebab9c new files
* b928972 remove gitignore
* dff3a76 add 2.txt again
* f683d45 remove 2.txt
* 257c5ae remove 1.txt since it should not have been checked in
* 7141dae changes
* de1eebe 4.txt and gitignore
* 47722c3 file 2 and 3
* 42303e9 file 1
# Right now the main branch is to the left; I'm not sure what decides what branch is printed to
# the left and right (and it may actually differ between versions of git).
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

You may have noticed that in the tree view the commits are not in chronological order anymore (since M1 and M2 were committed _before_ A1 and A2, however appear later in the view.

Git assumes that there is no dependency between the commits in different branches, so it really doesn't matter which one was first in time (generally a reasonable assumption); instead it tries to keep commits on one branch together. However if you really want to, you can add `--date-order` to the command:

```console
$ git log --graph --oneline --all --decorate --date-order
* aab1e86 (HEAD -> main) M3
| * ab666d9 (dangerous-experiment) A2
| * 2380c8f A1
* | e599eb3 M2
* | 4ee7994 M1
|/  
* cebab9c new files
* b928972 remove gitignore
* dff3a76 add 2.txt again
* f683d45 remove 2.txt
* 257c5ae remove 1.txt since it should not have been checked in
* 7141dae changes
* de1eebe 4.txt and gitignore
* 47722c3 file 2 and 3
* 42303e9 file 1
```

And how we have something that looks a lot like the blue-yellow graph at the start!

---

Now merge `dangerous-experiment` into `main`

Use `git merge BRANCHNAME` to merge that branch into `HEAD`

<!-- .element class="hidden-answer" -->

<button>show hint</button>

```console
$ git status -sb
## main
# We need to be on the branch that we want to merge into
$ git merge dangerous-experiment
# Now (edit if you want and) save the default commit message
Merge made by the 'ort' strategy.
 3.txt | 1 +
 4.txt | 1 +
 2 files changed, 2 insertions(+)
# And we're done. Let's see the result
$ git log --graph --oneline --all --decorate --date-order
*   9b5cfb2 (HEAD -> main) Merge branch 'dangerous-experiment'
|\
* | aab1e86 M3
| * ab666d9 (dangerous-experiment) A2
| * 2380c8f A1
* | e599eb3 M2
* | 4ee7994 M1
|/
* cebab9c new files
* b928972 remove gitignore
* dff3a76 add 2.txt again
* f683d45 remove 2.txt
* 257c5ae remove 1.txt since it should not have been checked in
* 7141dae changes
* de1eebe 4.txt and gitignore
* 47722c3 file 2 and 3
* 42303e9 file 1
# As you can see, we have a nice merging of branches.
# Also you see that "dangerous-experiment" still points to the A2 commit, which is the latest commit
# in this branch. Since we're done with dangerous-experiment, we will delete the branch.
$ git branch --delete dangerous-experiment
Deleted branch dangerous-experiment (was ab666d9).
# Remember that it only allows us to delete the branch if it's merged, else we have to use
# git branch --delete --force BRANCHNAME
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

We used in this case the merge-commit strategy on the merge (which is default, unless a fast-forward is possible (I think)). You can see that since only the merge-commit results in a tree with branches coming together again (circles in the tree). However the output of the command said `Merge made by the 'ort' strategy`. What's going on?

Actually `ort` is the strategy for how to do a merge-commit; it is about how to deal with merge conflicts etc. For now this is too detailed for this course. Just so you know, `ort` is the strategy on a different level.

vvvvvvvv

At the end of the merge, we deleted the branch.

Nothing bad will happen if you don't delete it, except that in a year time you will end up with 500 branches and you don't really remember which ones are merged, which not, etc (especially if some are your branches and some are of co-authors, you really don't know what's what anymore). Obviously at that point git (and GitHub) can help you to find the branches that were fully merged, however I personally think it's just good house-keeping to clean up once you're done with a branch (recreating the branch in the future if you need it again will take 2 seconds).

When we have GitHub in the mix as well, it will take another step to also delete the remote branch, but still, it's worth it in the long run :).

---

Finally for this week, we'll make (and resolve) a merge-conflict.

To work on this, we'll be using the New Zealand National Anthem: "God Save New Zealand" (please open [on wikipedia](https://en.wikipedia.org/wiki/God_Defend_New_Zealand#Lyrics) and scroll down to the lyrics).

So in a repository (either use the same, or make a new one), we will now make a file `anthem.txt` with the first two strophes (so the God Nations... and the Men of every creed) seperated by a blank line. Commit this file.

(answer scroll down)

vvvvvvvv

```console
$ echo "God of Nations at Thy feet,
In the bonds of love we meet,
Hear our voices, we entreat,
God defend our free land.
Guard Pacific's triple star
From the shafts of strife and war,
Make her praises heard afar,
God defend New Zealand.

Men of every creed and race,
Gather here before Thy face,
Asking Thee to bless this place,
God defend our free land.
From dissension, envy, hate,
And corruption guard our state,
Make our country good and great,
God defend New Zealand." > anthem.txt
$ git add anthem.txt
$ git commit -m "anthem"
[main dbfda96] anthem
 1 file changed, 17 insertions(+)
 create mode 100644 anthem.txt
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

In case you're wondering why we take such a long text (the 1-line `1.txt` etc files worked fine before); the reason is that merge conflicts on 1-line files are trivial; whereas any merge conflict you'll encounter in real life is likely to be on longer files.

---

Make a new branch (`maori`) and change the first line, the 6th line (From the shafts...), the 8th line and the last line into Māori, and commit this.

```console
$ git checkout -b maori
Switched to a new branch 'maori'
$ nano anthem.txt
# easiest to change the file with nano and then save and exit
# it should look like this:
$ cat anthem.txt
E Ihowā Atua,
In the bonds of love we meet,
Hear our voices, we entreat,
God defend our free land.
Guard Pacific's triple star
Kia tau tō atawhai;
Make her praises heard afar,
Aotearoa

Men of every creed and race,
Gather here before Thy face,
Asking Thee to bless this place,
God defend our free land.
From dissension, envy, hate,
And corruption guard our state,
Make our country good and great,
Aotearoa
# Don't worry if you don't have the accents or typos or anything, it's not important for what we do, as long as you change those lines and only those lines
$ git add anthem.txt
$ git commit -m "making a start of the Māori translation"
[maori c4563ae] making a start of the Māori translation
 1 file changed, 4 insertions(+), 4 deletions(-)
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

Note that although it's legal to use non-ASCII characters (like the ā in Māori) in a branch name, I would highly suggest not doing so unless you really have to (i.e. in Polish, always use the not-accented characters in branchnames (as well as in any filenames); it's obviously a different story if you work on a project that is in Russian or Chinese).

At the same time, I have no problem using non-ASCII characters in commit messages as you see in the answer. The rule here is (more or less): a commit message you type once and afterwards only read. Also, if there is a problem (i.e. it will say MÅéori instead of Māori on some systems) it will not be such a big problem. This is different for branch names and filenames.

---

Now go to the main branch, and here we also edit the anthem (note that the changes we made before are gone now). This time we change the 1st, 2nd line, as well as in the second part the 3rd (Asking Thee) and the penultimate line (Make out country). Change those lines into the Literal translation of the Māori text).

(answer scroll down)

vvvvvvvv


```console
$  git checkout main
Switched to branch 'main'
$ nano anthem.txt
$ cat anthem.txt
O Lord, God,
Of all people
Hear our voices, we entreat,
God defend our free land.
Guard Pacific's triple star
From the shafts of strife and war,
Make her praises heard afar,
God defend New Zealand.

Men of every creed and race,
Gather here before Thy face,
Māori or Pākehā
God defend our free land.
From dissension, envy, hate,
And corruption guard our state,
Live in peace
God defend New Zealand.
# Again, only important thing is that you changed the right lines (and
# into something else than in the moari branch)
$ git add anthem.txt
$ git commit -m "literal maori translation"
[main 7bbefbe] literal maori translation
 1 file changed, 4 insertions(+), 4 deletions(-)
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Now, we're ready to merge. Try to predict in your head where conflicts will arise, and try to merge (merge-commit).

```console
$ git status -sb
## main
$ git merge maori
Auto-merging anthem.txt
CONFLICT (content): Merge conflict in anthem.txt
Automatic merge failed; fix conflicts and then commit the result.
# Git says that it tries to merge anthem.txt automatically (since both branches changed it;
# often different branches will have changed different files, so there is no need to even
# automatically merge a file).
# However, there is a conflict (in the content; in theory you can also have conflicts in
# metadata set on the file, but let's ignore this for now) in anthem.txt.
# We need to fix the conflicts, and then recommit.
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

So let's look at the file and find the conflicts.

```console
$ cat anthem.txt
<<<<<<< HEAD
O Lord, God,
Of all people
=======
E Ihowā Atua,
In the bonds of love we meet,
>>>>>>> maori
Hear our voices, we entreat,
God defend our free land.
Guard Pacific's triple star
Kia tau tō atawhai;
Make her praises heard afar,
Aotearoa

Men of every creed and race,
Gather here before Thy face,
Māori or Pākehā
God defend our free land.
From dissension, envy, hate,
And corruption guard our state,
<<<<<<< HEAD
Live in peace
God defend New Zealand.
=======
Make our country good and great,
Aotearoa
>>>>>>> maori
```
<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

- So we see two conflicts. The first in lines 1 & 2, the second in the two last lines.
- The changes in lines 6 and 8 (in maori branch), and in the 3rd line of the second strophe (in main branch), were merged without a problem.
- However in the last two lines, there is a conflict, even though maori branch changed the last line, and main branch the penultimate one.
- Generally git is happy to merge changes if the line or any close-by line is not edited in the other branch (I'm sure what "close-by" means can be set somewhere, but by default it's (I think) 1 line around).
- If the line or a close-by line _was_ changed in the other branch as well, you get a conflict.
- Note that git uses some smart algorithm to determine what "the same line" means (so that if you delete 10 lines in one commit, it still knows which lines in branch A map to which lines in branch B.

---

Abort the merge, and check that it aborted

Use `git merge --abort` to abort the merge

<!-- .element class="hidden-answer" -->

<button>show hint</button>

(answer scroll down)
vvvvvvvv

```console
$ git merge --abort
$ git status -sb
## main
# makes sense, we're still on the main branch
$ cat anthem.txt
O Lord, God,
Of all people
Hear our voices, we entreat,
God defend our free land.
Guard Pacific's triple star
From the shafts of strife and war,
Make her praises heard afar,
God defend New Zealand.

Men of every creed and race,
Gather here before Thy face,
Māori or Pākehā
God defend our free land.
From dissension, envy, hate,
And corruption guard our state,
Live in peace
God defend New Zealand.
# The latest version from main, no conflicts no nothing.
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Try the merge again. This time, fix `anthem.txt` when it gives you a conflict and finish the merge.

```console
$ git status -sb
## main
$ git merge maori
Auto-merging anthem.txt
CONFLICT (content): Merge conflict in anthem.txt
Automatic merge failed; fix conflicts and then commit the result.
$ nano anthem.txt
# Fix the conflict (choose one version, or the other, or decide what you want)
# Note that git really doesn't care what you do, you can even not change anything and just
# mark the whole file (including the <<<<<<< HEAD texts) as (conflict) resolved.
# This is also why you always have to manually check when you fix a conflict that there is not
# another conflict further down in the file; git won't complain if you check it in
$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   anthem.txt

no changes added to commit (use "git add" and/or "git commit -a")
# just showing what it looks like in git status
$ git add anthem.txt
# with "git add" you tell git that you resolved the conflicts in this file.
# in this case there is only one file with conflicts, so you only have to git add one file.
$ git status
On branch main
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
	modified:   anthem.txt
# git status helpfully tells us how we're doing: all conflicts resolved, but still merging
# finish merging by using "git commit". You can supply a commit message with "-m" in this case
# but with a merge I prefer the text editor to edit the commit message (because it fills in a useful
# default commit message. usually I just accept the default message).
$ git commit
[main dd7826c] Merge branch 'maori'
$ git branch -d maori  # clean up after ourselves
Deleted branch maori (was dbfb879).
$ git log --graph --oneline --all --decorate
*   dd7826c (HEAD -> main) Merge branch 'maori'
|\
| * dbfb879 (maori) making a start of the Māori translation
* | 7bbefbe literal maori translation
|/
* 42c37de anthem
*   102db4e Merge branch 'dangerous-experiment'
|\
| * ab666d9 (dangerous-experiment) A2
| * 2380c8f A1
* | aab1e86 M3
* | e599eb3 M2
* | 4ee7994 M1
|/
* cebab9c new files
* b928972 remove gitignore
* dff3a76 add 2.txt again
* f683d45 remove 2.txt
* 257c5ae remove 1.txt since it should not have been checked in
* 7141dae changes
* de1eebe 4.txt and gitignore
* 47722c3 file 2 and 3
# our beautiful tree with 2 merged branches
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

During a "merge-resolve-conflict" you can change anything, not just the files that have conflicts. However it's good git-etiquettes (gitiquettes?) to only make those changes that are resolving merge conflicts. If e.g. you spot, while fixing the merge conflict, a typo in the file you edit, don't fix it, but make a note to yourself, first finish the merge, and only then fix the typo (in a new commit).


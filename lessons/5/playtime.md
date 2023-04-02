For this playtime, we continue where we left off last time:

```console
$ pwd
/home/claude/minions
$ ls -la
total 20
drwxr-xr-x 3 claude claude 4096 Mar 24 11:24 .
drwxr-x--- 1 claude claude 4096 Mar 24 17:50 ..
drwxr-xr-x 8 claude claude 4096 Mar 24 18:16 .git
-rw-r--r-- 1 claude claude  145 Mar 24 11:47 bananas.txt
-rw-r--r-- 1 claude claude   15 Mar 25 07:01 fluffy.txt
$ git status
# no reply means no local changes and no changes in the index
```

---

We're first going to check some differences between changes in index and changes in working directory

---
Stage your changes in `bananas.txt` (and confirm with `git status` that all changed are staged now)
- To "stage" means "to add to the index". Also note that (technically) you're staging _your changes_ (you're adding _your changes_ to the index), you're not staging your file unless it's a new file (although, people often say "I'm staging my file"). There are ways to stage only certain changes in your file, but this should generally only be a last resort (since you shouldn't be working on more than one problem at a time anyways).
- You could try to do something like (don't do this) `cat bananas.txt | tr a b > bananas.txt`. As we saw in lesson 2, `tr a b` replaces every `a` with a `b`. This will fail, because since all commands will run at the same time, it will write to the file while reading from it, and the result is an empty file.....
Before committing, we'll use `git diff` to see what changes we have.
- Run `git diff` and explain what you see

```console
# remember to scroll to the bottom for the whole story
$ git diff
diff --git a/bananas.txt b/bananas.txt
index 4b53994..e2067f9 100644
--- a/bananas.txt
+++ b/bananas.txt
@@ -7,3 +7,4 @@ Tokadido Pokatoli
 Kalimanomani
 Tanotika
 Ba Ba Ba, Ba Ba Na Na
+One more banana
diff --git a/unicorns.txt b/unicorns.txt
index 9a64460..c12cf20 100644
--- a/unicorns.txt
+++ b/unicorns.txt
@@ -7,3 +7,4 @@ if they were really real..
 And they are!
 So i bought one so i could pet it.

+One more unicorn

# "git diff" shows a unified diff (as we saw a couple of weeks ago,
# using "diff -u file1 file2". Rather than giving it two files, it shows the diff
# between two git-versions.
# Without any extra parameters, "git diff" shows the difference between
# the files in the index, and the files in the working directory.
#
# Obviously your exact diff may look different depending on the content of your files
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv


One small detail to add is that `git diff` shows the diff between the the index and the working directory only for those files that are in the index. So if you have files in your working directory that you never did `git add` on, they are not included in the diff.


---

- Run `git diff --staged` and explain what you see

```console
$ git diff --staged
diff --git a/bananas.txt b/bananas.txt
index 1abe203..4b53994 100644
--- a/bananas.txt
+++ b/bananas.txt
@@ -1,6 +1,6 @@
 Ba Ba Ba, Ba Ba Na Na
 Ba Ba Ba, Ba Ba Na Na
-Bananahahaaa
+Bananahahaaaaaaaaa
 Potatoo nahahaaa

 Tokadido Pokatoli
diff --git a/unicorns.txt b/unicorns.txt
new file mode 100644
index 0000000..9a64460
--- /dev/null
+++ b/unicorns.txt
@@ -0,0 +1,9 @@
+Unicorns I love them,
+Unicorns i love them,
+Uni-Uni-Unicorns, I loove them!
+
+Uni-Unicorns I could pet one
+if they were really real..
+And they are!
+So i bought one so i could pet it.
+
# "git diff --staged" shows the diff between the current revision in git,
# and the version in the index
# In other words, it shows exactly what would be committed if we run "commit".
# Therefore it is a good idea to always run "git diff --staged" before a
# "git commit", so that you're sure which changes you're committing.
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

In case you ever see someone else do this: `git diff --cached` is the same as `git diff --staged`. 

Cache is the original name for the index, hence the `--cached`. However, using `--index` will not work, and is actually used in other contexts (to keep things simple).

You'll see it a lot with git that many actions can be achieved with different commands. People that used git in the early days will use certain commands (that worked back then) while by now there are more user-friendly commands at hand.

Where possible I will try to use the more modern/more user-friendly commands here, even though I personally would never use them :).

---

- Add the unstaged changes in `bananas.txt` to the index as well, so that all changes (both the ones currently in the index, and the ones currently in the working directory) are in the index
- Confirm that this worked with `git status` and `git diff --staged`

```console
$ git add bananas.txt
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   bananas.txt
        new file:   unicorns.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   unicorns.txt
# This shows that there are no changes in bananas.txt anymore that are not
# in the index. You can see the same with "git status --short"
$ git diff --staged
diff --git a/bananas.txt b/bananas.txt
index 1abe203..e2067f9 100644
--- a/bananas.txt
+++ b/bananas.txt
@@ -1,9 +1,10 @@
 Ba Ba Ba, Ba Ba Na Na
 Ba Ba Ba, Ba Ba Na Na
-Bananahahaaa
+Bananahahaaaaaaaaa
 Potatoo nahahaaa

 Tokadido Pokatoli
 Kalimanomani
 Tanotika
 Ba Ba Ba, Ba Ba Na Na
+One more banana
diff --git a/unicorns.txt b/unicorns.txt
new file mode 100644
index 0000000..9a64460
--- /dev/null
+++ b/unicorns.txt
@@ -0,0 +1,9 @@
+Unicorns I love them,
+Unicorns i love them,
+Uni-Uni-Unicorns, I loove them!
+
+Uni-Unicorns I could pet one
+if they were really real..
+And they are!
+So i bought one so i could pet it.
+
# There you have it, the line "One more banana" is now in the index (as well as the 

```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Now the opposite, we want the changes in `bananas.txt` not in the index any longer. Afterwards, confirm that you succeeded.

If you look at the output of the `git status` command, it actually shows you how to do this.

<!-- .element class="hidden-answer" -->

<button>show hint</button>

```console
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   bananas.txt
        new file:   unicorns.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   unicorns.txt
# It says we should use "git restore --staged <file>" to unstage
$ git restore --staged bananas.txt
$ git status --short
 M bananas.txt
AM unicorns.txt
# As you can see, only an M in the second column, so nothing in the index anymore
$ git diff --staged
diff --git a/unicorns.txt b/unicorns.txt
new file mode 100644
index 0000000..9a64460
--- /dev/null
+++ b/unicorns.txt
@@ -0,0 +1,9 @@
+Unicorns I love them,
+Unicorns i love them,
+Uni-Uni-Unicorns, I loove them!
+
+Uni-Unicorns I could pet one
+if they were really real..
+And they are!
+So i bought one so i could pet it.
+
# No more bananas. You could also look at "git diff" and see that all diffs are in there.
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>


vvvvvvvv

The old way of doing `git restore --staged <file>` is `git reset <file>`, so you may sometimes encounter that too.

It's also useful to imagine what the `git restore --staged <file>` command actually means. It means "_restore_ the _<file>_ in the _staged_ version (=index) (to how it looks in the current revision).

Note that this command does not actually change the file in the working directory. The `bananas.txt` file in the working directory always had all changes in it, however _compared to the index_ it had fewer changes when some of the changes were already staged.

---

Finally, what you've been waiting for. Commit the index!

```console
$ git commit -m "unicorn song"
[main b70de99] unicorn song
 1 file changed, 9 insertions(+)
 create mode 100644 unicorns.txt
$ git status --short
 M bananas.txt
 M unicorns.txt
# Both only have local changes, nothing in index anymore
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

Show the diff but only for the `unicorn.txt` file

`git diff` takes extra parameters; if the extra parameter is a filename, it shows the diff only for that file.

<!-- .element class="hidden-answer" -->

<button>show hint</button>

```console
$ git diff unicorns.txt
diff --git a/unicorns.txt b/unicorns.txt
index 9a64460..c12cf20 100644
--- a/unicorns.txt
+++ b/unicorns.txt
@@ -7,3 +7,4 @@ if they were really real..
 And they are!
 So i bought one so i could pet it.

+One more unicorn
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

Many `git` commands take parameters, and often the parameters can be either a filename or a `commitref` (a `commitref` is anything that points to a commit; this can be a `sha`, a `tag`, a `branch`, etc; we'll dive into these in a future lesson).

`git diff` is a good example here. `git diff unicorn.txt` shows the diff of `unicorn.txt` whereas `git diff 123abcd` shows the diff between the working directory and revision with sha `123abcd` (this will not work for you, since your repository will not have a revision with this sha).

This obviously leads to a problem when something is both a filename and a `commitref`; something like this most often happens if you have a directory called `bananas` and also a branch called `bananas`.

Therefore, it's often suggested to make sure that you don't make branches with the names of files or directories :).

---

We have changed our mind. `unicorn.txt` is fine the way it is (in git) and we want to remove the changes in the local directory.

Remember what `git restore --staged <file>` actually does, and what the different parts of the command mean.

<!-- .element class="hidden-answer" -->

<button>show hint</button>

```console
$ git diff unicorns.txt
diff --git a/unicorns.txt b/unicorns.txt
index 9a64460..c12cf20 100644
--- a/unicorns.txt
+++ b/unicorns.txt
@@ -7,3 +7,4 @@ if they were really real..
 And they are!
 So i bought one so i could pet it.

+One more unicorn

# So if "git restore --staged unicorns.txt" restores the version in the index,
# without "--staged" it will restore the version in the working directory
$ git restore unicorns.txt
$ git diff unicorns.txt
# No output, means no diff
$ git status --short
 M bananas.txt
# As you can see, there is no more unicorns.txt here (in the status; you can
# check with "ls" and "cat" that the unicorns.txt file is still there)
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

Another (older) way to do this is `git checkout unicorns.txt`.

Files that are restored this way, are overwritten with the version from the latest revision. There is no way to get back your changes if you accidentally do this (sometimes you can still get your original file back in the editor if you have it open, but not always). Another good reason to commit stuff often!

---

Now commit the local changes in `bananas.txt` to the repository.

```console
$ git status --short
 M bananas.txt
$ git add .
$ git status --short
M  bananas.txt
$ git diff --staged
diff --git a/bananas.txt b/bananas.txt
index 1abe203..e2067f9 100644
--- a/bananas.txt
+++ b/bananas.txt
@@ -1,9 +1,10 @@
 Ba Ba Ba, Ba Ba Na Na
 Ba Ba Ba, Ba Ba Na Na
-Bananahahaaa
+Bananahahaaaaaaaaa
 Potatoo nahahaaa

 Tokadido Pokatoli
 Kalimanomani
 Tanotika
 Ba Ba Ba, Ba Ba Na Na
+One more banana
# Always do a "git diff --staged" to check what you're actually about to commit
$ git commit -m "almost done"
[main 6c5fd12] almost done
 1 file changed, 2 insertions(+), 1 deletion(-)
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv

Rather than using `git add bananas.txt` I used `git add .`. As you may recall, `.` is the current directory, so with this command I add all the changes in the current directory to the index (`git add bananas.txt` would obviously have worked just as well in this case, I just wanted to do something else :)).

---

Now finally, use `git log` to see all commits

```console
$ git log
commit 6c5fd12ff047afb1161a024834f601d859f7252f (HEAD -> main)
Author: Claude <claude@claude.nl>
Date:   Sat Apr 1 18:45:58 2023 +0000

    almost done

commit 01e01c1fb55cb2f0163fcd5ff745d061b77ffc53
Author: Claude <claude@claude.nl>
Date:   Sat Apr 1 18:11:14 2023 +0000

    unicorn song

commit 1fee07a4e0e3c7b81daf5ba1cd15f9d62d880b40
Author: Claude <claude@claude.nl>
Date:   Sat Apr 1 18:10:05 2023 +0000

    exercise 26

commit 4075390e1ad1b5708bb58cef5e8cce901509e1e5
Author: Claude <claude@claude.nl>
Date:   Fri Mar 24 17:50:15 2023 +0000

    Bananas for minions
# "git log" shows a chronological timeline of your commits.
# you can use extra parameters to define the exact output format you want to have
# On the top you can see the most recent commit (which also is the "HEAD" of
# branch "main".
# in larger repositories we (obviously) usually want to see only some of the commits.
# As you may remember from an earlier lesson, you can limit your output by piping:
# "git log | head -n 10" (try this now) shows only the first 10 lines
```

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvvvv


---


# ⭐️⭐️⭐️ Done ⭐️⭐️⭐️

Don't forget to regularly commit your own work!
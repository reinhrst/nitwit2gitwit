### 7: Local git advanced
- Understand commit refs
- Make branches 
- Merge
- (and remote repos are just branches)

(8: Github and integrations)
---

### Commit ref(erenece)s

- Sha (e.g. `4353afc3`). Immutable
- Tag (e.g. `v1.0`). Can be moved
    - Human-friendly
    - gets given after commit
- Branch(name) (e.g. `main`)
    - Human friendly
    - Points to latest commit in branch (per definition)
    - Gets updated when extra commit is added to branch
- `HEAD`: currently checked out revision
- Relative (e.g. `HEAD^^^` or `4353afc3^`)
    - `^` means "the unique parent of
    - Note that some shells need you to escape `^`

vvvvvvv

- Commit-refs mean different things depending on command
  - The state of the code at that point
  - The changes between that commit and the parent
  - The changes between that commit and "last common ancestor"

Some commands take 1 commitref, some 2, some 0, 1 or 2 and a pathname.

_therefore best to avoid overlap between commitref and pathnames_


---

### How to think about git branch

- Like evolutionary tree
- A common ancestry (and last common ancestor); although it is possible to "invent life again" (LCA = "nothingness")
- Do some work that should not be in main branch (yet)
    - Some feature that you plan to merge in the future
    - Some experiment that needs you to change some code, which never gets merged
    - Different versions of the code:
        - For Mac / Linux / Windows
        - For public / private use
        - Released/next-release/development
        - ???

vvvvvvv

- Recombine:
    - `cherry-pick` for one _commit_ (horizontal gene transfer?)
    - `merge` for all _commits_
- Branches end-of-life:
  - Forever
  - Deleted (Pruned _at branch point_)
    - Orphaned commits
  - Merged (and then deleted)

---

### Branch names

- Default branch (`main` or `master` or `trunk`)
- Cannot contain space, but can contain `-`, `_` and `/` (don't use `/` at start)
- Example convention (but define your own):
    - `main`, `release` branches
    - `beta/FEATURENAME` branches for things that are tested and ready
    - `feat/USERNAME/FEATURENAME` for things that are in progress
- Short but descriptive names is a good idea
- Generally not a good idea to use file-names (in order to avoid confusion)

_For now, don't worry too much_

---

### Git branches cheat sheet

|command|description|
|---|---|
|`git checkout COMMITREF`|Checkout an existing commitref (can be branch)
|`git checkout -b BRANCH`|Create a new branch BRANCH and check it out
|`git branch`|List all (local) branches
|`git branch --all`|List all branches (local and remote)
|`git branch --delete BRANCH`|Delete branch BRANCH _if it's all merged_
|`git branch --delete --force BRANCH`|Delete branch BRANCH _even if not fully merged_
|`git branch -d BRANCH`|Shortcut for `git branch --delete BRANCH`
|`git branch -D BRANCH`|`git branch --delete --force BRANCH`|

---

### Merging


<pre class="mermaid">
gitGraph
    commit id: "1"
    branch A
    checkout main
    commit id: "M1"
    commit id: "M2"
    checkout A
    commit id: "A1"
    commit id: "A2"
    checkout main
    commit id: "M3"
</pre>

- When you merge branch _A_ into branch _main_ it means:
  - At the end,  _main_ should have all the changes in branch _A_ (in addition to what it already had)
- Different methods:
  - (manually -- no git;  sometimes if change is simple (or super complex))
  - merge-commit
  - rebase / fast-forward
  - squash


vvvvvvv

- Branches in git are _everywhere_ so merging is too
  - local branches
  - remote repositories
  - forking
  - pull requests

- Branching is super easy.
- Merging is easy-ish (most of the time)
- Merge conflicts are where the complexity is

A merge-conflict happens when changes somehow overlap 


vvvvvvv

#### manual

<pre class="mermaid">
gitGraph
    commit id: "1"
    branch A
    checkout main
    commit id: "M1"
    commit id: "M2"
    checkout A
    commit id: "A1"
    commit id: "A2"
    checkout main
    commit id: "M3"
</pre>


<pre class="mermaid">
gitGraph
    commit id: "1"
    commit id: "M1"
    commit id: "M2"
    commit id: "M3"
    commit id: "A1&2 manually"
</pre>

In some complex merge situations, manual merge is the only (practical) solution

vvvvvvv


#### merge-commit

<pre class="mermaid">
gitGraph
    commit id: "1"
    branch A
    checkout main
    commit id: "M1"
    commit id: "M2"
    checkout A
    commit id: "A1"
    commit id: "A2"
    checkout main
    commit id: "M3"
</pre>


<pre class="mermaid">
gitGraph
    commit id: "1"
    branch A
    checkout main
    commit id: "M1"
    commit id: "M2"
    checkout A
    commit id: "A1"
    commit id: "A2"
    checkout main
    commit id: "M3"
    merge A tag:"merge-commit"
</pre>

A merge-commit has 2 (or more) parents, and may contain extra "diffs" to indicate how to resolve merge-conflicts.

vvvvvvv

#### Rebase / fast-forward

<pre class="mermaid">
gitGraph
    commit id: "1"
    branch A
    checkout main
    commit id: "M1"
    commit id: "M2"
    checkout A
    commit id: "A1"
    commit id: "A2"
    checkout main
    commit id: "M3"
</pre>

In rebase (we rebase _A_ to _main_) we first move the base (LCA) of branch _A_ to the tip of _main_ (note that `A1` and `A2` will need to change (at least their parent). Note that "committer" or "commit date" are **not** changed.

<pre class="mermaid">
gitGraph
    commit id: "1"
    checkout main
    commit id: "M1"
    commit id: "M2"
    commit id: "M3"
    branch A
    commit id: "A1*"
    commit id: "A2*"
</pre>

Then we "fast-forward" _main_ (basically no commits are changed, just the _main_ label is moved).

<pre class="mermaid">
gitGraph
    commit id: "1"
    commit id: "M1"
    commit id: "M2"
    commit id: "M3"
    commit id: "A1*"
    commit id: "A2*"
</pre>

vvvvvvv

#### squash-merge

<pre class="mermaid">
gitGraph
    commit id: "1"
    branch A
    checkout main
    commit id: "M1"
    commit id: "M2"
    checkout A
    commit id: "A1"
    commit id: "A2"
    checkout main
    commit id: "M3"
</pre>

Squash

<pre class="mermaid">
gitGraph
    commit id: "1"
    branch A
    checkout main
    commit id: "M1"
    commit id: "M2"
    checkout A
    commit id: "A1&2"
    checkout main
    commit id: "M3"
</pre>

(continued on next slide...)

vvvvvvv

Rebase

<pre class="mermaid">
gitGraph
    commit id: "1"
    checkout main
    commit id: "M1"
    commit id: "M2"
    commit id: "M3"
    branch A
    commit id: "A1&2*"
</pre>

Now just fast-forward

<pre class="mermaid">
gitGraph
    commit id: "1"
    commit id: "M1"
    commit id: "M2"
    commit id: "M3"
    commit id: "A1&2*"
</pre>

vvvvvvv

#### Notes about merges

- In the diagrams we pretend the branch disappears after merge; this is a manual operation (and not always what you want)
- Git merge always tries to do it's best to not create conflicts, but if it does, you will have to manually fix them
- Rebase may result in rebase conflicts (which are more or less the same)
- avoid conflicts by not checking in more than you want (remember `git diff --cached` before commit)!!!!

Differences in strategies

|     |mergecommit|rebase/ff|squash|manual|
|-----|-----------|---------|------|---|
|nr commits in _main_| 1 (merge) | multiple | 1 (squashed) | 1 (manual)
|_main_ is in chronological order | yes | no | ??? | ???
|history | split (complex) | straight | straight | straight
|original commits available | yes | yes | no | no
|original blame available | yes | yes | no | no 
|branch visible in history | yes | no | no | no
|branch is rewriten| no | yes | yes | ???

---

### Git merge cheat sheet

|command|description|
|---|---|
|`git cherry-pick COMMITREF`|Apply the _diff_ pointed to by COMMITREF to the current branch.<br>`cherry-pick` may pause if not clean
|`git merge BRANCH`|Starts merging BRANCH into current branch.<br>`merge` may pause if not clean.
|`git merge --abort`|Abort a pause merged
|`git merge --continue`|Continue a paused merge after manually resolving conlicts

---

### Branches and remote git

```
git add remote origin git@github.com:reinhrst/nitwit2gitwit`
git push --set-upstream origin branch
```

- This creates a branch `remotes/origin/main` which is meant to reflect `main` branch on GitHub
- For the following commands, we assume we're in `main`
- `git fetch` means "update `remotes/origin/main` to match remote `main` branch

vvvvvvv

- `git pull` means `git fetch main && git merge remotes/origin/main`
  - Until you make an explicit choice, it will ask you for a merge strategy
  - I think "rebase" is the cleanest (but [discussion](https://stackoverflow.com/questions/2472254/when-should-i-use-git-pull-rebase)).
  - Be prepared that you may get merge (rebase) conflicts if you have local commits or local working directory changes
  - Avoid too many conflicts by pushing regularly (as soon as your commits are in GitHub, conflicts are not _your_ problem anymore)
- As long as all changes are made in 1 remote (1 person / 1 computer) you should not have merges / rebases / conflicts.

vvvvvvv

- `git push` means:
  - check if `remotes/origin/main` is up to date with GitHub `main`
  - check if local `main` has `remotes/origin/main` as parent (i.e. local `main` is `remotes/origin/main`  with one or more commits)
  - if not:
    - break off `push` and tell user to pull first
  - else:
    - send new commits to GitHub and "fast-forward" GitHub `main` and `remotes/origin/main` to local `main`
- `git push` can _never_ lead to conflicts, since it doesn't try to merge or rebase (only fast-forward)
- GitHub `main` can only gain more commits, it can never loose a commit or change a commit
  - unless you force-push, but you shouldn't unless you know what you're doing!

### Take-aways last week

- Hashing creates a small number/string from any size of information that (faiap) uniquely identifies this information
- Any change in original data will result in a completely different hash
- Humans should easily be able to compare hashes (in hex format)
- `git` uses _sha_-hashes as its revision "numbers". The same sha → the same commit, the same revision, the same code
- Do `git` every day!

vvvvvv

If you compare two hashes and first X hex-digits match, how large is the change that the underlying data is different:

| X | p |
|---|---|
| 1 | $\approx0.06$  |
| 2 | $\approx0.004$  |
| 4 | $\approx0.000015\approx10^{-5}$  |
| 7 | $\approx0.0000000037\approx10^{-9}$  |
| 40 | $\approx0.00000000000000000000000000000000000000000000000068\approx10^{-48}$  |

---

# Lesson 5

- Take a breath
- Much more about local git

---

### Git for Windows

- Not a full Linux for windows
- Other solutions, such as WSL

---
### How to build a (local) VCS using diff and patch

```none
/
- .vcs/
  - commits/
    - 1/
      - message.txt
      - parents.txt (=none)
      - diffs/
        - raven.txt.patch
        - dove.txt.patch
    - 2/
      - message.txt
      - parents.txt (=1)
      - diffs/
        - raven.txt.patch
    - 3/
      - message.txt
      - parents.txt (=2)
      - diffs/
        - sparrow.txt.patch
        - dove.txt.patch
  - branches/
    - main.txt (=3)
  - tags/
    - v1.0.txt (=2)
  - HEAD.txt (=3)
  - CURRENT_BRANCH.txt (=main)
- dove.txt
- sparrow.txt
- raven.txt
```

<!-- .element: class="fragment" data-fragment-index="1" -->

Example VCS system **(not git)** with 3 revisions, and revision 3 checked out.

<!-- .element: class="fragment" data-fragment-index="1" -->

---

### Local git

- Exercises will only take you that far; you _really_ learn when you work with it.
- **Take the pain**
    - Two hours per week is not enough
    - You will run into problems _before_ you learn the solution

---

### How to choose what is one repository?

- One "project"
- Belongs together (one cannot work without the other)
- Same people working on it
- In the end: many opinions, just choose something
- You should have between 2 and 5 repos you use regularly

---

### What projects make sense to use a (text-based) VCS for?

We discussed the _idea_ of non-text based diffs (e.g. image diffs), but in practice `git` is text-based.

- >99% of people use `git` with normal (text-based) diff tools
- So `git` makes sense mostly for text-based formats
- Code is obvious example
- However other uses (markdown, csv, html, svg)

You will likely never need it, but it _is_ possible to use other `diff`/`patch` with `git`. e.g. `images`, `xlsx`, `csv`, `pdf`, Jupyter Notebook.

---

### What files are part of your git repository, and which are not?

- Everything that you created (code, images, graphs)
- Readme files / documentation / instructions (ideally in Markdown)
- Ideally use text-based formats

vvvvvv

##### But not:
- Raw data (usually; you can have a "data repo")
- Derivative (by script) stuff -- _Single source of truth_
- Huge files (esp if they change a lot)
- Binary files that change a lot (e.g. Word documents or zip files)
- Commented out / not used code (make branch!)
- Code that is in another repo
- Development files for your environment
- PASSWORDS / SECRETS (remember that all history is normally kept!)

vvvvvv

- Generally I would advice against files > 1MB
- GitHub will get upset with files > 50MB (and refuse >100MB)
- Remember files will always be in history (unless you rewrite)
- There is something called Git Large File Storage (LFS).

vvvvvv

_There are always exceptions to this rule, in time you'll find out what works for you. However have rules within one repo!_

---

### Open vs closed source and license

The first thing you have to choose when making a new repo in GitHub is whether it's public or private

- public: the whole world can see it: open source
- Note that there is a difference between "open source" and "anything can use/copy this"
Tempting to make everything private, but nicer to make things public. Also people interested in you may check out your code / find your code through Google

If you make something public later, be aware that all history will also become public!


vvvvvv

- A license (typically in LICENSE.TXT, or LICENSE.MD) is a legally binding agreement of what can be done with the code:
  - Everything, no restrictions: MIT, CC0
  - Only in other Open Source projects: GPL
  - Create Commons:
    - CC0: Public domain
    - BY: credit must be given to the author
    - SA: Adaptations must be shared under the same terms
    - NC: Only non-commercial use
    - ND: No derivates are allowed
- Note that others might have opinions on public/private and the license: journals, universities, etc

---

### Git is not a backup (but GitHub may be)

- Editing something in the working directory does nothing with git
- When you add something to the index, it can be retrieved from the repo if deleted
- When something is committed, it can be retrieved from the repo (as long as it's a parent of some branch)
- However remember: the repo is only a local directory; only when you push to someone else (or GitHub), or backup your directory (to external HD / Dropbox / email to yourself).


- Really _really_ important stuff need online and offline backups.

---

### How often should one commit their code

It's a personal preference / agree on rules per project or repo / you will get a feeling for what works for you _(for now: often to get experience)_

vvvvvv

##### My suggestion:
- When you finish something
- When you start working on something else
- At least every couple of hours (lunchtime, before end of day?)
- It does not have to work (although commit it as soon as it works), but note in commit message
- Remember: semantic changes
- Completely ok to have single-char commits, or 50-page commits
- When it gets too large to lose
- When you start to change / rewrite lots of code

If your code is not ready yet, just make a commit in a branch!

NB: you push to GitHub after every commit!

---

### Extra: when do you make a branch

_branches are cheap_

NOTE: This is a preview, we will deep-dive into branches soon

vvvvvv

- When working on something that you don't quite want to share yet in the `main` branch (or is not ready)
- When you start a large "operation", that may take a couple of days (or: a couple of commits) and:
    - you don't want to disturb other repository users until it's done
    - you may at some point (while doing the operation) need access to the previous, working, code
    - you are not sure that it's a good idea what you're doing, and only want to make it part of the main codebase when you're sure it works
- When you want to experiment / test something
- When you need to make changes to an older version (e.g. someone reports a bug to a certain version).

Note: just working in `main` and not pushing is **NOT** how to do it (although technically you have a branch now).

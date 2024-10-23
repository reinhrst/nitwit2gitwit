### Size of things

<pre><code data-trim data-noescape data-line-numbers="2|1-2|2-5|2-3,6-9|2,10-11|" data-fragment-index="2">
Base16:▕ 1 ▕ c ▕ 6 ▕ 1 ▕ 7 ▕ a ▕ 0 ▕ f ▕ c ▕ 0 ▕ 1 ▕ c ▕ 0 ▕ 8 ▕ 9 ▕ 6 ▕
Memory: 0001110001100001011110100000111111000000000111000000100001100000
Bytes: ▕       ▕       ▕       ▕       ▕       ▕       ▕       ▕       ▕
Bytes:    (28)    (61)   (122)    (15)    (192)   (28)    (8)     (96)
Bytes:   (0x1c)  (0x61)  (0x7a) (0x0f)   (0xc0)  (0x1c) (0x08)   (0x60)
Ascii:    {FS}     =      z      {SI}     {?}     {FS}    {BS}     `
Ascii:          ".=z....`"
Latin_1:        ".=z.À..`"
Latin_2:        ".=z.Ŕ..`"
Hex:          0x1c617a0fc01c0860    (or 0x1C617A0FC01C0860)
Decimal:               2045049913869076576</code></pre>

- 64 bits (base 2)
- 16 nibbles (base 16) <!-- .element: class="fragment" data-fragment-index="2" -->
- 8 bytes (base 256) <!-- .element: class="fragment" data-fragment-index="3"  -->
- 8 characters (BUT: only in "old" encodings) <!-- .element: class="fragment" data-fragment-index="4"  -->
- hex-number of length 16 (without 0x!) (decimal nr of length 19) <!-- .element: class="fragment" data-fragment-index="5"  -->

<span markdown="1" class="fragment" data-fragment-index="6">Normally length is in bits or bytes. Therefore a if the hash is `0x1c617a0fc01c0860`, it's of length _8 bytes_, or _64 bits_.</span>

---

### Lesson 4

- Version control systems
- Git (local)

---

### Version Control System (VCS) / Source Code Management (SCM)

- Simple numbers for "(development) versions"
- Go back and forward between versions (e.g. if someone reports a bug, or if you knew it used to work last week)
- See the evolution of a file (incl who and commit message)
- Allow multiple people to work on a project
- Using patch-files to save space
- (branches)

vvvvvv

History:

- Have been around forever
- Mostly centralised (lock files -- disadvantages)
- In 2005 `git` was developed as decentralised (+local) VCS, for the linux kernel

---

### Content, change, semantic change

| Ver | Content                  | Change           | Sem Changes            |
| --- | ------------------------ | ---------------- | ---------------------- |
| 1   | We are going to Bergen   | \*\*             | new plan               |
| 2   | We are flying to Bergen  | going -> flying  | Go by airplane         |
| 3   | We are flying to Gdansk  | Bergen -> Gdansk | Go to Gdansk after all |
| 4   | You are flying to Gdansk | We -> You        | Actually I'm not going |

---

### VCS basics

<pre class="mermaid">
sequenceDiagram
	VCS->>working directory: checkout
    working directory->>editor: load file(s)
    editor->>working directory: save file(s)
	working directory->>VCS: commit
</pre>

You never edit files directly in the VCS. You always get files from the VCS into your local directory (`checkout`). There you edit the files, and then send the changes back to the CVS (`commit)`.

---

### VCS (git) terms

| term              | def                                                                            |
| ----------------- | ------------------------------------------------------------------------------ |
| respository       | the git database you work on; usually 1 project                                |
| revision          | development version                                                            |
| `checkout`        | Bring the working directory in line with certain revision                      |
| local&nbsp;change | `diff` between latest checked-out version and version in working directory     |
| `commit`          | Make a new revision (of currently checked-out revision + local changes)        |
| a commit          | the changes between two subsequent revisions                                   |
| commit msg        | Log-message for your commit, **not** part of the code                          |
| parent            | if at revision A, the parent is that revision that came just before revision A |
| id/sha            | a "number" for your commit / revision                                          |
|                   |                                                                                |
| a branch          | If multiple revisions with the same parent, they start a branch                |
| `merge`           | Combine all commits in two branches, to create a new revision (with 2 parents) |
|                   |                                                                                |
| `fetch`           | get new revisions from "remote location"                                       |
| `pull`            | `fetch` + `merge`                                                                |
| `push`            | push new commits to "remote location"                                          |

---

### Examples with git terms

| id/sha                                                         | revision                                                                                 | a commit                                                                    | commit message                                                                         |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
|                                                                | **Main**                                                                                 |                                                                             |                                                                                        |
| 1                                                              | We are going to Bergen                                                                   | \*\*                                                                        | new plan                                                                               |
| 1-2                                                            | We are flying to Bergen                                                                  | going -> flying                                                             | Go by airplane                                                                         |
| 1-3                                                            | We are flying to Gdansk                                                                  | Bergen -> Gdansk                                                            | Go to Gdansk after all                                                                 |
| 1-4                                                            | You are flying to Gdansk                                                                 | We -> You                                                                   | Actually I'm not going                                                                 |
|                                                                | **branch: past (from rev 1)**<!-- .element: class="fragment" data-fragment-index="1" --> |                                                                             |                                                                                        |
| 2-2<!-- .element: class="fragment" data-fragment-index="1" --> | We were going to Bergen<!-- .element: class="fragment" data-fragment-index="1" -->       | are -> were<!-- .element: class="fragment" data-fragment-index="1" -->      | Story is better in the past<!-- .element: class="fragment" data-fragment-index="1" --> |
|                                                                | **Merged (in main)**<!-- .element: class="fragment" data-fragment-index="2" -->          |                                                                             |                                                                                        |
| M-2<!-- .element: class="fragment" data-fragment-index="2" --> | You were flying to Gdansk<!-- .element: class="fragment" data-fragment-index="2" -->     | Merge 1-4 & 2-2 <!-- .element: class="fragment" data-fragment-index="2" --> | _\*All changes\*_<!-- .element: class="fragment" data-fragment-index="2" -->           |

---

### The same, in a git diagram

<pre class="mermaid">
gitGraph
    checkout main
    commit id: "1"
    branch past
    checkout main
    commit id: "1-2"
    commit id: "1-3"
    checkout past
    commit id: "2-2"
    checkout main
    commit id: "1-4"
    merge past id: "1-4 & 2-2"
</pre>

NB: "time" is always from left to right (or top to bottom)

- "Main" branch in `main` (or `master`)
- From the initial commit `1` a branch `past` is made, to work on a version of the story in the past tense
- In the main branch, `commit`s `1-2` and `1-3` are made
- In the past branch, `commit` `2-2` is made
- In the main branch, `commit` `1-4` is made
- It's decided that the `past` branch should be merged (all changes from this branch should be pulled in) into `main`.

Note: how to choose a branch name?

---

### Local git

_It's essential to understand git local mode before moving on to non-local._

It's essential to (sort of) understand git non-local mode
before moving to GitHub.

For now, forget about `pull`, `fetch` and `push`

Many devs (incl myself) have local gits on Dropbox for backup (less these days)

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

vvvvvv

- `commit`:
  - Create a new subdirectory under `commits`
  - create patch files to show difference between `HEAD` and working directory
  - create `message.txt` (based on message from user) and `parents.txt`
  - change `HEAD.txt` to point to new commit
  - change the file `branches/#CURRENT_BRANCH.txt#.txt` (so `branches/main.txt`) to point to new commit
- Sequential version numbers a bad idea. What if we use the _hash_ of (`message.txt` + `parents.txt` + `diffs/*`)? That is _almost exactly_ what `git` does.
- When `vcs checkout 2`, we just apply diffs for commits `1` and `2` and have version `2`

---

### How is git different

- uses `.git` directory
- not one directory per commit (also lots of optimisations)
- use `sha` as commit/revision number
- allows for more complex branching / merging

<pre class="mermaid">
gitGraph
    commit id: "d025a921"
    commit id: "2ad61971"
    commit id: "4ff7dd4e"
    commit id: "6760bd27"
    branch reveal.js
    checkout reveal.js
    commit id: "62b927b8"
    branch typos
    commit id: "91347842"
    commit id: "10031726"
    commit id: "c881ce59"
    checkout main
    merge typos
    commit id: "56ac0a73"
    checkout reveal.js
    commit id: "2b494976"
    commit id: "a8420eba"
    checkout main
    commit id: "f42f95c9"
    branch crazy-idea
    checkout crazy-idea
    commit id: "541d5c05"
    commit id: "e573f21b"
    checkout main
    commit id: "ba88d9ef"
    commit id: "aa1b0e8f"
    checkout reveal.js
    commit id: "d2659292"
    branch mermaid-plugin
    checkout mermaid-plugin
    commit id: "34418e7d"
    checkout main
    merge reveal.js
    checkout mermaid-plugin
    commit id: "282a1b9b"
    checkout main
    commit id: "9e5caa28"
    merge mermaid-plugin
    commit id: "f1a8a41b"
    commit id: "b8df9f45"
    checkout crazy-idea
    commit id: "8db12eed"
</pre>

---

### How to think about git

- Git is a tree/subway map, where each "station" is a _revision_ (a "version" of the code).
- Between any two revisions there is a _diff_; a diff between two connected stations is a _commit_.

- Each station has a name which we call a _sha_ (SHA = Secure Hash Algorithm).
  The sha is roughly (or: can be thought of as):

```
hash(parent + diff + commit_name + commit_message + commit_datetime)
```

- The sha is 20 bytes long (written as 40 hex-digits), but usually we only show the first 7 hex-digits (e.g. `8db12ee`); Larger projects need more.

vvvvvv

- A _tag_ is a unique (semantic) label that points to a sha. It can be chosen by the user, and can be moved. Typ: version number

- A _branch_ (act. branch-tag) is like a tag; it points to the latest sha on a branch (and moves when a new commit is made to the branch).

<pre class="mermaid">
%%{init: {"useMaxWidth": true}}%%
gitGraph
    commit id: "d025a921"
    commit id: "2ad61971"
    commit id: "4ff7dd4e" tag: "v0.1"
    commit id: "6760bd27"
    commit id: "f42f95c9" tag: "v0.2"
    commit id: "541d5c05"
    commit id: "ba88d9ef"
    commit id: "aa1b0e8f" tag: "main" 
</pre>

<pre class="mermaid">
%%{init: {"useMaxWidth": true}}%%
gitGraph
    commit id: "d025a921"
    commit id: "2ad61971"
    commit id: "4ff7dd4e" tag: "v0.1"
    commit id: "6760bd27"
    commit id: "f42f95c9" tag: "v0.2"
    commit id: "541d5c05"
    commit id: "ba88d9ef"
    commit id: "aa1b0e8f"
    commit id: "c881ce59"
    commit id: "56ac0a73" tag: "main" 
</pre>

<pre class="mermaid">
%%{init: {"useMaxWidth": true}}%%
gitGraph
    commit id: "d025a921"
    commit id: "2ad61971"
    commit id: "4ff7dd4e" tag: "v0.1"
    commit id: "6760bd27"
    commit id: "f42f95c9" tag: "v0.2"
    commit id: "541d5c05"
    commit id: "ba88d9ef"
    commit id: "aa1b0e8f"
    commit id: "c881ce59"
    commit id: "56ac0a73"
    commit id: "22339b36" tag: "v0.3"
    commit id: "b0944c21"
    commit id: "cbd67e23" tag: "main" 
</pre>

---

### Explain index

With `commit` you move changes from your working directory to git. But which changes?

To solve this problem, committing is a two-stage operation.

First you _stage_ changes into the _index_

Then when you're ready, you `commit` the index

The _index_ is therefore a subset of the changes between latest checked out version, and your working directory.

---

### (local) git cheat sheet

```
git subcommand subcommand-options -- general way to interact with git
git help -- show all subcommands
git help subcommand -- show help for certain subcommand
```

| subcommand | action                                                                        |
| ---------- | ----------------------------------------------------------------------------- |
| `status`   | Shows what files differ between "current revision"                            |
|            |                                                                               |
| `init`     | Start a new (empty) git respository in the current directory                  |
| `checkout` | Make a certain revision the "current revision" and apply to working directory |
| `add`      | Move changes into the index                                                   |
| `reset`    | Move changes out of the index (although there are other ways)                 |
| `commit`   | Commit the (changes in the) index into the respository (as a new commit)      |
| `diff`     | Run a `diff` between different commits, or a commit and your local files      |
| `log`      | See a list, starting at the current commit and showing all parents            |

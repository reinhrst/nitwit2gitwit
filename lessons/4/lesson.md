## Catchup of last week

- I will sometimes drill down a bit deep, in the hope that the shallow parts stick
- Important about number systems:
  - There are different systems
  - Everything in a computer is binary, which means powers-of-two make sense
  - Hex(adecimal) system used a lot; `0x...` or just numbers and `abcdef`/`ABCDEF` combined
- Using `|`, one can pipe from one command to another
- Windows users are cursed with line endings
- `diff` generates a diff-file between two files, `patch` applies that diff-file

---

# Lesson 4

- Crypto and hash
- Local git

---

## Cryptography

<pre class="mermaid">
  %%{init: {'theme': 'neutral', 'look': 'handDrawn'}}%%
  flowchart LR
    A[Message] -->|encrypt| B[Encrypted message]
    B -->|decrypt| C[Original Message]
</pre>

(Ultimate) design goal for Cryptography

- Nobody but sender and recipient will know message content

vvvvvv

Additional goals:

- Recipient knows that message is from sender and has not been tampered with
- Recipient knows whether it has missed earlier messages
- ...

(Quantum Cryptography: guarantee that only one party has received message)

vvvvvv

Encryption (encoding) and decryption (decoding) happens with _keys_.

- Symmetric encryption (shared secret): same key for encoding and decoding (like house keys)
- Asymmetric encryption: different keys for encoding and decoding

Only 100% secure (non-quantum) encryption: truly random one-time pads (iff pads themselves are not compromised).

In practice: pseudo-random keys, lots of maths trying to make things as safe as possible.

_Breaking this code will take 100 times the age of the universe\*\*\*_

Cryptography is a field in itself (within mathematics)

---

## Symmetric encryption

Like a safe with a limited number of keys (typically: two).
When you open the safe and it contains a message that is not from you, it _has to be put in there_ by the other key owner.

Problem:

- You will need a unique key for every single person you communicate with.
- How do you get that key to that person?
- Digital keys are much easier to copy than real ones. Even if you know that you kept your key safe, there is no way to know if the other key is safe.


---

## Asymmetric encryption

Used in two ways:

- Like a display-board behind two locks. One key to read the board, one key to change the message.
- Like a safe with a letterbox with a separate lock. One key opens the safe and allows to read the messages inside, the other key opens the letterbox and allows to post a letter.

In practice (often):

- You have a private key (which you keep private) and a public key (which you make public; e.g. put on your website); a _key pair_.
- Anyone with the public key can encrypt a message that only the private key (=you) can decrypt
- The private key (= you) can encrypt a message that only the public key can decrypt (what is the use of this?)
- Using two keypairs, encryption and authentication can be achieved

vvvvvv

Asymmetric encryption (non)problems:

- Every person only needs a single key pair no matter how many persons they communicate with
- Only you have your private key, so only you are responsible for keeping it private.
- Public keys of people are freely available to download
- However, only works if you are sure that the public key you use belongs to the person/system you want to talk to.

Public Key Infrastructure (PKI) helps a bit:

- Keys are _signed_ with other keys
- Always gets back to some key you need to trust

---

## Hashing

"A hash function is any function that can be used to map data of arbitrary size to fixed-size values" (wikipedia)

```madeup
f(byte[16]) -> byte[16]
f(byte[32]) -> byte[16]
f(byte[1000]) -> byte[16]
f(byte[0xffffffff]) -> byte[16]
f(byte[1]) -> byte[16]
f(byte[0]) -> byte[16]
```

Note: if we are to hash 4GB into 16 bytes, we _obviously_ loose data; so a "reverse hash function" doesn't exist (unless input is a limited list)

Some examples (to use on The Raven)?

<!--
- Always 0000000
- Always some random number
- First 16 characters
- Smarter: pos 1 is number of a's, pos 2 = number of b's, etc
-->

vvvvvv

A hashing function takes (an arbitrary number of, incl 0) _bytes_ as input and returns (a predefined number of) _bytes_ as output.

A file on the computer (and any data in memory) are just bytes, so you can hash anything on your computer:

- a text (or a text file)
- source code
- `.docx` word document
- `.pdf` file
- video file
- program

You can also hash multiple files (with some tricks) into a single hash.

vvvvvv

In practice a "good" hash function:

- Small change in input leads to complete change of output
- Cannot change input to get desired output
- (Not reversible)

_If_ you choose the right function:

- Quickly (few bytes) compare if two things are the same
- Check if things are the same over slow connections
- Humans can compare if two things are the same
- Humans can check if something is what they think it is
- Digital signatures
- Check keys
- "Show that you know something without revealing it"
- Put in buckets in determined way

vvvvvv

Some examples: CRC-32, MD5, SHA1, SHA2, SHA3, SHA256, SHA512

These hash functions are open source and determinate; every (correct) implementation has the same output for the same input

Secure hashing is a field in itself (within mathematics; NIST)

For "practical (non security) use", you can take any of these and assume the following:

- Two different inputs will result in two different outputs (**but** birthday problem)
- (You can pick the first X bytes and assume it to be as good a hash function with that size)

Take away: a hash is a "proxy" that points to (one unique; or more) item. Git uses hashing (SHA) extensively

<!-- some examples of birthday problem:
If you have X possible values, and Y "random" values, how large is the chance of a collision.
E.g: 4 bytes (32 bits, 4B possibilities, after 9300 values you have a 1% possibility of a match.

16 bytes (128 bits) has even with 26B values a 0.0000000000000001% chance of collision (10^-18)
-->

vvvvvv

### Size of a hash

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

<span markdown="1" class="fragment" data-fragment-index="6">Normally length is in bits or bytes. Therefore a if the hash is `0x1c 61 7a 0f c0 1c 08 60`, it's of length _8 bytes_, or _64 bits_.</span>

vvvvvv

# Signatures

Hashing + encryption can be used to create digital signatures:

- Create a hash of the document you want to sign + extra info (who signs it, date-time, location)
- Encrypt this hash with the person's private key, and attach this to the document (as some metadata).
- Anyone opening the document can just read it; if they want to check your signature, they calculate the same hash on the document (carefully stripping out your signature first), and then compare it to decrypting the signature with your public key.
- This way a signature only adds a couple of bytes to a document's length
- This is why it's important that it's infeasible to find collisions in the used hash function.

---

## Playtime

- Use the `md5sum` program to calculate MD5 hash of different Raven versions.
- Calculate md5 hash of `hello world`
- Calculate md5 hash of `hello world` again
- Calculate md5 hash of `hello world1`
- Calculate md5 hash of `hello world2`
- Calculate sha256 of `hello world`
- Calculate sha512 of `hello world`
- How big is an md5 hash? How big a sha256 hash? And the sha512 hash?
- Advanced: did we _actually_ calculate the md5 of "hello world"?

---

### Version Control System (VCS) / Source Code Management (SCM)

- Simple numbers for "(development) versions"
- Go back and forward between versions (e.g. if someone reports a bug, or if you knew it used to work last week)
- See the evolution of a file (incl who and commit message)
- Allow multiple people to work on a project
- Using patch-files to save space
- Branches

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

<pre class="mermaid" id="vcs-diagram">
sequenceDiagram
	VCS->>working directory: checkout
    working directory->>editor: load file(s)
    editor->>working directory: save file(s)
	working directory->>VCS: commit
</pre>

You never edit files directly in the VCS. You always get files from the VCS into your local directory (`checkout`). There you edit the files, and then send the changes back to the CVS (`commit)`.

---

#### VCS (git) terms

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
| id/_sha_            | a "number" for your commit / revision                                          |
|                   |                                                                                |
| a _tag_          | A manually placed (but movable) label to a revision. E.g. a concrete version.                  |
| a _branch_          | All commits from the root to a named branch-tip (like tag but moves on commit)  |
| `merge`           | Combine all commits in two branches, to create a new revision (with 2 parents) |
|                   |                                                                                |
| `fetch`           | get new revisions + tags + branch-tips from "remote location"                                       |
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

vvvvvv

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


- "Main" branch is `main` (or `master`)
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
- Between any two revisions there is a _diff_
- A _commit_ is a "commit package" of (parents + diffs + commit message + committer name & email + commit date-time)
- Often _commit_ and _revision_ are used interchangeably. This means that both may point at a version of the code, and a commit package
- Each station has a name which we call a _sha_ (SHA = Secure Hash Algorithm).
  The sha is roughly a hash over the commit package
- The sha is 20 bytes long (written as 40 hex-digits), but usually we only show the first 7 hex-digits (e.g. `8db12ee`); Larger projects need more.
- If two commits have the same sha, they are the exact same commit package (barring the Birthday Problem; but you need $>10^{15}$ commits to have a 1-in-a-billion chance of collision)
- Therefore if two _revisions_ have the same _sha_ its the same revision (→ the same code)

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

vvvvvv

<pre class="mermaid" id="index-diagram">
sequenceDiagram
    current revision-)index: git checkout
    index->>working directory: git checkout
    working directory->>index: git add
    index->>current revision: commit (makes new revision)
</pre>

---

### Extra: set up git editor

When you commit something, `git` will ask for a commit message.
In order to do so, `git` will open an editor.

By default this editor is `vim`, the one and only absolute best editor in the world, but with a quite steep learning curve.

So we will need to switch this for `nano`.

vvvvvv

First, confirm that `nano` is installed on your system: `nano somefile.txt`.
It should open an editor and allow you to edit and then save a file.

If not, do `brew install nano` (on Mac).

Now, we need to make sure `git` uses `nano` instead of `vim`:

vvvvvv

- `git config list` shows the current git configuration.
- `git config list | grep editor` shows if there is anything about an editor
- `git config core.editor nano` sets the editor (check with the command above)

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

---

## Discussion

- How to choose what is one repository?
- What projects make sense to use a text-based VCS for?
- What files are part of your git repository, and which are not?
- Should your repo be open or closed source?


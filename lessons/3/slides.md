---
marp: true
paginate: true
---

# Discuss feedback

- Terminal/shell very powerful tool
- However (almost) never the fastest the first time around

*However (almost) always the fastest once you are an expert*

- For now I will focus on git & github; later (if wanted) we can go more into shell programming
- Same (obviously) for other subjects
- If there is a useful task *now*, I can probably create something
(although terminal not always the best for everything).

---

# Lesson 3

- Crypto and hash
- Version Control Systems
- Local git

---

# Cryptography

Message ---(*encrypt*)--> encrypted message ---(*decrypt*)--> orginal message

(Ultimate) design goal for Cryptography

- Nobody but sender and recipient will know message content

Additional goals:

- Recipient knows that message is from sender and has not been tampered with
- Recipient knows whether it has missed earlier messages
- ...

(Quantum Cryptography: guarantee that only one party has received message)

Cryptography is a field in itself (within mathematics)

---

# Cryptography 2

Symmetric key (shared secret): same key for encoding and decoding
Asymmetric key (public key): independent key for encoding and decoding

Initial key sharing is problematic: PKI (central) / key sharing sessions (decentral)

Only (best case) guarantee: someone with certain key (key security is important)

*Always as strong as the weakest link*

Examples: RSA / elliptic curve

---

# Hashing

"A hash function is any function that can be used to map data of arbitrary size to fixed-size values" (wikipedia)

```madeup
f(byte[16]) -> byte[16]
f(byte[32]) -> byte[16]
f(byte[1000]) -> byte[16]
f(byte[0xffffffff]) -> byte[16]
f(byte[1]) -> byte[16]
f(byte[0]) -> byte[16]
```

Note: if we are to hash 4GB into 16 bytes, we *obviously* loose data; so a "reverse hash function" doesn't exist (unless input is a limited list)

Some examples (to use on The Raven)?

<!--
- Always 0000000
- Always some random number
- First 16 characters
- Smarter: pos 1 is number of a's, pos 2 = number of b's, etc
-->

---

# Hashing 2

*If* you choose the right function:

- Quickly (few bytes) compare if two things are the same
- Humans can compare if two things are the same
- Humans can check if something is what they think it is
- Digital signatures
- Check keys
- "Show that you know something without revealing it"
- Put in buckets in determined way

The right function:

- Not reversible
- Cannot change input to get desired output
- Small change in input leads to complete change of output

---

# Hashing 3

Examples; some better than others: CRC-32, MD5, SHA1, SHA2, SHA3, SHA256, SHA512

Secure hashing is a field in itself (within mathematics)

For "practical (non security) use", you can take any of these and assume the following:

- You can pick the first X bytes and assume it to be as good a hash function with that size)
- Two different inputs will result in two different outputs (**but** birthday problem)

Take away: a hash is a "proxy" that points to (one unique; or more) item. Git uses hashing (SHA) extensively

<!-- some examples of birthday problem:
If you have X possible values, and Y "random" values, how large is the chance of a collision.
E.g: 4 bytes (32 bits, 4B possibilities, after 9300 values you have a 1% possibility of a match.

16 bytes (128 bits) has even with 26B values a 0.0000000000000001% chance of collision (10^-18)
-->
---

# Playtime

- Use the `md5sum` program to calculate MD5 hash of different Raven versions.
How many bytes is the output?
- Calculate md5 hash of `hello world`
- Calculate md5 hash of `hello world` again
- Calculate md5 hash of `hello world1`
- Calculate md5 hash of `hello world2`
- Calculate sha1 of `hello world`

<!-- Note: we actually calculated md5 of `hello world\n`
What does output size mean for birthday paradox? -->

---

# Version Control System (VCS), Source Code Management (SCM)

- Simple(r) numbers for "(development) versions"
- Go back and forward between versions (e.g. if someone reports a bug, or if you knew it used to work last week)
- See the evolution of a file (incl who and commit message)
- Allow multiple people to work on a project
- Using patch-files to save space
- (branches)

History:

- Have been around forever
- Mostly centralised (lock files -- disadvantages)
- In 2005 `git` was developed as decentralised (+local) VCS, for the linux kernel

<!-- dev versions vs "Versions"; note that certainly also very useful for one-person projects! -->
---

# Git history

Early April 2005: Bitkeeper (commercial git-like software) removes free license for git kernal developers
3 April: development of Git began
6 April: project announced by Linus Torvalds,
7 April: Git (source code) uses git as version management system
18 April: First merge of branches
29 April: "performance goals met"
16 June: Linux Kernel 2.6.12 launched on git


---

# VCS terms

(based on `git`)

- "revision": development version
- `checkout`: Bring my working directory in line with certain revision
- "local changes": `diff` between latest checked-out version and version on disk
- `commit`: Make a new revision (of currently checked-out revision + (subset of) local changes)
- "a commit": the changes between two subsequent revisions (confusingly sometimes also called a revision)
- "commit message": Log-message for your commit, **not** part of the code
- `fetch`: get new revisions from "remote location"
- `pull`: `fetch` + magic
- `push`: push new commits to "remote location"

---

# Local git

**It's essential to understand git local mode**
before moving on to non-local.

It's essential to (sort of) understand git non-local mode
before moving to github.

For now, forget about `pull`, `fetch` and `push`

Many devs (incl myself) have local gits on Dropbox for backup (less these days)

<!-- Just as it's essential to understand `diff` and `patch` before going on to 
emailing patch files around  -->

---

# How to build a (local) VCS using diff and patch

<!--

- Need some way to say "this is a version (= commit)
- Version needs a number (sequential? or something else ?)
- When commit, we save diff
- When checkout certain version, we apply `patch` multiple times

-->
---

# How to build a (local) VCS

```madeup
/
- .vcs/
  - commit 1/
    - message.txt
    - diffs/
      - raven.txt.patch
      - dove.txt.patch
  - commit 2/
    - message.txt
    - diffs/
      - raven.txt.patch
  - commit 3/
    - message.txt
    - diffs/
      - sparrow.txt.patch
      - dove.txt.patch
- dove.txt
- sparrow.txt
- raven.txt
```

Example VCS system **(not git)** with 3 revisions, and revision 3 checked out.

---

# How is git different

- uses `.git` directory
- not one directory per commit (also lots of optimisations)
- use `sha` as commit/revision number

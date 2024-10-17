# Lesson 2

- Version Control System

---

## Version Control System

`git` is a Distributed Version Control System

- Version Control System
- Revision Control System
- Source Control System
- Source Code Management

https://git-scm.com/

---

## What is a DVCS

- A VCS keeps older versions of your files
- Like an "undo" button on steroids
  - Keep all history forever
  - History contains all files, any file types
  - Each change has a "note / comment"
  - See older versions and see changes between versions, without actually "undoing"
  - Undo one specific change
  - Trees of changes
- And then all of this distributed, multi-user.

Caveat: you have to manually create the undo-steps.

---

## In practice

- Let's make it visual
- Once you have tasted the power, you never want to go back

vvvvvv

## start

![v1](2/v1.webp)

v1

vvvvvv

## add man

![v2](2/v2.webp)

v2

vvvvvv

## add cat

![v3](2/v3.webp)

v3

vvvvvv

## add faces on man and cat

![v4](2/v4.webp)

v4

vvvvvv

## add piano on string

![v5](2/v5.webp)

v5

vvvvvv

## Make piano on string obey the laws of physics

![v6](2/v6.webp)

v6

vvvvvv

## Replace piano by safe

![v7](2/v7.webp)

v7

vvvvvv

## Colour cat

![v8](2/v8.webp)

v8

vvvvvv

## Give man a hat

![v9](2/v9.webp)

v9

vvvvvv

## Give cat an aura

![v10](2/v10.webp)

v10

vvvvvv

## Get a second winch for string

![v11](2/v11.webp)

v11

---

## "Timeline"

![timeline](2/timeline.webp)

The steps in order, with short names and version numbers


---

## Revision-line

![revisionline](2/revisionline.webp)

It might make as much sense, to name the changes (not the images)

---

## Environment

![v6](2/v6.webp)

When I was working here, I wanted to experiment with adding some environment

vvvvvv

## Add a sun

![v7*](2/v7p.webp)

v7*

vvvvvv

## Add houses and a tree

![v8*](2/v8p.webp)

v8*

Note that _I_ decide what goes together into a revision

vvvvvv

## Add a river

![v9*](2/v9p.webp)

v9*

vvvvvv

## Add a car

![v10*](2/v10p.webp)

v10*

---

## New revisionline

![revisionline-with-environ](2/revisionline-with-environ.webp)

---

## Speech bubbles

![v5](2/v5.webp)

Also at some point I looked into speech bubbles

vvvvvv

## Wisecracks

![v6**](2/v6pp.webp)

v6**

Note that this frame makes sense, however this would not make sense together with the sun.

vvvvvv

## More realistic response

![v7**](2/v7pp.webp)

v8*

---

## New revisionline

![revisionline-with-2-branches](2/revisionline-with-2-branches.webp)

---

## Even more complex

![revisionline-with-branches](2/revisionline-with-branches.webp)

---
## Tree

![root](2/root.webp)
---

## Tree with branches
![branchpoints](2/branchpoints.webp)
---

## Two similar trees
![revisionline-with-branches](2/revisionline-with-branches.webp)
vvvvvv
![revisionline-with-branches-alt](2/revisionline-with-branches-alt.webp)

---

## Trees and branches in git

- In `git` you work with _repositories_
- A repository is a tree with (usually) a single root
- The tree consists of _commits_ (aka _revisions_)
- It has one or more branches, all running from the root to the tip
- Each branch has a name
- A branch does not have to "stick out", you can even have two branches completely overlap
- Default branch name is `main` or `master`

---

## Branches

![drawn-branches](2/drawn-branches.webp)

---

## Why do we need a repository

### Undo specific commit

- "Undo" normally allows undoing of the last action.
- In VCS, you can _revert_ any commit
- e.g. once the drawing is finished, you could do `git revert v4`, what would happen?

The faces should be removed from the final image
<!-- .element class="hidden-answer" -->

<button>show answer</button>

- Note that sometimes a later commit depends on a previous one, meaning manual fixing is needed.

vvvvvv

### Separation of features

- By doing certain things in separate branches, you can try things without polluting the stable code.
- e.g. I could experiment adding text bubbles, and only decide later if I needed them
- It means that if you have a function, you could work on some changes, but still keep the original function until your changes are done

vvvvvv

### Merge two branches

- It's possible merge two branches.
- If we are on the `main` branch, and type `git merge environment`, what should happen?

The changes in the `environment` branch should be "imported", so there will be all the changes in the `main` branch, and the sun/house/tree/car.
<!-- .element class="hidden-answer" -->

<button>show answer</button>

- Also here, this may not always be possible automatic, or the result may not always make sense. e.g. import the `speech-bubbles` branch into the `environment` branch.

vvvvvv

### Cherry-pick certain commits

- It's not necessary to merge whole branches, but e.g. only import the commit that adds the car to the `main` branch.

vvvvvv
### Different people can work on different branches

- And then sync through something like GitHub

vvvvvv
### History, attribution and comments

- At any time it's possible to see the full history of the repository, and go to any spot in the tree
- At this spot, new branches can be started
- The history will show _who_ did a certain commit and show the _commit message_.
- Git tools also allow you to see in the current code, when a certain line was last changed and by whom.

---

![revisionline-with-branches](2/revisionline-with-branches.webp)

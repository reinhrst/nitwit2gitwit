# Lesson 5

- Github (because....)
- Much more about local git

---

### Github: broad overview

For profit company (owned by Microsoft)

- "Centralised" repo -- either private or public (open source)
- Some tools to make git-stuff nicer (web based interface)
- Suggested git workflows
- Project management (code reviews / issues / project boards / scrum boards)
- Markdown rendering
- Build & run "space"
- Web hosting for people/projects
- All integrated (links)

vvvvvv

#### Decentralised repo

<pre class="mermaid">
sequenceDiagram
    actor Linus
    actor James
    actor Anne
    actor Claire
    actor Sandra
    actor John
    Linus ->> James: sha23
    Linus ->> Anne:  sha2
    Anne ->> Claire: sha2,sha5
    Sandra ->> Anne: sha7
    John ->> Sandra: sha5,sha3
    James ->> John: sha13
    James ->> Claire: sha2
    Claire ->> John: sha4
    Claire ->> Sandra: sha14
    Sandra ->> Linus: sha1,sha15,sha2,sha3
    John ->> Linus: sha16
    Linus ->> Claire: sha7
    Claire ->> Linus: sha13
    Note over Linus: Releases version 2.16
</pre>

vvvvvv

#### Centralised repo

<pre class="mermaid">
sequenceDiagram
    participant repo
    autonumber
    actor Linus
    actor James
    actor Anne
    actor Sandra
    actor John
    Linus ->> repo: sha23
    Linus ->> repo:  sha2
    repo ->>+Anne: all changes
    repo ->>+Sandra: all changes
    Anne ->>-repo: sha2,sha5
    Sandra-->> repo: sha7 (fails)
    repo ->> Sandra: sha2,sha5
    Sandra ->>-repo: sha7
    repo ->>+John: all changes
    John ->>-repo: sha5,sha3
    repo ->> Linus: all changes
    Note over repo,Linus: Releases version 2.16
</pre>


vvvvvv

#### Github and centralised repo

- Git is _free software_ and everyone can (and could) set up a certralised repo for free (if they have a server)
- Github offers these kinds of repos "as a service" (GaaS)
- Github made repos free for Open Source projects and small projects (you pay above certain limits)
- Github added additional useful tools (like bug tracker)
- These days most open source projects on Github (90%), some on GitLab (9%) and others (1%). Almost nobody self-hosted.

- Centralised repo just special case of Decentralised repo
- Centralised repo great, if it's always up, and you have internet connection.
- Even with centralised repo, decentralised workflow still works.

_percentages were made up by me, please don't quote :)_

vvvvvv


#### Github suggested git workflows

- "Conventions" on how to do things
- Pull requests
    - If you don't have access
    - By convention in some repos
    - If you want someone to check you work
    - Allows for code reviews


vvvvvv

#### Project management

- Code reviews: back and forth on changes before merge is done
- Github issues: list of bugs / questions / wishlist / (what you want it to be). Iterative back and forth / status / link to commits.
- Project boards: Very flexible, a.o. scrum boards
- Often too limited for very large projects, but great in 99% of cases

vvvvvv

#### Markdown

- Markdown is a language that allows you to write (readable) plain text documents, which render to text with layouts
- Different flavours (e.g. GFM, Github Flavoured Markdown)
- Headers / **bold** / _italic_ / [links](https://github.com/) / images
- Depending on flavour / plugins:
    - Tables
    - Code highlighting / rendering / diagrams (e.g. Mermaid)
    - Smilies
    - Math $e^{i\pi}+1=0$
- By default (mainly) used for web documents (websites), but some flavours for presentations, books, etc
- Alternatives: Asciidoc, RTF, LateX.
- Github renders markdown in `.md` files (hence `Readme.md`), and in issues / code reviews / etc.

vvvvvv

#### Other tools

- Lot of code needs a _build_ or _Continuous Integration_ step (e.g. make HTML from Markdown, compile programs, run tests). Github provides (secure) server-space where scripts can be run automatically.
- Everyone gets a webspace (`https://#USERNAME#.github.io/`) that you can use for free (one per account). Afaik webspace per _repo_ is a paid option.
- All Github tools try to be integrated; so commit messages can link (or modify) to issues, links are made between different parts of the system.

---

### Local git

- Exercises will only take you that far; you _really_ learn when you work with it.
- **Take the pain**
    - Two hours per week is not enough
    - You will run into problems _before_ you learn the solution

---


### What stuff should one commit (in real life)

- Everything that you created (code, images, graphs)
- Readme files / documentation / instrcutions (ideally in Markdown)

##### But not:
- Raw data (usually; you can have a "data repo")
- Derivative (by script) stuff
- Huge files (esp if they change a lot)
- Binary files that change a lot (e.g. Word documents or zip files)
- Commented out / not used code (make branch!)
- Code that is in another repo
- Development files for your environment
- PASSWORDS / SECRETS (remember that all history is normally kept!)

vvvvvv

_There are always exceptions to this rule, in time you'll find out what works for you. However have rules within one repo!_

---

### Git is not a backup (but github may be)

- Editing something in the working directory does nothing with git
- When you add something to the index, it can be retrieved from the repo if deleted
- When something is committed, it can be retrieved from the repo (as long as it's a parent of some branch)
- However remember: the repo is only a local directory; only when you push to someone else (or github) you have an (online) backup

- Really _really_ important stuff need online and offline backups.

---

### How often should one commit their code

It's a personal preference / agree on rules per project or repo / you will get a feeling for what works for you _(for now: often to get experience)_

##### My suggestion:
- When you finish something
- When you start working on something else
- At least every couple of hours (lunchtime, before end of day?)
- It does not have to work (although commit it as soon as it works), and note in commit message
- Remember: semantic changes

- When you start to change / rewrite lots of code


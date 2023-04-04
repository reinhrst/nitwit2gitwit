# Lesson 6

- Startup scripts for shell
- Setup ssh for Github
- Setup R Studio for use with git(hub)
- "What should I make a repository" discussion
- Selective commits (`.gitignore`)

---

We're going to optimise your shell-experience a bit

|shell|rc file|
|----|----|
|`bash`|`~/.bashrc`|
|`zsh`|`~/.zshrc`|

Anything you put in these files (for now, there is no difference between these files) will be executed every time you open a shell.

Try it:

```console
$ echo 'PS1="\w \$ "' >> .bashrc  # (or .zshrc)
```

Open a new shell (new tab in terminal program)

vvvvvv

- You can edit these files with nano (or any other text-editor).
- These files can grow quite large if you work a lot with shell and have many things you like to set-up
- E.g. my init-files are about 500 lines long :).

---

### `ssh`

- Stands for Secure SHell (however is not a shell)
- Allows one to connect securely to another computer and start a shell there
- Can do other things like copy files (`scp`) or forward ports
- Used as the default connection method in git(hub)

vvvvvv

#### Password-based authentication

_Grossly simplified_

<span class="mermaid">
sequenceDiagram
  participant local
  participant remote
  local ->> remote: start ssh session please
  remote ->> local: sure, my public key is ABC
  Note over local: check remote's public key
  Note over local,remote: securely agree on session key
  local ->> remote: Encrypted(please log in with username X and password Y)
  local ->> remote: Encrypted(ok, welcome)
</span>

vvvvvv

#### Key-based authentication

_Grossly simplified_

<span class="mermaid">
sequenceDiagram
  participant local
  participant remote
  local ->> remote: start ssh session please
  remote ->> local: sure, my public key is ABC
  Note over local: check remote's public key
  local ->> remote: Encrypted(Here's my public key)
  local ->> remote: Encrypted(ok, welcome)
</span>

Imagine "you prove who you are, by being given a locked box, and giving back the content of the box". You never have to show the key to prove that you actually have it.

vvvvvv

- Remember, in PubPrivKey system, encryption happens with a pair a keys: one public one private
- Private key should never be shared with anyone (unlike e.g. passwords)
- Private key is often stored encrypted (so needs a passphrase before use)
- Public key may be shared publicly (e.g. on your website)
- Anything _encrypted_ with one key can only be _decrypted_ with the other:
  - If encrypted with public key, decryption requires private key (used for message TO you, everyone can encrypt, only you can decrypt).
  - If encrypted with private key, decryption requires public key (hence for messages FROM you: everyone can decrypt, but will know for sure that it was you encrypting the message)
- if A and B want to talk securely (confidential (nobody can read messages) and integer (nobody can spoof or alter messages)):
  - A --> B: PrA(PuB(message1)) (so: message encrypted first with B's public key, and then A's private key)
  - B --> A: PrB(PuA(message2))

vvvvvv

- Github only allows connections using `ssh` with Key-Based Authentication (no password authentication). Anonymous connections are allowed over HTTPS.
- So in order to use Github, we need to have a (unique) private/public key pair.
- We will then associate our public key with our account, so github knows that if that key is used, it is you wanting in.
- Even github will not know (or ever ask for, etc) your private key.
- Keep your private key as secure as your Github password (as in: never let it leave your computer)
- If you have multiple computers, best to generate 1 key per computer and associate multiple in your account.
- If you loose your private key (and only use it for Github): no problem, just generate a new key, and associate it with your account.

---

### Github and SSH key

- So in order to use Github, we need to have a (unique) private/public key pair.
- Let's first check (in GitBash / Zsh) if we already have one. If so, it should be in `~/.ssh/` directory. `ls` that directory and look for two files `id_*` and `id_*.pub` (the `.pub` is the public key, the other one the private key).
- If you don't have the keys, we create some (from thin air; [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)):
  - First create `~/.ssh/` if that does not exist
  - Now run `ssh-keygen -t ed25519 -C "computername"`
  - When it asks `Enter a file in which to save the key`, just press enter (accept the default)
  - When it asks for passphrase, for now we select an empty passphrase
- Because we did not add a passphrase, we can (I think) skip the ssh-agent stuff
- Now connect to github: `ssh git@github.com` (explain parts of the command)

vvvvvv

- OK, that didn't do much, because Github doesn't know about our key yet :)
- Follow [these instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account):
  - print the ***public*** ssh key: `cat ~/.ssh/id_XXXXXX.pub` and copy this to clipboard (select is sometimes enough, otherwise we have to experiment)
  - Go to <https://github.com/>, log in, click your photo on the right top and choose "settings"
  - Go to "SSH and GPG keys" --> New SSH Key
  - Title: computer name, type: Authentication key, key: whatever you just copied, and "Add SSH key"
- Now again connect to github: `ssh git@github.com` (explain parts of the command)

```console
$ ssh git@github.com
Hi reinhrst! You've successfully authenticated, but GitHub does not provide shell access.
Connection to ssh.github.com closed.
```

<!-- .element class="fragment" -->

---

### Push some work to github

- On the Github homepage, choose "New" (repository)
- Choose a name, make it private, and don't select anything else (but click "Create Repository)

...or push an existing repository from the command line
```bash
git remote add origin git@github.com:reinhrst/projectA.git
git branch -M main
git push -u origin main
```

^^^^ these lines are the commands we need to execute to connect our (existing) local git to Github

vvvvvv

```bash
git remote add origin git@github.com:reinhrst/projectA.git
# this tells our local git that we want to add a new remote repository to talk to.
# The remote repository is called "origin" (default name) and can be found at this address
git branch -M main
# This renames the current branch to "main"; useful sometimes, but not now
# so we will skip this
git push -u origin main
# Tells our local git to push the "main" branch to "origin"
# (normally the remote branch name will be the same as the local branch name (main)
# but this is not required, and in certain situations it makes sense to have
# different names)
```

- So let's execute the first and third line in your own local git repository (make sure to use the line you got on the webpage, and not `reinhrst/projectA.git`)
- After pushing, reload the webpage.

vvvvvv

Let's make a quick Readme file for this repository:

```console
$ echo "# Save a unicorn (today)

This repository contains my work on project save-a-unicorn.
It contains:
- R code to create maps of unicorn sightings
- Instructions on how to build unicorn traps
- Field-instructions on how to deal with unicorn-:poop: (aka gold)
" > Readme.md
$ git add Readme.md
$ git commit -m "added a readme file"
$ git push
```

Now reload our webpage

_Readme files on private repos are very useful to remind future-you what this repo was about_


vvvvvv

From now on, after every commit in this repository, you should type `git push` to push it (no need to do `-u origin` unless you have a new branch).

---

#### Workflow new Github repo

1. Local in the lead
  - Create repo on your computer (`git init`)
  - Create empty repo on Github
  - Copy-paste the `git remote add` and `git push -i origin main` codes
2. Github in the lead
  - Create repo on Github, including Readme / License / anything (Github will do `git init`)
  - `git clone` on your local computer

NB: `git clone` clones an existing repo from Github (or elsewhere); it can be used for new and (long) existing repos.

---

### Setup R Studio to work with git(hub)

---

### "What should I make a repository" discussion

- Git should not dictate your directory structure (usually)
- Normally, your directory structure will look something like this:

```asciiart
projects
|- projectA
|  |- src
|  |- data
|  |- output
|  |- cache
|  |- doc
|- projectB
|  |- src
|  |- data
|  |- output
|  |- cache
|  |- doc
```

vvvvvv


- Or with one more level

```asciiart
projects
|- Gdansk
|  |- projectA
|  |  |- src
|  |  |- data
|  |  |- output
|  |  |- cache
|  |  |- doc
|  |- projectB
|  |  |- src
|  |  |- data
|  |  |- output
|  |  |- cache
|  |  |- doc
|- OxNav
|  |- projectC
|  |  |- src
etc
```

vvvvvv

- The dirs with `*` are the ones that you want to make repo roots (where the `.git` directory lives)
- The dirs with `$` are the ones that you want to add to your repos

```asciiart
projects
|- projectA *
|  |- src $
|  |- data
|  |- output
|  |- cache
|  |- doc $
|- projectB *
|  |- src $
|  |- data
|  |- output
|  |- cache
|  |- doc $
```

vvvvvv

- Sometimes you find that one project borrows from another. For instance, if in `projectA` you wrote an amazing function, you might have somewhere in `projectB` something like:

```
import "../../projectA/src/function.R"
```

- This is not good (since a repo should not depend on things outside of the repo)

Solutions:

- If projectB uses most of projectA's code, make projectA a module and import it in projectB
- Else make a module "KasiaLibrary" and move the shared code in there. Make this module a dependency of both.

---

### Selective commits

- You can only commit the `src` and `doc` directories to your repository by doing `git add src doc`, rather than `git add .`.
- You don't have to add directories to the repo, you add files. So even to an empty repo, you can do `git add src/test.R src/library/subdir/test.R`. No need to `git mkdir` (also, it's not possible to do so)
- (Because git has no concepts of directories, you were making placeholder files during the gitlab course; if you want a `git clone` to create an (empty) `data` directory, you just check in a `data/.placeholder` file.)
- However, if you only check in some files / directory, there will always be a mess in your `git status` with untracked files.
- Also, if you want to ignore (for git) files _inside_ directories, things get even more complex; you'd have to do `git add src/*.R src/*.Rmd` or something.

## 🎈`.gitignore`🎈

<!-- .element class="fragment" -->

vvvvvv

### `.gitignore`

- Put a file called `.gitignore` in your repo root (next to the `.git` directory)

```gitignore
# ignore all .doc files (anywhere)
*.doc

# ignore all .html files (anywhere)
*.html

# ignore all files in ANY directory named temp
temp/

# ignore all files in the data,cache and output dir in the root directory
/data/
/cache/
/output/

# make an exception for the placeholder file in data
!/data/.placeholder
```

vvvvvv

- The `.gitignore` file is committed like anything else, so the ignores apply to all people sharing the repo
- There is also a `global.gitignore` file (in your home dir) that applies to your whole computer, and a way to add files to the ignore list without putting them in the shared `.gitignore` file.
- In time you'll learn to put the files specific to the _project_ in `.gitignore`, whereas the files specific to your OS / IDE (e.g. `.DS_Store`) in the other ignore locations

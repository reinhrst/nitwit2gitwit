# Lesson 8

- Use git to see old versions of your code
- Work with GitHub issues
- How to push/pull branches to/from GitHub

---

- Using `git checkout` you can:
  - change branch: `git checkout BRANCH`
  - create a new branch: `git checkout -b BRANCH`
  - go to any spot in your git tree: `git checkout COMMITREF`
  - overwrite any local file with the version from the index (which is usually `HEAD`):
    - `git checkout anthem.txt` -- replace the file `anthem.txt` with index version
    - `git checkout code` -- replace the directory `code` with index version
    - `git checkout .` -- replace all files with index version
    - NB: Adds files that are in index (but removed locally); does not remove files that are not in index, but exist locally (untracked files); use `git clean` for that

---

Interactive:

- Find the gitwit repo on GitHub.
- Clone the repo
- Check out the version that was committed on `2023-03-25T10:21:49+01:00`
- Make a new branch `FIRSTNAME`
- Make some changes in some files, and commit
- use `git revert COMMITREF` to revert your changes
- Check the file, and check the log.
- Again make some changes in your files
- Now revert the files using `git checkout`
- Check that there are no local changes left.

---

Interactive2:

- Find the issues on GitHub for the gitwit repo
- Choose one issue each and fix in your own branch

vvvvvvvv

- That didn't work, because the file did not yet exist in the spot where this branch was made
- Best to start again: checkout `main` and delete the branch you just made
- Now make a new branch (starting at `main`) called `FIRSTNAME` and fix your issues. Make sure to use commit message: `fixes #3` (or `fixes #4`, depending on what issue you're working on)
  - In GitHub, issue numbers always have a pound sign (`#`) in front of them (aka "hashtag" to millennials). Whenever you use `#3` anywhere in GitHub, or in a commit message, it will create a link to the issue
- Next, push your branch to GitHub

vvvvvvvv

- Find both your own, and the other person's branch on GitHub
- Look at both issues. Any changes?
- Pull the other person's branch
- Now each person will merge the other person's fix to main, and push
- Check the issues again, what has changed


- Checkout `main` and delete the branch you just made

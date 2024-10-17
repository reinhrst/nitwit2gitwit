# Playtime 2

---

Use the repository below for the questions.
Each page of questions starts with this repository,
so one page of questions does not influence the next.

However questions on one page do affect each other,
if question 1 changes the repository, question 2 assumes the changed repository.

I will not ask you to draw images or how the repository looks after the questions, but it may be helpful to try to imagine this in your own mind (or draw on paper).

vvvvvv

![branches-with-names](2/branches-with-names.webp)

---

How many commits are on the `main` branch?

I'm on `main`, and I type `git revert v9`. What happens? How many commits are now on the `main` branch?

I type `git revert v7`. What happens? How many commits are now on the `main` branch?

- 11
- an extra commit is added to the `main` branch, that is the opposite of `v9` (-hat). The final image on the `main` branch is now like the previous last image, but without a hat on. There are now 12 commits.
- an extra commit is added replacing the safe with a piano. So the result is without a hat and with a piano instead of a safe. There are now 13 commits on the `main` branch.

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvv

We are on the `environment` branch.

What is the effect of `git revert v4`?

What is the effect of `git revert v8`?

- An extra commit is added to the `environment` branch, removing the faces
- This is interesting, since `v8` is not in the ancestry of `environment` (note, although we have `v8*` on the environment branch, remember that these names were only chosen for convenience sake; in `git` world these will be called `64f9d` and `1ef70` or something, so they have _absolutely no_ relation to `git`). `git` itself does not care that `v8` is not on the `environment` branch, and will still try to add a commit that is the opposite of `v8`, so "remove colour from the cat". This however will lead to a conflict, since the cat is not coloured.

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvv

We are on the `pollution` branch

What is the effect of `git merge environment` ?

What is the effect of `git merge speech-bubbles` ?

- The `pollution` branch will grow one commit, namely the `v10*` one, adding the car. Note that there are different merge-strategies, and not all add the merged in branch into the current branch, but for these questions we assume that they do.
- The `pollution` branch grows another two commits, and now has a car, and speech bubbles "Say hello to my little friend" and "HELP".


<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvv

We are on the `speech-bubbles` branch. What is the effect of `git merge main`

What would be the difference if _instead_, we would have been on the `main` branch and do `git merge speech-bubbles`?


- Remember that `main` is just a branch as any other. The result is that the `speech-bubbles` branch grows with all the commits that were done since the last common commit, so `v6`, `v7`, `v8`, `v9`, `v10`, `v11`
- There are two differences: (1) only the branch you are on is affected, so in the former case the `main` branch would stay the same and the `speech-bubbles` branch grows, in the latter case the other way around. Secondly, _using this merge strategy_ the difference is that in the former case the changes are ordered to first have `v6**` and `v7**` and only then `v6...v11`, in the latter case it's the other way around. The resulting image would be the same in both cases.

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvv

We are on the `main` branch.

What is the effect of `git cherry-pick v6**`?

What is the effect of `git cherry-pick v9*`?

What is the effect of `git cherry-pick v7**`?


- There will be one more commit on `main` that adds text bubbles "Say hello to my little friend" and "I hate rainy days".
- One more commit, adding a river.
- If this was done on a clean repository, it would give a conflict, however since `v6**` was already merged, it will work and replace the second bubble with HELP. So on main there will now be 3 new commits (as compared to the original repo), one adding 2 bubbles, one adding a river, and one replacing the second bubble.

<!-- .element class="hidden-answer" -->

<button>show answer</button>

vvvvvv

We are on the `main` branch.

I want to change the picture in the following ways: replace the safe by a piano, and add a car and a sun. What commands do I use?

- `git revert v7; git cherry-pick 'v10*'; git cherry-pick 'v7*'`. Some remarks: (1) the semicolon `;` means "next command" in shell. Also correct is `git revert v7 && git cherry-pick 'v10*' && git cherry-pick 'v7*'`. `&&` means "only run the next command if the previous command was successful". (2) we need quotes around `v7*` and `v10*` because `*` has a special meaning in shell. It just shows that my naming conventions for the commits was not that good, and the `git` way of naming things is much better.

<!-- .element class="hidden-answer" -->

<button>show answer</button>


vvvvvv

We are on the `main` branch.

I want to add text bubbles "Say hello to my little friend" and "I hate rainy days" but in this exercise you are _not allowed to use `git cherry-pick`_.

- `git merge speech-bubbles && git revert 'v7**'`

<!-- .element class="hidden-answer" -->

<button>show answer</button>

---

## Some shell practice

- Make a new directory `playtime-2` (or what you want), and in that directory make two subdirectories `A` and `B`.
- Make another subdirectory `C.txt` (never in real life give your directories the extension `.txt` unless you want other people (including your future self) to hate you. However nothing technical is stopping you from putting whatever extension you want in a directory name.

vvvvvv

- The command `seq #end#` prints all numbers from 1 to _end_. Create a file `100.txt` in the `A` subdirectory, containing all numbers from 1 to 100.
- Copy the file `100.txt` to the `C.txt` subdirectory.
- Now in the last command, replace `C.txt` by `D.txt`. What happens?
- Print the `D.txt` file to the terminal. You will see that you cannot see the whole file at once without scrolling.
- The command `less` takes the input, and only shows as much as fits on the screen. You can pipe any output into this command by adding `| less` (`|` is the pipe symbol). Try this and see how it works. Using `space` you can scroll down. Using `q` you can quit the `less` program.
- Finally, remove the `100.txt` file in the `A` subdirectory.

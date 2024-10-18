# Homework take-aways

`cat test.txt` will print the content of `test.txt` to the screen.

However if you do `cat` by itself, you seem to be "stuck".

Things to try: CTRL-C (break), CTRL-\ (really break), CTRL-D (exit).

Sometimes CTRL-D on newline.

However, don't press it twice, or you'll exit your shell ;)

---

# Lesson 3

- Numeral systems: binary, octal, decimal, hexadecimal
- CLI commands: pipe, redirect, how programs fit together (& terminal)
- Diff and Patch

---

## Numeral systems

If you thought that at least numbers were something you could count on being simple....

**You're wrong!!**

vvvvvv

## Numeral systems

- Decimal (base 10)
- Binary (base 2)
- Octal (base 8)
- Hexadecimal (base 16)
- Base 64
- Base 256


---

## Decimal (base 10):


<foobar>
$$
\begin{aligned}
42 &= 4 * 10 + 2 * 1 \\
42 &= 4 * 10^1 + 2 * 10 ^0 \\
123450 &= 1 * 10^5 + 2 * 10 ^ 4 + 3 * 10^3 * 4 * 10 ^ 2 + 5 * 10^1 + 0 * 10^0 \\
& \\
3.14 &= 3 * 10^0 + 1 * 10^{-1} + 4 * 10^{-2}
\end{aligned}
$$
</foobar>

---

## Binary (base 2)


Written as `0b.....`

<foobar>
$$
\begin{aligned}
 0\mathrm{b}10 &= 1 * 2^1 + 0 * 2 ^ 0 = 2 \\
 0\mathrm{b}101010 &= ...
\end{aligned}
$$
</foobar>

A single 1 or 0 is called a bit. 8 bits is a byte:

<foobar>
$$
\begin{aligned}
 0\mathrm{b}00000000 &= 0 \\
 0\mathrm{b}11111111 &= 255
\end{aligned}
$$
</foobar>

_There are 10 types of people in the world: those who understand binary, and those who don't._

vvvvvv

## Endianness

![byte](3/byte.webp)

Please decode what byte is in the signal above

---

## Hexadecimal (hex; base 16)

Written as `0x.....`
We need characters for the numbers 10-15: `A=10, B=11, C=12, D=13, E=14, F=15`.
Both uppercase and lowercase used

<foobar>
$$
\begin{aligned}
 0\mathrm{x}10 &= 16 \\
 0\mathrm{xFF} &= ... \\
 0\mathrm{xdeadbeef} &= ... \\
\end{aligned}
$$
</foobar>

Two hex-digits are one byte (16 * 16 = 256)

---
(lesser systems)

## Octal (base 8)

Written as `0o.....` or `0....`

Only used in specific contexts

## Base 64

Uses symbols `0-9a-zA-Z` (10 + 26 + 26 = 62) and two extra (often `+` and `\`).

Used to display binary data in "printable symbols"

vvvvvv

### Side note: other non-computer bases

- Base 10 comes from "counting on one's fingers"
- Base 12  (duodecimal) minor and speculative usage, foot-inch, dozen-gross, months in year, 12 hours in a day (and 12 in a night).
- Base 20 (vigesimal) Mayans, some early European systems
- Base 60 (sexagesimal) used by Babylonians and still in use for time-keeping / angular positioning:

<foobar>
$$
\begin{aligned}
 5\mathrm{h} 30\mathrm{m} 12\mathrm{s} &= 5 * 60^2 + 30 * 60^1 + 12 * 60 ^ 0 \mathrm{s} \\
 77\mathrm{°} 00' 06'' &= 77 * 60 ^ 0 + 0 * 60 ^{-1} + 6 * 60^{-2} = 77.0013\mathrm{°} \\
 15\mathrm{°} 32' 28'' &= 15 * 60 ^ 0 + 32 * 60 ^{-1} + 28 * 60^{-2} = 15.54410\mathrm{°} \\
\end{aligned}
$$
</foobar>

UK until 1971: 4 farthing = 1 penny, 12 pence = 1 shilling, 20 shilling = £1

Note that base 12 and base 60 nice for mathematical reasons.

---

## Why all these bases / when to use which

- Decimal is just because people are used to it
- Computers work with bits and bytes (= 8 bits), which have 2 and $2^8=256$ values. So it's nice if your number system uses powers of 2 or powers of 256.
- Binary has $$2^1$$ values per digit (so 1 bit)
- Octal has $$2^3=8$$ values per digit (so 3 bits)
- Hexadecimal has $$2^4=16$$ values per digit (so 4 bits, 2 hex-digits = 1 byte)
- Base 64 has $$2^6=64$$ values per digit (so 4 digits = 24 bits = 3 bytes)


vvvvvv

Generally things will have a prefix:

- No prefix: decimal
- `0b...`: binary (eg. `0b10101010`)
- `0o....`: octal. Sometimes also (annoyingly) just `0...`. So `0123 !== 123` (`0123 == 0o123 == ...`)
- `0x...` hexadecimal. Often written in groups of two: `0xFF A0 01 00 45 76 7E 0E` to represent bytes.

Sometimes, you can only know from context:

- If things mix upper and lowercase letters and numbers, good chance it's base64
- If things mix numbers and letters A-F (either uppercase or lowercase but not both) it's usually hexadecimal
- Some commandline programs (like `chmod` always expect octal numbers)
- Some domains always use hexadecimal (e.g. in HTML, color grey is `rgb(127, 127, 127) == #7F7F7F`. So `#111111 !== rgb(11, 11, 11)`

---

## CLI programs


```text
           command line parameters
                      |
                      |
                      V
                  *-------*
     (stdin --->) |PROGRAM|----> stdout
                  |       |----> stderr
                  *-------*
                      |
                      |
                      V
                return code
```

vvvvvv

## Connect them

(like audio equipment / signal processors)


```text
             *-----*        *-----*        *-----*
(stdin --->) |PROG1|------->|PROG2|------->|PROG3|-------> stdout
             |     |--\     |     |--\     |     |--\
             *-----*  |     *-----*  |     *-----*  |
               | ^  stderr   | ^ ^ stderr         stderr
               | |    |      | | |   |              |
               v |    v      v | |   v              v
             *-----*        *-----*
             |FILE |        |PROG4|
             *-----*        *-----*

```

vvvvvv

## Default filedescriptors

- `stdin`: standard input (to a program). Connected to terminal (what you type) by default, if not piped in from somewhere else
- `stdout`: standard output (from a program). By default print to terminal.
- `stderr`: standard error (from a program). Here the program will send warnings and error messages. By default connected to the terminal

Redirections

- `|` pipe character, connects the `stdout` of the previous program to the `stdin` of the next program.
- `>` sends the `stdout` of the previous program to a file
- `>>` appends the `stdout` of the previous program to a file
- `<` uses the content of a file as `stdin` to the **previous** program
---

## Some commands
These commands all work on `stdin`, but can also take a filename (or multiple)

`cat` -- print content
`tr abc def` -- replace every `a` with `d`, every `b` with `e`, etc.
`wc -l` -- count lines
`wc -c` -- count characters
`grep Raven` -- only show lines with the word "Raven"
`grep -v Raven` -- only show lines without the word "Raven"
`grep -n Raven` -- `-n` adds line numbers
`head -n 10` / `tail -n 10` -- show first / last 10 lines
`cut -d ' ' -f 2-3` -- show words 2 and 3 for each line
`|` is the command to connect the `stdout` of one program to the `stdin` of the next

e.g. `cat test.txt | grep hello | tr he ba`

---

# Hands-on

For this hands-on work, you need some files. In order to get the files, we will _clone_ a `git` repo from GitHub:

```
# make sure you're in a directory where you want to make a subdir "raven"
git clone --branch lesson3 https://github.com/reinhrst/raven
cd raven
```

NOTE: Even though we use a `git` repo to download the files, the things we do in this playtime are NOT using `git`.

---


In the `raven` directory there are different versions of the poem by E.A.Poe.
For now we focus on `original.txt`.

- Print the poem
- How many lines does it have?
- Print only the lines with `raven`.
  Is this what you expected?
- How many lines are there without an `a` in them.
- Print the lines with both `bird` and `fancy` in them
- Now the same, but only the first line
- Now the same, but with line numbers
- Can you make the poem about a Bever?

---

## `diff` and `patch`

Understanding `git` means understanding `diff` and `patch`, which do most of the interesting work.

- `diff file1 file2` shows the difference between 2 files
- `diff --color --unified file1 file2` shows the difference between 2 files in better format
- `patch orginal patchfile -o -` applies the patchfile (result of diff) to original

---

Let's use `diff` so we understand how it works

- Look at the contents of `orginal.txt`
- Now look at the contents of `orginal2.txt`
- Determine the differences between the two files.

---

- look at the differences between `modern.txt` and each of `modern?.txt`
- make a patchfile for `modern.txt` to `modern2.txt` (how can we write `stdout` to a file? See lesson 1)
- apply this to `modern3.txt`. Save the result in `modern23.txt`.
- now add the changes of `modern4.txt` to it `modern234.txt`
- now make `modern2345.txt`. Did it work? Why not?

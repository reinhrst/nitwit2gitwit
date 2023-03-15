---
marp: true
paginate: true
---

# Homework take aways

`cat test.txt` will print the content of `test.txt` to the screen.

However if you do `cat` by itself, you seem to be "stuck".

Things to try: CTRL-C (break), CTRL-\ (really break), CTRL-D (exit).

Sometimes CTRL-D on newline.

However, don't press it twice, or you'll exit your shell ;)

---

# Lesson 2

- Number systems: binary, octal, decimal, hexadecimal
- CLI commands: pipe, redirect, how programs fit together (& terminal)
- Diff and Patch

---

# Decimal (base 10):

$$
\begin{align}
42 &= 4 * 10 + 2 * 1 \\
42 &= 4 * 10^1 + 2 * 10 ^0 \\
123450 &= 1 * 10^5 + 2 * 10 ^ 4 + 3 * 10^3 * 4 * 10 ^ 2 + 5 * 10^1 + 0 * 10^0 \\
& \\
3.14 &= 3 * 10^0 + 1 * 10^{-1} + 4 * 10^{-2}
\end{align}
$$

---

# Binary (base 2)

"The other day I told my friend 10 jokes about binary.
Unfortunately, he didn’t get either of them!"

Written as `0b.....`

$$
\begin{align}
 0\mathrm{b}10 &= 1 * 2^1 + 0 * 2 ^ 0 = 2 \\
 0\mathrm{b}101010 &= ...
\end{align}
$$

A single 1 or 0 is called a bit. 8 bits is a byte:

$$
\begin{align}
 0\mathrm{b}00000000 &= 0 \\
 0\mathrm{b}11111111 &= 255
\end{align}
$$

(Note: little-endian vs big-endian)

---

# Hexadecimal (hex; base 16)

Written as `0x.....`
We need characters for the numbers 10-15: `A=10, B=11, C=12, D=13, E=14, F=15`.
Both uppercase and lowercase used

$$
\begin{align}
 0\mathrm{x}10 &= 16 \\
 0\mathrm{xFF} &= ... \\
 0\mathrm{xfaceb00c} &= ... \\
\end{align}
$$

Note: `0xFF FF FF FF` (`=0x01 00 00 00 00 - 1`)

---
(lesser systems)

# Octal (base 8)

Written as `0o.....` or `0....` (so sometimes `0123 != 123`)

Only used in specific contexts

# Base 256

Each byte is one "character"; used in practice by writing hexadecimal as groups of two.

---

# CLI programs


```asciiart
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

---

# Connect them (like audio equipment / signal processors)


```asciiart
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

---

# The terminal

All connections between programs (incl shell) are binary: `0100101110100101010101...`

The terminal (traditionally) transforms it into "characters" and then "pixels"

```asciiart
                    A
                    S         F
                    C         O    ....1....
                    I         N    ...1.1...
                    I         T    ..1...1..
01000001 ----> 65 ----> 'A' ---->  .1.....1.
                                   111111111
                                   1.......1
                                   1.......1
```

And in the other direction (when a key is pressed, sends the ASCII code as binary "on the wire").

---

# Some commands
These commands all work on stdin, but can also take a filename (or multiple)

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

# Play time

Each has their own environment.

In the directory `~/raven` there are 3 different versions of the poem by E.A.Poe.
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

# Diff and patch (the workhorses of git)

- `diff file1 file2` shows the difference between 2 files
- `diff -u file1 file2` shows the difference between 2 files in better format
- `patch orginal patchfile -o -` applies the patchfile (result of diff) to original

---

# Playtime 2

- look at the differences between `modern.txt` and each of `modern?.txt`
- make a patchfile for `modern.txt` to `modern2.txt` (how can we write `stdout` to a file? See lesson 1)
- apply this to `modern3.txt`. Save the result in `modern23.txt`.
- now add the changes of `modern4.txt` to it `modern234.txt`
- now make `modern2345.txt`. Did it work? Why not?

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

_If_ you choose the right function:

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

vvvvvv

Some examples: CRC-32, MD5, SHA1, SHA2, SHA3, SHA256, SHA512

Secure hashing is a field in itself (within mathematics; NIST)

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

## Playtime

- Use the `md5sum` program to calculate MD5 hash of different Raven versions.
  How many bytes is the output?
- Calculate md5 hash of `hello world`
- Calculate md5 hash of `hello world` again
- Calculate md5 hash of `hello world1`
- Calculate md5 hash of `hello world2`
- Calculate sha1 of `hello world`
- How big is an md5 hash? How big a sha1 hash?
- Advanced: did we _actually_ calculate the md5 of "hello world"?


vvvvvv

NB Hashing + encryption is used to create digital signatures!

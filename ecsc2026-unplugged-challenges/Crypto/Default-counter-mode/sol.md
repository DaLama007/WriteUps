# Default Counter Mode

## First ideas

- We get to choose two modes of encryption
- Once with a random nonce and once with the byte string 'mysupernonce'
- This hardcoded nonce seems vulnerable but lets see

---

## Deeper look 
To get encrypted flag we have to use the 1. encryption mode. But we can use the second to find out the key. We know the text that is getting encrypted and we know the nonce. This allows us to perhpas bruteforce the key.
After looking up a bit, encryption with the same key and the same nonce, keeps the encryption message rigurously the same.

--- 

Readthrough this blog: https://medium.com/@Espress0/cracking-aes-ctr-a-known-plaintext-decryption-walkthrough-8a46dec79594

This explains how knowing one block of the plaintext allows us to understand the parameters. But since the nonce stays the same, let's try to focuson that.

Lets try to xor encrypted text 1 by encrypted text 2. 

```

ct = b'ffa292f18ebe650b716451ce187d6858729a520904eb34cb'
ct2 = b'e7a292f18ebe650b716451ce187d6858729a520904eb34cb '

print(bytes([a^b for a,b in zip(ct,ct2)]))
```


I got this input with these parameters:

Simple cipher for these two:
- ct1: encrypt("hello")
- ct2: encrypt("pello")

output:
b'\x03Q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

This leaves us with the xor of the two ciphers,without the keystream.

I then discovered this post:
https://book-of-gehn.github.io/articles/2018/12/04/Fixed-Nonce-CTR-Attack.html

but still no idea, have to get key somehow

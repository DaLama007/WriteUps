# RRSA

Ok so I see that we have prime numbers which are irreversible. BUT we can calculate them by dividing the results of their multiplications.

n3/n1 = r^2.

```

r = math.sqrt(int(n3)/int(n1))
q = int(n2)/r
p = int(n1)/q


print("r= ",{r})
print("q= ",{q})
print("p= ",{p})
```

This provides us with the parameters used in the RSA.
We can now try and reverse it:

So we have to calculate private exponent and modulus and then use them to decrypt:

```
# lets calc the priv exponent of n1
e = 65537
d1 = pow(e, -1, (p - 1) * (q - 1))

# lets decrypt
print(long_to_bytes(pow(c1, d1, int(n1))))
```

Since m3 is a little special, but we can think like this:
" Suppose the prime factorization of n is given by

      $n = p1_k1 p2_k2 ... pr_kr$
Then it can be shown that

      $φ(n) = n (1 - 1/p1) (1 - 1/p2) ... (1 - 1/pr)$ "

Ok but this only works for distinct primes,so we have to do:
n3 · (1-1/p)(1-1/q)(1-1/r)

float point error still creates error so lets use the integer formula:

```
# lets do n3
euler = (p-1)*(q-1)*(r-1)*r
d3 = pow(e, -1, euler)

# lets decrypt
print(long_to_bytes(pow(c3, d3, int(n3))))
```
then we get flag:
ECSC{Rsa_but_with_two_Rs_like_in_vrrooooooom}

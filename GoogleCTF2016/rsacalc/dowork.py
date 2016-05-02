#!/usr/bin/python
import random
import string
import base64
import sha

proof=raw_input()
while True:
    a = ''.join(random.choice(string.lowercase) for x in range(8))
    s = sha.new(proof + a)
    k = s.digest().encode("hex")[:5]
    if k == "00000":
        print(a)
        break


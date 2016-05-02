rsacalc
======
# The Attack
To check out the problem, we had to connect to the following service:
```bash
ncat --ssl  ssl-added-and-removed-here.ctfcompetition.com 59999
```
```
How about some work?
proof=2SY+zPhsFk7u, sha1(proof+work).hex().startswith('00000')
```
We wrote a python script to do a simple proof of work so we could check out the rest of the problem.
```python
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
```

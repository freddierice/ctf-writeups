rsacalc
======
## The Poking
To poke at the problem, we had to connect to the following service:
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
After giving the proof of work, it shows the following: 
```
Welcome to the Cloud Computing Service!
Setting up the environment...
Done. Please input your desired operation: (type help for... help)
```
Naturally, we started playing around with the calculator until things got weird.  Things got weird pretty fast: 
```
help
Usage: [operand1] operator operand2
        Supported operations: +, -, *, /, ^, |, &, **, sqrt, encrypt, decrypt
1 + 2 
3
sqrt 4 
19773005982015197272052081637842914064726745781454688242701748462921367591634272728495444069359188386017290190642621325692422287039620571824558585805741369878071976763771688937511032215931942402270224599786445156234975469645294498049387525995941537090156018605634813882897061225407376074555692081293029011543275954504609450854079748979102310239678467816781445089635169698976405262126651132972642719532820508953515741283541673599919435694097248372666659238905975603970289313901095062721633355882106300722233163463467467727106270181794357101286163101974590707101661958047707461278259209830002238128769526950635281839696
```
What. 

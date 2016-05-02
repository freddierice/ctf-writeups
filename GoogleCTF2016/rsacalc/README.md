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
1977300598201519727205208163784291406472674578145468824270174846292136759163427272849544406935918838
6017290190642621325692422287039620571824558585805741369878071976763771688937511032215931942402270224
5997864451562349754696452944980493875259959415370901560186056348138828970612254073760745556920812930
2901154327595450460945085407974897910231023967846781678144508963516969897640526212665113297264271953
2820508953515741283541673599919435694097248372666659238905975603970289313901095062721633355882106300
7222331634634674677271062701817943571012861631019745907071016619580477074612782592098300022381287695
26950635281839696
```
What. That does not look like the square root of 4.  Keep this in mind for later on.  
```
Free trial finished.
Hey, don't forget your flag!
ALXx/zKUt1+k1o2hFLm21RyOY5+0r+3taucTrz5wJ1bbr6hi6VdzMRTEaAKINeEAWmuXq8DOPXDyLud9z/khtOL13o2nD48VlxKyUlP2qKYk6wFfN8Z/pOi7oxnRTAAPEwiPb+CkeGMu9hGUqifsNACWZIyMzX3PPO42oZIFlp/zAXlw/4TOqEuuGbtwyyTBwBgf0gvjiAmJHey+qd+VQRz6o+68e04kA+exZrDMS4vGJidHwx7B7UZgEtpIBTgxhcLlZQgW+UGFSmqYgqvhO+fQSHBG5ci0z6bOimPKJAZtmgEvtt+tChNPxL9Y0RlFWCoIbE+cJn0Qd/Wa+Pxd+Q==
```
Yes! We have the flag! It is
```bash
echo -n "ALXx/zKUt..." | base64 -d | xxd
0000000: 00b5 f1ff 3294 b75f a4d6 8da1 14b9 b6d5  ....2.._........
0000010: 1c8e 639f b4af eded 6ae7 13af 3e70 2756  ..c.....j...>p'V
0000020: dbaf a862 e957 7331 14c4 6802 8835 e100  ...b.Ws1..h..5..
0000030: 5a6b 97ab c0ce 3d70 f22e e77d cff9 21b4  Zk....=p...}..!.
0000040: e2f5 de8d a70f 8f15 9712 b252 53f6 a8a6  ...........RS...
0000050: 24eb 015f 37c6 7fa4 e8bb a319 d14c 000f  $.._7........L..
0000060: 1308 8f6f e0a4 7863 2ef6 1194 aa27 ec34  ...o..xc.....'.4
0000070: 0096 648c 8ccd 7dcf 3cee 36a1 9205 969f  ..d...}.<.6.....
0000080: f301 7970 ff84 cea8 4bae 19bb 70cb 24c1  ..yp....K...p.$.
0000090: c018 1fd2 0be3 8809 891d ecbe a9df 9541  ...............A
00000a0: 1cfa a3ee bc7b 4e24 03e7 b166 b0cc 4b8b  .....{N$...f..K.
00000b0: c626 2747 c31e c1ed 4660 12da 4805 3831  .&'G....F`..H.81
00000c0: 85c2 e565 0816 f941 854a 6a98 82ab e13b  ...e...A.Jj....;
00000d0: e7d0 4870 46e5 c8b4 cfa6 ce8a 63ca 2406  ..HpF.......c.$.
00000e0: 6d9a 012f b6df ad0a 134f c4bf 58d1 1945  m../.....O..X..E
00000f0: 582a 086c 4f9c 267d 1077 f59a f8fc 5df9  X*.lO.&}.w....].
```
encrypted. Bummer. 

However, since this problem is named rsacalc, and rsa is computed modulo a number, we figured that 197730... could be a modular square root of 4.  If th

from itertools import *
t = "13 14 16 25 27 31 34 35 41 43 45 46 47 52 53 54 61 64 67 72 74 76"
g = "AB BA BC CB CD DC CF FC GF FG BD DB GC CG FE EF CE EC DE ED AG GA"

s = set(g.replace(' ',''))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
    if set(g.split()) == set(nt.split()):
        print(p)
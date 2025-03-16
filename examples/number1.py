from itertools import *
t = "12 14 17 21 24 28 35 37 38 41 42 46 53 58 64 67 71 73 76 82 83 85"
g = "BH HB AB BA AH HA AE EA EC CE CD DC FD DF HF FH FG GF EG GE GC CG"

s = set(g.replace(' ',''))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(*p)
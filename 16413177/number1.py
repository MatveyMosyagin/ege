from itertools import *
t = "12 14 21 24 26 35 36 37 41 42 46 47 53 56 62 63 64 65 67 73 74 76"
g = "АБ БА БД ДБ АВ ВА БВ ВБ ВД ДВ ДЕ ЕД ВЕ ЕВ ЕК КЕ ВГ ГВ ЕГ ГЕ КГ ГК"

s = set(g.replace(' ',''))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
    if set(g.split()) == set(nt.split()):
        print(p)
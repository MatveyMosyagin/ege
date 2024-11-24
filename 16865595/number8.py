from itertools import product


a = 0
for i in (product('0123456789ABCDEF', repeat=8)):
    if i[0] != "0" and i.count("0") == 2 and (i.count("A") + i.count("B") + i.count("C") + i.count("D") + i.count("E") + i.count("F")) <= 4:
        a += 1
print(a)
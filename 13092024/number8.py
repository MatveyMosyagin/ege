from itertools import product
a = list(product('АВОРТ', repeat=4))
print(a.index(('Т', 'А', 'Р', 'А')) + 1)





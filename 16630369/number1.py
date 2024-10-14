from itertools import product
words = list(product('КЛРТ', repeat=4))
print(*words[66])

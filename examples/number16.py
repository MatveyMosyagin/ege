from functools import *
@lru_cache(None)


#Рекурсивные функции с возвращаемыми значениями
# def f(x):
#     if x < 3:
#         return 2
#     if x > 2 and x % 2 == 0:
#         return f(x-2) + f(x-1) - x
#     if x > 2 and x % 2 == 1:
#         return f(x-1) - f(x-2) + 2 * x
# print(f(32))

#Алгоритмы, опирающиеся на несколько предыдущих значений
# def f(x):
#     if x == 1:
#         return 1
#     if x == 2:
#         return 3
#     if x > 2:
#         return f(x-1) * x + f(x-2) * (x-1)
# print(f(5))


# def F(n):
#     if n < 3:
#         return 1
#     if n > 2:
#         return sum(F(i) for i in range (1,n))
# print(F(18))


#Алгоритмы, опирающиеся на одно предыдущее значение
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n-1) * n
# print(F(5))






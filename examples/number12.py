# a = '8'*68
# while ('222' in a) or ('888' in a):
#     if '222' in a:
#         a = a.replace('222', '8', 1)
#     else:
#         a = a.replace('888', '2', 1)
# print(a)

# s = '>' + '1' * 10 + '2' * 20 + '3' * 30
# while ('>1' in s) or ('>2' in s) or ('>3' in s):
#     if '>1' in s:
#         s = s.replace('>1', '22>', 1)
#     if '>2' in s:
#         s = s.replace('>2', '2>', 1)
#     if '>3' in s:
#         s = s.replace('>3', '1>', 1)
# print(s.count('1') + s.count('2') * 2)


# s = '>' + '1' * 26 + '2' * 10 + '3' * 14
# while ('>1' in s) or ('>2' in s) or ('>3' in s):
#     if '>1' in s:
#         s = s.replace('>1', '22>', 1)
#     if '>2' in s:
#         s = s.replace('>2', '2>', 1)
#     if '>3' in s:
#         s = s.replace('>3', '1>', 1)
# print(s.count('1') + s.count('2') * 2)


# s = list('7'*40 + '9' * 40 + '4' * 50)
# s = ''.join(s)
# while '49' in s or '97' in s or '47' in s:
#     if '47' in s:
#         s = s.replace('47', '74', 1)
#     elif '97' in s:
#         s = s.replace('97', '79', 1)
#     elif '49' in s:
#         s = s.replace('49', '94', 1)
# print(s[24] + s[70] + s[104])


res = []
for i in range(200, 300):
    a = '1'*i
    while ('1111' in a):
        a = a.replace('1111', '22', 1)
        a = a.replace('222', '1', 1)
    res.append(a.count('1'))
    res.append(i)
print(res)


# for n in range(3, 50):
#     a = '2' + '5'*n
#     while ('25' in a) or ('355' in a) or ('555' in a):
#         if ('25' in a):
#             a = a.replace('25', '5', 1)
#         if ('355' in a):
#             a = a.replace('355', '52', 1)
#         if ('555' in a):
#             a = a.replace('555', '3', 1)
#     if sum(map(int, a)) == 17:
#         print(n)
#         break
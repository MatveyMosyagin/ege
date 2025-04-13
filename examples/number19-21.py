# #Одна куча
# def fu(a, m):
#     if a > 67:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [fu(a + 1, m - 1), fu(a + 4, m - 1), fu(5 * a, m - 1)]
#     if (m - 1) % 2 == 0:
#         return any(h)
#     else:
#         return any(h)
#
# print(19,[s for s in range(1,68) if not fu(s,1) and fu(s,2)])
# print(20,[s for s in range(1,68) if not fu(s,1) and fu(s,3)])
# print(21,[s for s in range(1,68) if not fu(s,2) and fu(s,4)])



#Две кучи
# def fu(a,b,m):
#     if (a+b)>80: return m%2==0
#     if m==0:return 0
#     h = [fu(a+2,b,m-1),fu(a,b+2,m-1),fu(a*2,b,m-1),fu(a,b*2,m-1)]
#     if a < b:
#         h.append(fu(a+1,b,m-1))
#     if a >= b:
#         h.append(fu(a,b+1,m-1))
#     return any(h) if (m-1)%2==0 else any(h) #19 any, 20-21 all
#
# print(19,[s for s in range(1,68) if not fu(12,s,1) and fu(12,s,2)])
# print(20,[s for s in range(1,200) if not fu(s,1) and fu(s,3)])
# print(21,[s for s in range(1,200) if not fu(s,2) and fu(s,4)])


# #Одна куча
# def f(a, m):
#     if a >= 132: return m%2 == 0
#     if m == 0: return 0
#     h = [f(a+3, m-1), f(a+6, m-1), f(a*3, m-1)]
#     return any(h) if (m-1)%2==0 else all(h) # any если сказано после неудачного хода
#
# print(19, [s for s in range(1, 131) if not f(s, 1) and f(s, 2)])
# print(20, [s for s in range(1, 131) if not f(s, 1) and f(s, 3)])
# print(21, [s for s in range(1, 131) if not f(s, 2) and f(s, 4)])



# #Две кучи
# def f(a, b, m):
#     if (a + b) >= 77: return m%2 == 0
#     if m == 0: return 0
#     h = [f(a+3, b, m-1), f(a*3, b, m-1), f(a, b+3, m-1), f(a, b*3, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
# print(19, [s for s in range(1, 65) if not f(12, s, 1) and f(12, s, 2)])
# print(19, [s for s in range(1, 65) if not f(12, s, 1) and f(12, s, 3)])
# print(19, [s for s in range(1, 65) if not f(12, s, 2) and f(12, s, 4)])

P = list(range(69, 92))
Q = list(range(77, 114))
A = [int(i) for i in range(1, 200)]
for x in range(200):
    if not((x in Q) <= (((x in P) == (x in Q)) or (not(x in P) <= (x in A)))):
        A = A[1:]
print(200 - len(A))


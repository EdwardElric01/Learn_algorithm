:
a = [2, 5, 7, 10, 5, 2]
b = [3, 8, 4, 11, 3, 4]


MAX = sum(a)
n = len(a)


F = [[None] * MAX for _ in range(n)]
Y =  [[None] * n for _ in range(MAX)]

for k in range(n):
    F[k][0] = sum(b[:(k+1)])
Y[0] = [0] * n

for x in range(a[0]):
    F[0][x] = b[0]
F[a[0]] = 0

for k in range(n):
    for x in range(1, sum(a[:(k+1)])+1):
        if x < a[k]:
            F[k][x] = F[k-1][x] + b[k]
            Y[x][k] = 1
        else:
            if F[k-1][x-a[k]] > F[k-1][x] + b[k]:
                F[k][x] = F[k-1][x] + b[k]
                Y[x][k] = 1
            else:
                F[k][x] = F[k-1][x-a[k]]
                Y[x][k] = 0


import numpy as np
print(np.array(F))
print(np.array(Y))







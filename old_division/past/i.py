import numpy as np
import sys
n = int(input())
q = int(input())

Q = [list(map(int, input().split())) for _ in range(q)]
S = np.arange(n*n, dtype='int')
A = S.reshape([n, n])

for q in Q:
    if q[0] == 1:
        if q[2] != q[1]:
            A[[q[2]-1, q[1]-1]] = A[[q[1]-1, q[2]-1]]
    elif q[0] == 2:
        if q[2] != q[1]:
            A[:, [q[1]-1, q[2]-1]] = A[:, [q[2]-1, q[1]-1]]
    elif q[0] == 3:
        A = A.T
    elif q[0] == 4:
        print(int(A[q[1]-1][q[2]-1]))

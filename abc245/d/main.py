import numpy as np
n, m = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
A = A[::-1]
C = C[::-1]


A = np.array(A)
C = np.array(C)

a = np.polydiv(C, A)

# print(a)
a = a[0][::-1]
ans = []
for s in a:
    ans.append(int(s))
print(*ans)

# print(time.time()-s)

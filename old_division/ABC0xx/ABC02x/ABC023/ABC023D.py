import numpy as np
n = int(input())
hs = [list(map(int, input().split()))for _ in range(n)]
for i in range(n):
    hs[i] = [hs[i][0]+hs[i][1]*j for j in range(n)]
h = np.asarray(hs)
print(h)

# mada

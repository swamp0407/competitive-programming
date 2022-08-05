from itertools import permutations
import itertools
import numpy as np
import sys
"""read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N, M = map(int, readline().split())
m = map(int, read().split())
ABC = zip(m, m, m)

perms = np.array(list(itertools.permutations(range(N))))

score = np.zeros(len(perms), np.int64)

for a, b, c in ABC:
    score[perms[:, a] < perms[:, b]] += c

answer = score.max()
print(answer)"""


n, m = map(int, input().split())
value = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    value[a][b] = c
ans = 0
for s in permutations(range(n), n):
    num = 0
    for i in range(n-1):
        for j in range(i+1, n):
            num += value[s[i]][s[j]]
    ans = max(ans, num)

print(ans)

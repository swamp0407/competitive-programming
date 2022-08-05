import collections
from numba import jit
n = int(input())
P = list(map(int, input().split()))
S = []
for p in P:
    p = p-1
    a = p % n
    b = p//n
    S.append([b, a])


INF = float('inf')
que = collections.deque([])
block = [[INF]*n for _ in range(n)]
for i in range(n):
    block[0][i] = 0
    block[n-1][i] = 0
    que.append([0, i])
    que.append([n-1, i])

for i in range(1, n-1):
    block[i][0] = 0
    block[i][n-1] = 0
    que.append([i, 0])
    que.append([i, n-1])

while que:
    x, y = que.popleft()
    if x+1 <= n-1 and block[x+1][y] == INF:
        block[x+1][y] = block[x][y]+1
        que.append([x+1, y])
    if x-1 >= 0 and block[x-1][y] == INF:
        block[x-1][y] = block[x][y]+1
        que.append([x-1, y])
    if y+1 <= n-1 and block[x][y+1] == INF:
        block[x][y+1] = block[x][y]+1
        que.append([x, y+1])
    if y-1 >= 0 and block[x][y-1] == INF:
        block[x][y-1] = block[x][y]+1
        que.append([x, y-1])
num = 0
sit = [[1]*n for _ in range(n)]


def bfs(block, sit, xx, yy):
    que = collections.deque([[xx, yy]])
    block[xx][yy] = block[xx][yy]-1
    while que:
        x, y = que.popleft()
        if x+1 <= n-1 and block[x+1][y] > block[x][y]+sit[x+1][y]:
            block[x+1][y] = block[x][y]+sit[x+1][y]
            que.append([x+1, y])
        if x-1 >= 0 and block[x-1][y] > block[x][y]+sit[x-1][y]:
            block[x-1][y] = block[x][y]+sit[x-1][y]
            que.append([x-1, y])
        if y+1 <= n-1 and block[x][y+1] > block[x][y]+sit[x][y+1]:
            block[x][y+1] = block[x][y]+sit[x][y+1]
            que.append([x, y+1])
        if y-1 >= 0 and block[x][y-1] > block[x][y]+sit[x][y-1]:
            block[x][y-1] = block[x][y]+sit[x][y-1]
            que.append([x, y-1])


for x, y in S:
    num += block[x][y]
    sit[x][y] = 0
    bfs(block, sit, x, y)

print(num)

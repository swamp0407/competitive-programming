import collections
n, xxx, yyy = map(int, input().split())

INF = float('inf')

block = [[INF]*403 for _ in range(403)]
for i in range(n):
    xx, yy = map(int, input().split())
    block[xx+201][yy+201] = "#"
que = collections.deque([[0, 0]])
block[0+201][0+201] = 0
while que:
    x, y = que.popleft()
    if x+1+201 <= 402 and y+1+201 <= 402 and block[x+1+201][y+1+201] == INF and block[x+1+201][y+1+201] != "#":
        block[x+1+201][y+1+201] = block[x+201][y+201]+1
        que.append([x+1, y+1])
    if x-1+201 >= -402 and y+1+201 <= 402 and block[x-1+201][y+1+201] == INF and block[x-1+201][y+1+201] != "#":
        block[x-1+201][y+1+201] = block[x+201][y+201]+1
        que.append([x-1, y+1])
    if y+1+201 <= 402 and block[x+201][y+1+201] == INF and block[x+201][y+1+201] != "#":
        block[x+201][y+1+201] = block[x+201][y+201]+1
        que.append([x, y+1])

    if x+1+201 <= 402 and block[x+1+201][y+201] == INF and block[x+1+201][y+201] != "#":
        block[x+1+201][y+201] = block[x+201][y+201]+1
        que.append([x+1, y])
    if x-1+201 >= -402 and block[x-1+201][y+201] == INF and block[x-1+201][y+201] != "#":
        block[x-1+201][y+201] = block[x+201][y+201]+1
        que.append([x-1, y])
    if y-1+201 >= -402 and block[x+201][y-1+201] == INF and block[x+201][y-1+201] != "#":
        block[x+201][y-1+201] = block[x+201][y+201]+1
        que.append([x, y-1])

if block[x+201][y+201] == INF:
    print(-1)
    exit()
print(block[xxx+201][yyy+201])

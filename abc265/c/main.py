###### 2022年 8月21日 日曜日 21時00分20秒 JST ######

h, w = map(int, input().split())

G = [list(input()) for _ in range(h)]
# print(G)
visited = [[False]*w for _ in range(h)]


visited[0][0] = True

stop = False
now = (0, 0)
loop = False
while True:
    i, j = now

    if G[i][j] == "U":
        if i == 0:
            break
        if not visited[i-1][j]:
            visited[i-1][j] = True
            now = (i-1, j)
        else:
            loop = True
            break
    elif G[i][j] == "D":
        if i == h-1:
            break
        if not visited[i+1][j]:
            visited[i+1][j] = True
            now = (i+1, j)
        else:
            loop = True
            break
    elif G[i][j] == "L":
        if j == 0:
            break
        if not visited[i][j-1]:
            visited[i][j-1] = True
            now = (i, j-1)
        else:
            loop = True
            break
    elif G[i][j] == "R":
        if j == w-1:
            break
        if not visited[i][j+1]:
            visited[i][j+1] = True
            now = (i, j+1)
        else:
            loop = True
            break
if loop:
    print(-1)
else:
    x, y = now
    print(x+1, y+1)

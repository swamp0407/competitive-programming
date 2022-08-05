from heapq import heappush, heappop
h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
S = [input() for _ in range(h)]


dx = [-2, -1, 0, 1, 2]
dy = [-2, -1, 0, 1, 2]
dist = [[float("inf")]*w for _ in range(h)]
dist[ch-1][cw-1] = 0
q = [[0, ch-1, cw-1]]

while q:
    d, x, y = heappop(q)
    for ddx in dx:
        for ddy in dy:
            nx = x+ddx
            ny = y+ddy

            if not (0 <= x+ddx <= h-1 and 0 <= y+ddy <= w-1):
                continue
            if ddx == 0 and ddy == 0:
                continue
            if S[nx][ny] == "#":
                continue
            if dist[x][y]+1 > dist[nx][ny]:
                continue
            if ddx == 0 and (ddy == 1 or ddy == -1)and dist[x][y] < dist[nx][ny]:
                dist[nx][ny] = dist[x][y]
                heappush(q, [dist[nx][ny], nx, ny])
            elif (ddx == 1 or ddx == -1) and ddy == 0 and dist[x][y] < dist[nx][ny]:
                dist[nx][ny] = dist[x][y]
                heappush(q, [dist[nx][ny], nx, ny])
            elif dist[nx][ny] > dist[x][y]+1:
                dist[nx][ny] = dist[x][y]+1
                heappush(q, [dist[nx][ny], nx, ny])
if dist[dh-1][dw-1] == float("inf"):
    print(-1)
    exit()
print(dist[dh-1][dw-1])

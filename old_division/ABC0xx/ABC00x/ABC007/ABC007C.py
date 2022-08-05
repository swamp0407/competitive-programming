from collections import deque
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

block = [list(input()) for _ in range(r)]

q = deque([[sy-1, sx-1]])
block[sy-1][sx-1] = 0
while not [gy-1, gx-1] in q:
    y, x = q.popleft()
    for dy, dx in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        if block[y+dy][x+dx] == ".":
            q.append([y+dy, x+dx])
            block[y+dy][x+dx] = block[y][x]+1
print(block[gy-1][gx-1])

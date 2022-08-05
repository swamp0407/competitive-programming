from collections import deque
h, w = map(int, input().split())
block = [list(map(str, input())) for _ in range(h)]
num = 0
for i in block:
    num += i.count(".")
block[0][0] = 0
q = deque([[0, 0]])
while q:
    y, x = q.popleft()
    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if y+dy >= 0 and y+dy < h and x+dx >= 0 and x+dx < w:
            if block[y+dy][x+dx] == ".":
                q.append([y+dy, x+dx])
                block[y+dy][x+dx] = block[y][x]+1

if block[h-1][w-1] == ".":
    print(-1)
else:
    print(num-block[h-1][w-1]-1)

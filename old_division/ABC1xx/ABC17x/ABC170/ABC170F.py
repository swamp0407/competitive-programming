from collections import deque
h, w, k = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
#block = [list(input()) for _ in range(h)]
block = []
for i in range(h):
    l = list(input())
    block.append([float("inf") if i == "." else i for i in l])
migi = 0
hidari = 1
ue = 2
sita = 3
q = deque()
q.append([x1-1, y1-1, 6, 1])
block[x1-1][y1-1] = 0
while q:
    xx, yy, houkou, kaisuu = q.popleft()
    if xx+1 <= h-1 and block[xx+1][yy] != "@":
        if houkou == sita and kaisuu < k and block[xx+1][yy] > block[xx][yy]:
            block[xx+1][yy] = block[xx][yy]
            q.append([xx+1, yy, sita, kaisuu+1])
        elif block[xx+1][yy] >= block[xx][yy]+1:
            block[xx+1][yy] = block[xx][yy]+1
            q.append([xx+1, yy, sita, 1])
    if xx-1 >= 0 and block[xx-1][yy] != "@":
        if houkou == ue and kaisuu < k and block[xx-1][yy] > block[xx][yy]:
            block[xx-1][yy] = block[xx][yy]
            q.append([xx-1, yy, ue, kaisuu+1])
        elif block[xx-1][yy] >= block[xx][yy]+1:
            block[xx-1][yy] = block[xx][yy]+1
            q.append([xx-1, yy, ue, 1])
    if yy+1 <= w-1 and block[xx][yy+1] != "@":
        if houkou == migi and kaisuu < k and block[xx][yy+1] > block[xx][yy]:
            block[xx][yy+1] = block[xx][yy]
            q.append([xx, yy+1, migi, kaisuu+1])
        elif block[xx][yy+1] >= block[xx][yy]+1:
            block[xx][yy+1] = block[xx][yy]+1
            q.append([xx, yy+1, migi, 1])
    if yy-1 >= 0 and block[xx][yy-1] != "@":
        if houkou == hidari and kaisuu < k and block[xx][yy-1] > block[xx][yy]:
            block[xx][yy-1] = block[xx][yy]
            q.append([xx, yy-1, hidari, kaisuu+1])
        elif block[xx][yy-1] >= block[xx][yy]+1:
            block[xx][yy-1] = block[xx][yy]+1
            q.append([xx, yy-1, hidari, 1])
if block[x2-1][y2-1] == float("inf"):
    print(-1)
else:
    print(block[x2-1][y2-1])

###### 2022年 8月21日 日曜日 21時00分20秒 JST ######
from collections import deque
n, m = map(int, input().split())

a, b, cc, d, e, f = map(int, input().split())
block = {}
for i in range(m):
    x, y = map(int, input().split())
    block[(x, y)] = 1

# print(block)
mod = 998244353
# 302C2

q = deque()
q.append((0, 0, 1))
for i in range(n):
    next_dict = {}
    while q:
        x, y, c = q.pop()
        for dx, dy in [(a, b), (cc, d), (e, f)]:
            nx = x + dx
            ny = y + dy
            if (nx, ny) in block:
                continue
            if next_dict.get((nx, ny)):
                next_dict[(nx, ny)] = (next_dict[(nx, ny)] + c) % mod
            else:
                next_dict[(nx, ny)] = c
    for nx, ny in next_dict:
        q.append((nx, ny, next_dict[(nx, ny)]))
    # print(len(q))
ans = 0
while q:
    x, y, c = q.pop()
    ans = (ans + c) % mod

print(ans)

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

# q = deque()
# q.append((0, 0, 1))
dp = [[[0] * (n+1) for __ in range(n+1)] for _ in range(n+1)]

dp[0][0][0] = 1
# print(dp)
for i in range(n):
    for n_a in range(i+1):
        for n_b in range(i+1):
            n_c = i - n_a - n_b
            if n_c < 0:
                continue
            x = a * n_a + cc * n_b + e * n_c
            y = b * n_a + d * n_b + f * n_c
            if (x, y) in block:
                continue
            if not (x+a, y+b) in block:
                dp[i+1][n_a+1][n_b] += dp[i][n_a][n_b]
            if not (x+cc, y+d) in block:
                dp[i+1][n_a][n_b+1] += dp[i][n_a][n_b]
            if not (x+e, y+f) in block:
                dp[i+1][n_a][n_b] += dp[i][n_a][n_b]


ans = 0
for n_a in range(n+1):
    for n_b in range(n+1):
        ans += dp[n][n_a][n_b]
        ans %= mod
print(ans)

#
# for i in range(n):
#     next_dict = {}
#     while q:
#         x, y, c = q.pop()
#         for dx, dy in [(a, b), (cc, d), (e, f)]:
#             nx = x + dx
#             ny = y + dy
#             if (nx, ny) in block:
#                 continue
#             if next_dict.get((nx, ny)):
#                 next_dict[(nx, ny)] = (next_dict[(nx, ny)] + c) % mod
#             else:
#                 next_dict[(nx, ny)] = c
#     for nx, ny in next_dict:
#         q.append((nx, ny, next_dict[(nx, ny)]))
#     # print(len(q))
# ans = 0
# while q:
#     x, y, c = q.pop()
#     ans = (ans + c) % mod

# print(ans)

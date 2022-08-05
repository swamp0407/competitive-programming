from collections import deque
h, w = map(int, input().split())
l = [input() for _ in range(h)]
l[0][0]
mod = 10**9+7
dp = [[0]*w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w-1):
        if j == 0:
            dp[i][j] = 1
        dp[i+1][j+1] = (dp[i][j+1]+dp[i+1][j]) % mod

print(dp[h*w-1])

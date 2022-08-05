mod = 998244353
n, s = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0]*(3001) for _ in range(n+1)]

dp[0][0] = 1

for i in range(n):
    for j in range(s+1):
        dp[i+1][j] = 2*dp[i][j] % mod
        if j-A[i] >= 0:
            dp[i+1][j] = (dp[i+1][j]+dp[i][j-A[i]]) % mod

print(dp[n][s])

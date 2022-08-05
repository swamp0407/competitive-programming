""" n, m = map(int, input().split())
d = [int(input())for _ in range(n)]
c = [int(input()) for _ in range(m)]

dp = [[0]*(m+1) for _ in range(n+1)]  # dp[i][j] 都市iにj日目にいるときの最低の疲労度
sum = 0
for i in range(1, n+1):
    dp[i][i] = dp[i-1][i-1]+c[i-1]*d[i-1]


for i in range(n):
    for j in range(i+1, m):
        dp[i+1][j+1] = min(dp[i+1][j], dp[i][j]+c[j]*d[i])
mod = 10**9+7
print(dp[n][m]) """

n, m = map(int, input().split())
d = [int(input())for _ in range(n)]
c = [int(input()) for _ in range(m)]
dp = [[10**10]*(m+1) for _ in range(n+1)]
for i in range(m+1):
    dp[0][i] = 0
for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = min(dp[i+1][j], dp[i][j]+c[j]*d[i])
print(dp[n][m])

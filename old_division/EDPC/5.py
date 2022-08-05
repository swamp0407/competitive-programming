n, w = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(n)]

dp = [[float("inf")]*(10**5+10) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 0
for i in range(n):
    for j in range(10**5+10):
        if j >= item[i][1]:
            dp[i+1][j] = min(dp[i][j], dp[i][j-item[i][1]]+item[i][0])
        else:
            dp[i+1][j] = dp[i][j]
ans = 0
for i in range(10**5+10):
    if dp[n][i] <= w:
        ans = i

print(ans)

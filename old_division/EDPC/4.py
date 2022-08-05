n, w = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(n):
    for j in range(w+1):
        if j >= item[i][0]:
            dp[i+1][j] = max(dp[i][j], dp[i][j-item[i][0]]+item[i][1])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[n][w])

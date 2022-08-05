n = int(input())
dp = [[0]*3 for _ in range(n)]
a, b, c = map(int, input().split())
dp[0][0] = a
dp[0][1] = b
dp[0][2] = c
for i in range(n-1):
    a, b, c = map(int, input().split())
    dp[i+1][0] = max(dp[i][1]+a, dp[i][2]+a)
    dp[i+1][1] = max(dp[i][0]+b, dp[i][2]+b)
    dp[i+1][2] = max(dp[i][0]+c, dp[i][1]+c)


print(max(dp[n-1]))

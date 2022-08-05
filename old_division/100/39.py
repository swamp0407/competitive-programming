n = int(input())
a = list(map(int, input().split()))
d = 21
dp = [[0]*d for i in range(n-1)]

dp[0][a[0]] = 1
for i in range(n-2):
    for j in range(d):
        if j+a[i+1] < d:
            dp[i+1][j+a[i+1]] += dp[i][j]
        if j-a[i+1] >= 0:
            dp[i+1][j-a[i+1]] += dp[i][j]

print(dp[n-2][a[n-1]])

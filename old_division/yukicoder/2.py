n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(a[0])
    exit()
dp = [[0]*2 for i in range(n)]

dp[0][0] = 0
dp[0][1] = a[0]
dp[1][0] = a[0]
dp[1][1] = a[1]

for i in range(2, n):
    dp[i][0] = max(dp[i-1][1], dp[i-2][1])
    dp[i][1] = max(dp[i-1][0], dp[i-2][0])+a[i]

print(max(dp[n-1][0], dp[n-1][1]))

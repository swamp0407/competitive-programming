n, k = map(int, input().split())
# 2237
H = list(map(int, input().split()))


dp = [float("inf")]*(n+2)
dp[0] = 0
for i in range(n):
    for j in range(1, k+1):
        if i+j >= n:
            break
        dp[i+j] = min(dp[i+j], dp[i]+abs(H[i]-H[i+j]))

print(dp[n-1])

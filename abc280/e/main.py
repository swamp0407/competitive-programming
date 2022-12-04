###### 2022年 12月 4日 日曜日 11時22分58秒 JST ######


n, p = map(int, input().split())

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 1

MOD = 998244353

inv100 = pow(100, MOD - 2, MOD)

p *= inv100

for i in range(2, n+1):
    dp[i] = (dp[i-2] * p + dp[i-1] * (1 - p)+1) % MOD


print(dp[n])

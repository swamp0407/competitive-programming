n, l = map(int, input().split())
x = list(map(int, input().split()))
t1, t2, t3 = map(int, input().split())

dp = [float("inf")]*(l+4)
X = [False]*(l+10)
for xx in x:
    X[xx] = True
dp[0] = 0

for i in range(l):
    dp[i+1] = min(dp[i+1], dp[i]+t1+(t3 if X[i] else 0))
    dp[i+2] = min(dp[i+2], dp[i]+t1+t2+(t3 if X[i] else 0))
    dp[i+4] = min(dp[i+4], dp[i]+t1+3*t2+(t3 if X[i] else 0))
print(int(min(dp[l], dp[l+1]-0.5*t1-0.5*t2, dp[l+2]-0.5*t1-1.5*t2)))

n = int(input())

W = list(map(int, input().split()))
W.sort()

s = sum(W)
if s % 2 == 1:
    print("impossible")
    exit()
ss = s//2
dp = [[False]*(s+1) for _ in range(n)]
for i in range(n):
    dp[i][0] = True
dp[0][W[0]] = True
for i in range(n-1):
    for j in range(ss+1):
        if j >= W[i+1]:
            dp[i+1][j] = dp[i][j-W[i+1]]
        if dp[i][j]:
            dp[i+1][j] = True

for i in range(n):
    if dp[i][ss]:
        print("possible")
        exit()
print("impossible")

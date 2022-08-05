a = input()
b = input()
na = len(a)
nb = len(b)

dp = [[0]*(nb+1) for _ in range(na+1)]

for i in range(na):
    for j in range(nb):
        if a[i] == b[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
ans = []
num = dp[na][nb]
x = na
y = nb
while num:
    if dp[x][y] == dp[x-1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y-1]:
        y -= 1
    else:
        ans.append(a[x-1])
        x -= 1
        y -= 1
        num -= 1

print("".join(ans[::-1]))

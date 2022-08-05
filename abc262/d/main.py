###### 2022年 7月31日 日曜日 21時00分22秒 JST ######
nn = int(input())
A = list(map(int, input().split()))

ans = 0


def solve(n):
    dp = [[[0 for ___ in range(n)] for __ in range(nn)]
          for _ in range(n)]  # i j a
    tempA = [a % n for a in A]
    tempA.sort()
    ret = 0
    print(tempA)
    print(dp)
    for i in range(n):
        if i == 0:
            for j, a in enumerate(tempA):
                dp[0][j][a] += 1
            continue
        for k in range(nn):
            for j, a in enumerate(tempA[k+1:]):
                for l in range(n):
                    dp[i][k+j][(l+a) % n] += dp[i-1][k][l]
    for i, ddp in enumerate(dp[n-1]):
        for j, d in enumerate(ddp):

            ret += d
    print(dp)
    print(ret/n, "ret//n")
    return ret//n


for i in range(1, nn+1):
    ans += solve(i)


print(ans)

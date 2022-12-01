###### 2022年 10月31日 月曜日 13時29分28秒 JST ######


n, m = map(int, input().split())

A = list(map(int, input().split()))


# dp[i][j][k] := i番目までの数字を使って総和がj 最後の数字を加えたとき1 そうでないとき0のときの操作の回数の最小値

# dp = [[[float("inf")]*(2) for _ in range(3010)] for _ in range(n+1)]

d0 = [float("inf")]*(3010)
d1 = [float("inf")]*(3010)

# for i in range(n+1):
# dp[0][0][1] = 0
d0[0] = 1
d1[A[0]] = 0
for i in range(1, n):
    for j in range(3009, -1, -1):
        for k in range(2):
            if k == 0:
                d0[j] = min(d0[j], d1[j]+1)
            else:
                if j-A[i] >= 0:
                    d1[j] = min(d0[j-A[i]], d1[j-A[i]])
                else:
                    d1[j] = float("inf")
for i in range(1, m+1):
    ans = min(d0[i], d1[i])
    print(ans if ans != float("inf") else -1)

###### 2023年 1月 6日 金曜日 08時03分10秒 JST ######
from bisect import bisect

n = int(input())


# N: 数列の長さ
# A[i]: a_i の値
def LIS(N, A):
    INF = 10**10

    dp = [INF]*(N+1)
    dp[0] = -A[0]
    for a in A[1:]:
        a = -a
        # idx = bisect(dp, a) #広義最長増加部分列
        idx = bisect(dp, a)
        dp[idx] = a
        # print(dp)
    return max(i for i in range(N+1) if dp[i] < INF)+1


A = [int(input()) for i in range(n)]

ans = LIS(n, A)
print(ans)

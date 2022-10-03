###### 2022年 10月 2日 日曜日 21時00分08秒 JST ######

n = int(input())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

C = [(A[i], B[i]) for i in range(n)]

C.sort()

# print(C)

D = [C[i][0] for i in range(n)]
E = [C[i][1] for i in range(n)]

# print(D)
# print(E)

from bisect import bisect


# N: 数列の長さ
# A[i]: a_i の値
def LIS(N, A):
    INF = 10**10

    dp = [INF]*(N+1)
    dp[0] = -1
    for a in A:
        #idx = bisect(dp, a) #広義最長増加部分列
        idx = bisect(dp, a-1)
        dp[idx] = min(a, dp[idx])
    return max(i for i in range(N+1) if dp[i] < INF)

print(LIS(n, E)+n)

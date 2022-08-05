N = int(input())
A = list(map(int, input().split()))
INF = float('inf')


def check(x):
    X = []
    for a in A:
        X.append(a - x)
    dp = [0] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        if i == 1:
            dp[i] = X[i - 1] + dp[i - 1]
        else:
            dp[i] = X[i - 1] + max(dp[i - 1], dp[i - 2])
    return max(dp[-1], dp[-2]) >= 0


ok, ng = 0, 10 ** 10
while ng - ok > 10 ** -6:
    mid = (ok + ng) / 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)


def check(x):
    X = []
    for a in A:
        if a < x:
            X.append(-1)
        else:
            X.append(1)
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        if i == 1:
            dp[i] = X[i - 1] + dp[i - 1]
        else:
            dp[i] = X[i - 1] + max(dp[i - 1], dp[i - 2])
    return max(dp[-1], dp[-2]) > 0


ok, ng = 0, 10 ** 10
while ok + 1 < ng:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)

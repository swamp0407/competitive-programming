n, m, k = map(int, input().split())
mod = 10**9+7
p = [0]*(m+1)
q = [0]*(m+1)
c = [0]*(m+1)
graph = [[] for _ in range(300+1)]
for i in range(m):
    u, v, c = map(int, input().split())
    graph[u].append([v, c])

dp = [[0]*(n+1) for _ in range(301)]


for i in range(1, n+1):
    for j in range(301):
        for g in graph[j]:
            dp[i+1][j+g[1]][g[0]] = dp[i+1][j]+dp[i][][]


for i in range(m):
    a, b, c = map(int, input().split())
    p[i] = a
    q[i] = b
    c[i] = c

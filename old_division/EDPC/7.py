from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
deg = [0]*(n+1)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    deg[v] += 1
q = deque()

for i in range(1, n+1):
    if deg[i] == 0:
        q.append(i)

dp = [0]*(n+1)
while q:
    n = q.popleft()
    for s in graph[n]:
        deg[s] -= 1
        if deg[s] == 0:
            q.append(s)
            dp[s] = dp[n]+1

print(max(dp))

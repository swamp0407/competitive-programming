from collections import defaultdict
n, m = map(int, input().split())

for i in range(m):
    u, v = map(int, input().split())


graph = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

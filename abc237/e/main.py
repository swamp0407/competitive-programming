n, m = map(int, input().split())
H = list(map(int, input().split()))

graph = [[] for _ in range(n)]


for i in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    if H[u] <= H[v]:
        graph[v].append((H[v]-H[u], u))
        graph[u].append((-2*(H[v]-H[u]), v))
    else:
        graph[v].append((-2*(H[u]-H[v]), u))
        graph[u].append(((H[u]-H[v]), v))

# print(graph)

cost = [-float("inf")]*n
cost[0] = 0
q = [0]
info = [0]*n
while q:
    c = q.pop()
    for v in graph[c]:
        cos, next = v
        if cost[c]+cos > cost[next]:
            q.append(next)
            # info[c] = 1
            cost[next] = cost[c]+cos


print(max(cost))

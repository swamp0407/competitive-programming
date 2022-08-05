import heapq
n, k = map(int, input().split())


C = []
R = []
for i in range(n):
    c, r = map(int, input().split())
    C.append(c)
    R.append(r)


graph = [[]*(n+1) for _ in range(n+1)]
for i in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = []
cost = [float("inf")]*(n+1)
cost[1] = 0
heapq.heappush(q, 1)
while q:
    s = heapq.heappop(q)
    for l in graph[s]:
        if cost[l] > cost[s]+dist
あきらめ

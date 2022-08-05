import heapq
n, k = map(int, input().split())


def dijkstra(s, e):
    dist = [float("inf")]*(n+1)
    dist[s] = 0
    q = []
    heapq.heappush(q, s)

    while q:
        a = heapq.heappop(q)
        for i, m in graph[a]:
            if dist[a]+i < dist[m]:
                dist[m] = dist[a]+i
                heapq.heappush(q, m)
    if dist[e] == float("inf"):
        print(-1)
    else:
        print(dist[e])


l = []
graph = [[]for _ in range(n+1)]

for i in range(k):
    A = list(map(int, input().split()))
    if A[0] == 1:
        q, w, e, r = A
        graph[w].append([r, e])
        graph[e].append([r, w])
    else:
        q, w, e = A
        dijkstra(w, e)

import collections
v, e, r = map(int, input().split())

graph = [[]*v for _ in range(v)]

for i in range(e):
    s, t, d = map(int, input().split())
    graph[s].append([t, d])


q = collections.deque()
dist = [float("inf")]*v
dist[r] = 0
q.append([0, r])

while q:
    d, s = q.popleft()
    if d > dist[s]:
        continue
    for ss, dd in graph[s]:
        if dist[ss] > dist[s]+dd:
            dist[ss] = dist[s]+dd
            q.append([dist[ss], ss])

for i in dist:
    if i == float("inf"):
        print("INF")
    else:
        print(i)

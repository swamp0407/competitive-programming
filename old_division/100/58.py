# 1857

from collections import deque
n, k, m, s = map(int, input().split())
p, q = map(int, input().split())
C = []
for i in range(k):
    c = int(input())
    C.append(c)


graph = [[]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

safe = [float("inf")]*(n+1)
for c in C:
    safe[c] = -1
    for l in graph[c]:
        safe[l] = -1


def bfs(s, n):
    q = deque(s)
    safe[s] = 0
    while q:
        l = q.popleft()
        for ll in graph[l]:
            if safe[ll] == float("inf"):
                safe[ll] = safe[l]+1
                q.append(ll)

# 諦め実装が大変そう

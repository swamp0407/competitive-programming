###### 2022年 8月13日 土曜日 21時00分23秒 JST ######

from copy import copy
import itertools
from collections import defaultdict
from collections import deque
s = input()

dist = defaultdict(int)


def bfs(dist, goal):
    queue = deque()
    queue.append("atcoder")
    while queue:
        s = queue.popleft()
        if s == goal:
            return dist[s]
        for to in graph[s]:
            if dist[to] != -1:
                continue
            dist[to] = dist[s] + 1
            queue.append(to)


# N, M = map(int, input().split())
graph = {}
dist = {}
for a in itertools.permutations(list("atcoder")):
    graph["".join(a)] = []
    for b in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]:
        c = list(a)
        c[b[0]], c[b[1]] = c[b[1]], c[b[0]]
        graph["".join(a)].append("".join(c))
        dist["".join(c)] = -1
# print(graph)
# for i in range(M):
#     a, b = map(int, input().split())
#     a, b = a-1, b-1
#     graph[a].append(b)
#     graph[b].append(a)
dist["atcoder"] = 0

ans = bfs(dist, s)
print(ans)

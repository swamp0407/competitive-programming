###### 2022年 11月12日 土曜日 21時00分18秒 JST ######
from collections import *
from collections import defaultdict, deque

n = int(input())


graph = defaultdict(list)
for i in range(n):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    graph[u].append(v)
    graph[v].append(u)


nax = 0


def bfs(dist):
    global nax
    queue = deque()
    queue.append(0)
    while queue:
        s = queue.popleft()
        for to in graph[s]:
            if dist.get(to):
                continue
            if nax < to:
                nax = to
            dist[to] = 1
            queue.append(to)


dist = {}
dist[0] = 0
bfs(dist)

print(nax+1)

###### 2022年 11月12日 土曜日 21時00分18秒 JST ######
from collections import defaultdict, deque

n, m, k = map(int, input().split())


graph0 = [[] for _ in range(n)]
graph1 = [[] for _ in range(n)]

v_graph = [[] for _ in range(n)]


dist = defaultdict(lambda: -1)


for i in range(m):
    u, v, a = map(int, input().split())
    if a:
        graph1[u-1].append(v-1)
        graph1[v-1].append(u-1)
    else:
        graph0[u-1].append(v-1)
        graph0[v-1].append(u-1)
S = list(map(int, input().split()))

S_dict = {s: i for i, s in enumerate(S)}


def bfs(dist):
    queue = deque()
    dist[(0, 1)] = 0
    queue.append((0, 1))
    while queue:
        s, a = queue.popleft()
        if s == n-1:
            print(dist[(s, a)])
            exit()
        if a:
            for to in graph1[s]:
                if dist[(to, 1)] != -1:
                    continue
                dist[(to, 1)] = dist[(s, 1)] + 1
                queue.append((to, 1))
        else:
            for to in graph0[s]:
                if dist[(to, 0)] != -1:
                    continue
                dist[(to, 0)] = dist[(s, 0)] + 1
                queue.append((to, 0))

        if S_dict.get(s+1) is not None:
            aa = 1-a
            if dist[(s, aa)] != -1:
                continue
            dist[(s, aa)] = dist[(s, a)]
            queue.appendleft((s, aa))
    print(-1)
    exit()


bfs(dist)

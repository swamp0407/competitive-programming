from heapq import *
INF = float('INF')

n, k = map(int, input().split())
graph = [[] for _ in range(n+1)]


def f(s, e):  # 島sから出て島eまで行く最安値
    cost_all = [INF] * (n+1)
    cost_all[s] = 0
    q = []
    heappush(q, s)
    while q:
        t = heappop(q)
        for c, i in graph[t]:
            if(cost_all[t] + c < cost_all[i]):
                cost_all[i] = cost_all[t] + c
                heappush(q, i)
    if(cost_all[e] == INF):
        return -1
    else:
        return cost_all[e]


for i in range(k):
    x = list(map(int, input().split()))
    if(x[0] == 1):
        a = x[1]
        b = x[2]
        cost = x[3]
        graph[a].append([cost, b])
        graph[b].append([cost, a])
    else:
        print(f(x[1], x[2]))

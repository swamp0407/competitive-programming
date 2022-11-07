###### 2022年 11月 7日 月曜日 11時55分00秒 JST ######

# 参考 https://atcoder.jp/contests/arc150/submissions/36027403

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1; v -= 1

    adj[u].append(v)
    adj[v].append(u)

from collections import deque

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dist = [K + 1] * N

if A[0] == B[0]:
    dist[0] = 1
else:
    dist[0] = 0

# vis = [False] * N
q = deque([0])


while q:
    v = q.popleft()

    # if vis[v]:
        # continue
    # vis[v] = True
    if dist[v] >= K:
        continue


    c = dist[v]
    for u in adj[v]:
        if A[u] == B[c] and dist[u] > c + 1:
            dist[u] = c + 1
            q.append(u)
        elif A[u] != B[c] and dist[u] > c:
            dist[u] = c
            q.appendleft(u)

if dist[N - 1] >= K:
    print('Yes')
else:
    print('No')



# from collections import deque


# def bfs_01(s):
#     que = deque([s])
#     while que:
#         s = que.popleft()
#         for to, w in edges[s]:
#             d = dist[i] + w
#             if d < dist[to]:
#                 dist[to] = d
#                 if w == 1:
#                     que.append(to)
#                 else:
#                     que.appendleft(to)

# # 頂点数N、始点の頂点番号s
# N, s = map(int, input().split())
# # 隣接リスト。
# # edges[i]の要素に(j, c)が含まれる時、iからjにコストcの辺が存在
# edges = [[] for i in range(N)]

# dist = [10**9]*N
# dist[s] = 0
# bfs_01(s)

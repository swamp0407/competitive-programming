from collections import deque, defaultdict
n = int(input())


T = [0] * n
K = [-1]*n
ab = []
graph = [[]for _ in range(n)]
for i in range(n):
    t, k, *A = list(map(int, input().split()))
    # print(t, k)
    T[i] = t
    K[i] = k
    graph[i] = [a-1 for a in A]

# print(graph)
visit = defaultdict(int)

queue = [n-1]

in_cnt = defaultdict(int)
outs = defaultdict(list)
for a, b in ab:
    in_cnt[b] += 1
    outs[a].append(b)

res = []
while len(queue) != 0:
    v = queue.pop()
    res.append(v)
    for v2 in graph[v]:
        if visit[v2] == 0:
            visit[v2] == 1
            queue.append(v2)


# print(res)
ans = 0
for r in res:
    ans += T[r]

print(ans)

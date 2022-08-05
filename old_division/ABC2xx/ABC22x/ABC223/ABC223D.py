from collections import defaultdict
from heapq import heapify, heappop, heappush
# n, m = map(int, input().split())


# graph = [[] for _ in range(n)]

# for i in range(m):
#     a, b = map(int, input().split())
#     graph[b]


v, n = map(int, input().split())
es = [[int(x) for x in input().split()] for _ in range(n)]

outs = defaultdict(list)
ins = defaultdict(int)
for v1, v2 in es:
    outs[v1].append(v2)
    ins[v2] += 1

q = [v1 for v1 in range(1, v+1) if ins[v1] == 0]
heapify(q)
res = []
while q:
    v1 = heappop(q)
    res.append(v1)
    for v2 in outs[v1]:
        ins[v2] -= 1
        if ins[v2] == 0:
            heappush(q, v2)

if len(res) != v:
    print(-1)
else:
    print(*res)

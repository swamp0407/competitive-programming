import sys
input = sys.stdin.readline
N = int(input())
sys.setrecursionlimit(300000)

G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


T = [[] for _ in range(N)]
visited = [False] * N
stack = [0]
visited[0] = True

nodes = []
while stack:
    node = stack.pop()
    nodes.append(node)
    for next_ in G[node]:
        if visited[next_]:
            continue
        visited[next_] = True
        stack.append(next_)
        T[node].append(next_)

top_20s = [[] for _ in range(N)]
counts = 1
for node in reversed(nodes):
    top = []
    for child in T[node]:
        top.extend(top_20s[child])
    if top == []:
        top_20s[node] = [counts, counts]
        counts += 1
    else:
        top.sort(reverse=True)
        top_20s[node] = [top[-1], top[0]]


for i in range(N):
    print(*top_20s[i])

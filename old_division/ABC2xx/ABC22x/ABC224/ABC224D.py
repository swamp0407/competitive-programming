m = int(input())

UV = [list(map(int, input().split())) for _ in range(m)]
P = list(map(int, input().split()))

goal = [8]*9

for i, p in enumerate(P):
    goal[p-1] = i
# print(goal)

start = [i for i in range(9)]
# print(start)

graph = [[] for _ in range(9)]
for u, v in UV:
    u = u-1
    v = v-1
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
q = []
q.append((start[::], 8, 0))

space = 8


def bf_search(q, start, space):

    table = {}
    table[tuple(start)] = True
    while q:
        a, space, count = q.popleft()
        for x in graph[space]:
            b = a
            b[space] = b[x]
            b[x] = 8
            key = tuple(b)
            if key in table:
                continue
            if b == goal:
                print(count+1)
                return
            q.append((b, x, count+1))
            table[key] = True
    print(-1)
    exit()


if start == goal:
    print(0)
    exit()
bf_search(q, start, 8)

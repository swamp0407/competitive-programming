import sys
input = sys.stdin.readline
n = int(input())
sys.setrecursionlimit(300000)

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    # a = i
    # b = a+1
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
subtree_value = [[] for _ in range(n)]
counts = 1


def dfs(curr):
    global counts
    visited[curr] = True
    val = []
    for node in graph[curr]:
        if not visited[node]:
            val += dfs(node)
            if len(val) > 20:
                val.sort()
                val = [val[0], val[-1]]

    if val == []:
        subtree_value[curr] = [counts, counts]
        counts += 1
        return subtree_value[curr]
    else:
        val.sort()
    subtree_value[curr] = [val[0], val[-1]]
    return subtree_value[curr]


A = []
A.sort()


dfs(0)
for i in range(n):
    print(*subtree_value[i])

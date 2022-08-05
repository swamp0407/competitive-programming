h, w = map(int, input().split())

graph = [list(input()) for _ in range(h)]


def solve(graph, i, j):
    d = {"1", "2", "3", "4", "5"}
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x = i+dx
        y = j+dy

        if 0 <= x and x <= h-1 and 0 <= y and y <= w-1:
            d.discard(graph[x][y])
    return d.pop()


for i in range(h):
    for j in range(w):
        if graph[i][j] == ".":
            graph[i][j] = solve(graph, i, j)

for a in graph:
    print(*a, sep="")

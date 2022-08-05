n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())


graph = [["." for __ in range(s-r+1)] for _ in range(q-p+1)]


for i in range(s-r+1):
    for j in range(q-p+1):
        y = i + r
        x = j + p

        if y == -x+a+b or y == x-a+b:
            graph[j][i] = "#"

for l in graph:
    print("".join(l))

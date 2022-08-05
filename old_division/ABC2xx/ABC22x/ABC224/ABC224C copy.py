from itertools import combinations
n = int(input())


X = [list(map(int, input().split())) for _ in range(n)]


d = combinations(range(n), 3)

ans = 0
for a, b, c in d:
    x1, y1 = X[a]
    x2, y2 = X[b]
    x3, y3 = X[c]

    if (x2-x1)*(y3-y2) == (x3-x2)*(y2-y1):
        continue
    ans += 1

print(ans)

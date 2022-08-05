# 人のを参考に1回自分で書いた(初E)


def find(x):
    if x == par[x]:
        return x
    par[x] = find(par[x])
    return par[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    par[y] = x


n, m = map(int, input().split())
par = {i: i for i in range(1, n+1)}
for _ in range(1, m+1):
    x, y, z = map(int, input().split())
    union(x, y)

print(sum([1 for i in range(1, n+1) if par[i] == i]))

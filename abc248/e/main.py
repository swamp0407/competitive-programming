from collections import defaultdict
from operator import mul
from functools import reduce
n, K = map(int, input().split())
XY = []
for i in range(n):
    x, y = map(int, input().split())
    XY.append((x, y))

XY.sort()


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


if K == 1:
    print("Infinity")
    exit()
# elif K == 2:
#     d = combinations_count(n, 2)
#     print(d)
#     exit()
# else:


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


'''
uf = UnionFind(N) -> create 6 separated nodes
uf.union(0, 2) -> unite two ids
uf.same(0, 2) -> have same top node?
uf.find(0) -> id of top node
uf.size(5) -> num of group

# 文字列や任意の数字を要素にしたり復元したい場合
l = ['A', 'B', 'C', 'D', 'E']

# {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
d = {x: i for i, x in enumerate(l)}

# {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
d_inv = {i: x for i, x in enumerate(l)}

uf.union(d['A'], d['D'])
print(d_inv[uf.find(d['D'])])
# A
'''


def cul(i, j):
    return i+j*n


uf = UnionFind(combinations_count(n, 2))
# uf.union(0, 2) -> unite two ids
# uf.same(0, 2) -> have same top node?
# uf.find(0) -> id of top node
# uf.size(5) -> num of group


for i in range(n):
    for j in range(j+1, i):
        for k in range(k+1j):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            x3, y3 = XY[k]
            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3
            if x1 * y2 == x2 * y1:
                uf.union(cul(i, j), cul(j, k))
                uf.union(cul(i, j), cul(i, k))


# print(uf)
ans = 0
for i in uf.all_group_members().values():
    if len(i) >= combinations_count(K, 2):
        ans += 1


if K == 2:
    print(ans)
    exit()
print(ans)

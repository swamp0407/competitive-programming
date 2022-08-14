###### 2022年 8月13日 土曜日 21時00分23秒 JST ######

from collections import defaultdict
n, m, e = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(e)]

q = int(input())

X = [int(input()) for _ in range(q)]
d = set(range(1, e+1)) - set(X)


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


uf = UnionFind(n+m)

graph = [[] for _ in range(n+m)]
for i in d:
    u, v = UV[i-1]
    uf.union(u-1, v-1)

parents = set()
for i in range(1, m+1):
    parents.add(uf.find(n+i-1))

c = -m
for p in parents:
    c += uf.size(p)
rAns = []
rAns.append(c)
for x in X[::-1]:
    u, v = UV[x-1]
    if uf.find(u-1) == uf.find(v-1):
        if uf.find(u-1) in parents:
            pass
    elif uf.find(u-1) in parents and uf.find(v-1) in parents:
        parents.remove(uf.find(u-1))
        parents.remove(uf.find(v-1))
        uf.union(u-1, v-1)
        parents.add(uf.find(v-1))
    elif uf.find(u-1) in parents and uf.find(v-1) not in parents:
        c += uf.size(v-1)
        parents.remove(uf.find(u-1))
        uf.union(u-1, v-1)
        parents.add(uf.find(v-1))

    elif uf.find(u-1) not in parents and uf.find(v-1) in parents:
        c += uf.size(u-1)
        parents.remove(uf.find(v-1))
        uf.union(u-1, v-1)
        parents.add(uf.find(v-1))

    uf.union(u-1, v-1)

    rAns.append(c)

for i in rAns[::-1][1:]:
    print(i)

from collections import defaultdict
n, m = map(int, input().split())


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
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


A = []
B = []
graph = [[] for _ in range(n)]
uf = UnionFind(n)
d = {}
for i in range(m):
    a, b = map(int, input().split())
    d[(a, b)] = 1

for a, b in d.keys():
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    if uf.find(a-1) == uf.find(b-1):
        print("No")
        exit()
    uf.union(a-1, b-1)
ok = 0
for row in graph:
    if len(row) >= 3:
        print("No")
        exit()
    if len(row) <= 1:
        ok += 1

if ok <= 1:
    print("No")
    exit()

print("Yes")

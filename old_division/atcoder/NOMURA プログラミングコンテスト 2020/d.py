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
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n = int(input())

A = list(map(int, input().split()))
kosuu = A.count(-1)
# print(kosuu)
uf = UnionFind(n)
for i, s in enumerate(A):
    if s != -1:
        uf.union(i, s-1)

# print(uf)
B = uf.roots()
# print(B)
num = 0
for s in B:
    num += uf.size(s)-1
mod = 10**9+7

ans = num*pow(n-1, kosuu, mod) % mod
for i, s in enumerate(A):
    if s == -1:
        ans = ans+(n-uf.size(i))*pow(n-1, kosuu-2, mod) % mod
print(ans)


# print(num)

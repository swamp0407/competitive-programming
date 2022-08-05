n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
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

uf=UnionFind(n)
for i in range(m):
    c,d=map(int,input().split())
    uf.union(c-1,d-1)

root=uf.roots()

h=[0]*n
d=[0]*n
for i in range(n):
    roo=uf.find(i)
    h[roo]+=a[roo]
    d[roo]+=b[roo]

for i in range(n):
    if h[i]!=d[i]:
        print("No")
        exit()
    else:
        continue


for i in root:
    member =uf.members(i)
    asum=0
    bsum=0
    for j in member:
        asum+=a[j]
        bsum+=b[j]
    if asum==bsum:
        continue
    else:
        print("No")
        exit()

print("Yes")


###### 2022年 8月27日 土曜日 21時00分19秒 JST ######
from collections import defaultdict
from collections import deque
n = int(input())


graph = [[] for _ in range(n+1)]

for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(dist):
    detect = 0
    queue = deque()
    queue.append(1)
    while queue:
        s = queue.popleft()
        for to in graph[s]:
            if dist[to] != -1:
                if detect == 0 and prev[to] != -1 and prev[to] != s:
                    detect = 1
                    current = to
                    while current != -1:
                        loop.append(current)
                        current = prev[current]
                    current = s
                    while current != -1:
                        loop.append(current)
                        current = prev[current]
                continue
            dist[to] = dist[s] + 1
            prev[to] = s

            queue.append(to)


def bfs2(dist, s):
    detect = 0
    queue = deque()
    queue.append(s)
    while queue:
        s = queue.popleft()
        for to in graph[s]:
            if dist[to] != -1:
                if detect == 0 and prev[to] != -1 and prev[to] != s:
                    detect = 1
                    current = to
                    while current != -1:
                        loop.append(current)
                        current = prev[current]
                    current = s
                    while current != -1:
                        loop.append(current)
                        current = prev[current]
                continue
            dist[to] = dist[s] + 1
            prev[to] = s
            uf.union(s, to)
            queue.append(to)


dist = [-1] * (n+1)

prev = [-1] * (n+1)

loop = []


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


uf = UnionFind(n+1)

dist[1] = 0
bfs(dist)
# print(loop)
for i in set(loop):
    dist[i] = 0


for i in range(len(loop)-1):
    uf.union(loop[i], loop[(i+1)])

s = set([i for i in range(1, n+1)])
d = s - set(loop)

dist = [-1] * (n+1)

for s in d:
    if dist[s] == -1:
        bfs2(dist, s)

q = int(input())

for i in range(q):
    a, b = map(int, input().split())
    if uf.same(a, b):
        print("Yes")
    else:
        print("No")

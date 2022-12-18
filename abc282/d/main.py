###### 2022年 12月17日 土曜日 21時00分29秒 JST ######


from collections import defaultdict, deque


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

n, m = map(int, input().split())
uf = UnionFind(n)


graph = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    uf.union(u, v)
    graph[u].append(v)
    graph[v].append(u)

roots = uf.roots()


visited = [-1]

count_0 = 0
count_1 = 1

dist = [-1]*n


def bfs(start):
    queue = deque()
    counts = [1, 0]
    now = 0
    dist[start] = 0
    queue.append(start)
    while queue:
        s = queue.popleft()
        now = 1-dist[s]
        for to in graph[s]:
            if dist[to] != -1:
                if dist[to] != now:
                    return 0, 0
                continue
            dist[to] = now
            counts[now] += 1
            queue.append(to)
    return counts[0], counts[1]


if len(roots) == 1:
    ans = n*(n-1)//2-m
    # print(n,  m, ans)

    ret = bfs(roots[0])
    if ret[0] == 0 and ret[1] == 0:
        print(0)
        exit()
    ans -= (ret[0])*(ret[0]-1)//2+(ret[1])*(ret[1]-1)//2
    # print(n,  m, ans, ret)
    print(ans)
else:
    ans = n*(n-1)//2-m
    for root in roots:
        ret = bfs(root)
        if ret[0] == 0 and ret[1] == 0:
            print(0)
            exit()
        ans -= (ret[0])*(ret[0]-1)//2+(ret[1])*(ret[1]-1)//2
    print(ans)

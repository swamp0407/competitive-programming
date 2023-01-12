class mf_graph:
    def __init__(self, n=0):
        self._n = n
        self.g = [[] for _ in range(n)]
        self.pos = []

    def add_edge(self, frm, to, cap):
        m = len(self.pos)
        e1 = mf_graph._edge(to, cap)
        e2 = mf_graph._edge(frm, 0)
        e1.rev = e2
        e2.rev = e1
        self.pos.append(e1)
        self.g[frm].append(e1)
        self.g[to].append(e2)
        return m

    class edge:
        def __init__(self, frm, to, cap, flow):
            self.frm = frm
            self.to = to
            self.cap = cap
            self.flow = flow

        def __iter__(self):
            yield self.frm
            yield self.to
            yield self.cap
            yield self.flow

    def get_edge(self, i):
        e1 = self.pos[i]
        e2 = e1.rev
        return mf_graph.edge(e2.to, e1.to, e1.cap + e2.cap, e2.cap)

    def edges(self):
        return [self.get_edge(i) for i in range(len(self.pos))]

    def change_edge(self, i, new_cap, new_flow):
        e = self.pos[i]
        e.cap = new_cap - new_flow
        e.rev.cap = new_flow

    def flow(self, s, t, flow_limit=0XFFFFFFFFFFFFFFF):
        g = self.g
        flow = 0
        while flow < flow_limit:
            level = [-1] * self._n
            level[s] = 0
            que = [None] * self._n
            ql = 0
            qr = 1
            que[0] = s
            unreached = True
            while unreached and ql < qr:
                v = que[ql]
                ql += 1
                for e in g[v]:
                    to = e.to
                    if e.cap and level[to] < 0:
                        level[to] = level[v] + 1
                        if to == t:
                            unreached = False
                            break
                        que[qr] = to
                        qr += 1
            if unreached:
                return flow
            ptr = [len(es) for es in g]
            stack = []
            v = t
            up = flow_limit - flow
            res = 0
            while True:
                if v == s or not ptr[v]:
                    if v == s:
                        res = up
                    while stack:
                        tmp = res
                        e, up, res = stack.pop()
                        e.cap -= tmp
                        e.rev.cap += tmp
                        res += tmp
                        if res < up:
                            v = e.to
                            break
                    else:
                        flow += res
                        break
                i = ptr[v]
                while i:
                    i -= 1
                    e = g[v][i]
                    if level[e.to] == level[v] - 1 and e.rev.cap:
                        ptr[v] = i
                        stack.append((e.rev, up, res))
                        v = e.to
                        up = min(up, e.rev.cap)
                        res = 0
                        break
                else:
                    ptr[v] = i
        return flow

    def min_cut(self, s):
        visited = [False] * self._n
        que = [None] * self._n
        ql = 0
        qr = 1
        que[0] = s
        visited[s] = True
        while ql < qr:
            p = que[ql]
            ql += 1
            for e in self.g[p]:
                if e.cap and not visited[e.to]:
                    visited[e.to] = True
                    que[qr] = e.to
                    qr += 1
        return visited

    class _edge:
        def __init__(self, to, cap):
            self.to = to
            self.cap = cap


n, m = map(int, input().split())
s = [input() for _ in range(n)]
g = mf_graph(n * m + 2)
for i in range(n):
    for j in range(i % 2, m, 2):
        if s[i][j] == '#':
            continue
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            x, y = i + di, j + dj
            if 0 <= x < n and 0 <= y < m and s[x][y] == '.':
                g.add_edge(i * m + j, x * m + y, 1)
for i in range(n):
    for j in range(m):
        if s[i][j] == '#':
            continue
        if (i + j) % 2 == 0:
            g.add_edge(n * m, i * m + j, 1)
        else:
            g.add_edge(i * m + j, n * m + 1, 1)
print(g.flow(n * m, n * m + 1))
ans = [list(si) for si in s]
for frm, to, cap, flow in g.edges():
    if flow and frm < n * m and to < n * m:
        i, j = frm // m, frm % m
        x, y = to // m, to % m
        if j == y:
            if i > x:
                i, j, x, y = x, y, i, j
            ans[i][j], ans[x][y] = 'v^'
        else:
            if j > y:
                i, j, x, y = x, y, i, j
            ans[i][j], ans[x][y] = '><'
for a in ans:
    print(*a, sep='')

###### 2022年 12月17日 土曜日 21時00分29秒 JST ######


# union-find木
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]  # 親
        self.rank = [0 for _ in range(n)]  # 根の深さ

    # xの属する木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # xとyの属する集合のマージ
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)


# クラスカル法
# V: 頂点集合(リスト) E: 辺集合[始点, 終点, 重み](リスト)
class kruskal():
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.E.sort(key=lambda x: x[2], reverse=True)  # 辺の重みでソート

    def weight(self):  # 最小全域木の重み和を求める
        UF = UnionFind(len(V))  # 頂点数でUnion Find Treeを初期化
        res = 0
        for i in range(len(self.E)):
            e = self.E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res += e[2]

        return res

    def edge(self):
        UF = UnionFind(len(self.V))  # 頂点数でUnion Find Treeを初期化
        res_E = []
        for i in range(len(self.E)):
            e = self.E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res_E.append(e)

        return res_E

    def node(self):
        UF = UnionFind(len(V))  # 頂点数でUnion Find Treeを初期化
        res_V = []
        for i in range(len(E)):
            e = E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res_V.append(e[0])
                res_V.append(e[1])

        return list(set(res_V))


n, m = map(int, input().split())


A = list(map(int, input().split()))


edge_list = []

mod_m = [[-float("inf")]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        mod_m[i][j] = (pow(A[i], A[j], m) + pow(A[j], A[i], m)) % m
        edge_list.append((i, j, mod_m[i][j]))

# edge_list.sort(reverse=True)
E = edge_list
V = [0]*n  # Vの要素数Nだけを使用


k = kruskal(V, E)
print(k.weight())

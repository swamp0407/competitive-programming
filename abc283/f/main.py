###### 2022年 12月24日 土曜日 21時00分19秒 JST ######

n = int(input())
P = list(map(int, input().split()))


# 単位元(最小値:inf、最大値:-inf、区間和:0、区間積:1、最大公約数:0)
# 最小値/最大値はfloat('inf')を避けた方が高速化できる
ide_ele = -10**18


class SegTree:
    """
    init(init_val, segfunc,ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


# 区間に行う操作(最小値:min、最大値:max、区間和:x+y、区間積:x*y、最大公約数:gcd)
def segfunc(x, y):
    return max(x, y)


'''
print(seg.query(0, 8))
seg.update(5, 0)
print(seg.query(0, 8))
'''
ans = [10**10] * n


def solve(P):
    seg = SegTree([ide_ele]*n, segfunc, ide_ele)
    ret = [0] * n
    for i, p in enumerate(P):
        ret[i] = p + i - seg.query(0, p)
        ans[i] = min(ans[i], ret[i])
        seg.update(p-1, p+i)

    print(ret)

    return ret


solve(P)

for i in range(n):
    P[i] = n - P[i] + 1

solve(P)

P = P[::-1]
ans = ans[::-1]

solve(P)

for i in range(n):
    P[i] = n - P[i] + 1

solve(P)


ans = ans[::-1]
print(ans)

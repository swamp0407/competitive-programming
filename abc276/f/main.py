###### 2022年 11月 7日 月曜日 14時05分19秒 JST ######


n = int(input())

A = list(map(int, input().split()))

# BIT(Fenwick Tree) ※一点加算、区間和のRSQ相当


class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s


mod = 998244353

'''
bit = BIT(5) # 要素数5個の配列を0で初期化
bit.add(1,3) # bit[1]に3を加算
bit.add(2,5) # bit[2]に5を加算
print(bit.sum(1,3)) # インデックス1から2(半閉半開区間)の要素の合計(=8)を取得
print(bit.data) # [0,3,5,8,0]
'''
f1 = BIT(max(A)+10)
f2 = BIT(max(A)+10)


ans = 0


for i in range(n):
    d2 = f2.sum(A[i]+1, max(A)+1)
    d = f1.sum(1, A[i]+1) * A[i] + d2
    ans += 2*d + A[i]
    print(ans*pow(i+1, -1, mod)**2 % mod)
    f1.add(A[i],  1)
    f2.add(A[i], A[i])

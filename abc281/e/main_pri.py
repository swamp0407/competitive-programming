###### 2022年 12月12日 月曜日 12時01分10秒 JST ######

# heapqライブラリのimport
import math
from bisect import (bisect, bisect_left, bisect_right, insort, insort_left,
                    insort_right)
from heapq import (heapify, heappop, heappush, heappushpop, heapreplace,
                   nlargest, nsmallest)
from typing import Generic, Iterable, Iterator, List, TypeVar, Union

n, m, k = map(int, input().split())

A = list(map(int, input().split()))


T = TypeVar('T')


'''
a = [1, 6, 8, 0, -1]
heapify(a)  # リストを優先度付きキューへ(リストが空の場合はheapify()不要)
heappop(a)  # 最小値の取り出し
heappush(a, -2)  # 要素の挿入
nlargest(3, a) #リストから大きい順に3個取り出し([8,6,1])
'''


class PQ:
    def __init__(self) -> None:
        self.q = []
        self.dq = []

    def add(self, x):
        heappush(self.q, x)

    def discard(self, x):
        self.dq.append(x)

    def top(self):
        while self.dq and self.dq[0] == self.q[0]:
            heappop(self.q)
            self.dq.pop(0)
        return self.q[0]

    def pop(self):
        self.top()
        return heappop(self.q)

    def __len__(self):
        return len(self.q) - len(self.dq)

    def __getitem__(self, i):
        if i < 0:
            i += len(self)
        if i < 0 or i >= len(self):
            raise IndexError
        while self.dq and self.dq[0] == self.q[0]:
            heappop(self.q)
            self.dq.pop(0)
        return self.q[i]

    def __repr__(self) -> str:
        return "PQ" + str(list(self))


class DS:
    def __init__(self, k) -> None:
        self.k = k
        self.sum = 0
        self.l = PQ()
        self.r = PQ()

    def ladd(self, x):
        self.sum += x
        self.l.add(x)

    def lerase(self, x):
        self.sum -= x
        self.l.discard(x)

    def add(self, x):
        self.ladd(x)
        if len(self.l) <= self.k:
            return
        self.r.add(self.l[-1])
        self.lerase(self.l[-1])

    def erase(self, x):
        if:
            self.lerase(x)
        else:
            self.r.discard(x)
        if len(self.l) < self.k:
            self.ladd(self.r[0])
            self.r.discard(self.r[0])


ans = 0
ds = DS(k)

for i in range(m):
    ds.add(A[i])

ans = [ds.sum]

for i in range(n-m):
    ar = A[i]
    an = A[i+m]
    ds.add(an)
    ds.erase(ar)
    ans.append(ds.sum)

print(*ans)

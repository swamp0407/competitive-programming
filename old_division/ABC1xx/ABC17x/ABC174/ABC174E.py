import copy
from math import ceil
n, k = map(int, input().split())
A = list(map(int, input().split()))

ok = 100000000000
ng = 0


def cal(n):
    s = 0
    for a in A:
        s += ceil(a/n)-1
    return s


while ok-ng > 1:
    mid = (ok+ng)//2
    s = cal(mid)
    if s <= k:
        ok = mid
    else:
        ng = mid
print(ok)

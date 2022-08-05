from functools import reduce
from operator import mul
mod = 998244353


n, m, k = map(int, input().split())


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


ans = 0
for i in range(k-n+1):
    d = combinations_count(k+n, n) % mod
    print(i+n-1, n-1, d)
    ans = (ans + d) % mod


print(ans)

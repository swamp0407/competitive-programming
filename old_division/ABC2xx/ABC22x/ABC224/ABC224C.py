
import math
from collections import defaultdict
from itertools import combinations
n = int(input())


X = [list(map(int, input().split())) for _ in range(n)]


d = combinations(range(n), 2)
g = defaultdict(int)
ans = 0
for a, b in d:
    x1, y1 = X[a]
    x2, y2 = X[b]
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    yy = y2-y1
    xx = x2-x1
    zz = math.gcd(xx, yy)
    if xx == 0:
        yy = 3
        f = float(x1)
    elif yy == 0:
        xx = 3
        f = float(0)
    else:
        xx = xx//zz
        yy = yy//zz
        f = y1-yy/xx*x1
        print(xx, yy, f)

    g[(xx, yy, f)] += 2


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def get(n):
    for i in range(3, 10000):
        if combinations_count(i, 2)*2 == n:
            return i


ans = combinations_count(n, 3)
for i, c in g.items():
    if c != 2:
        s = get(c)
        ans -= combinations_count(s, 3)

print(ans)

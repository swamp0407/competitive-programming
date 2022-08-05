import math
a, b, n = map(int, input().split())

if b <= n:
    print(math.floor(a*(b-1)/b))
else:
    print(math.floor(a*n/b))

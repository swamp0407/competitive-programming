###### 2022年 11月20日 日曜日 21時00分13秒 JST ######

from functools import reduce
from math import gcd


def my_gcd(*numbers):
    return reduce(gcd, numbers)


n = int(input())

A = list(map(int, input().split()))


diff_list = [A[i+1] - A[i] for i in range(n-1)]

diff = A[-1]-A[0]
m = my_gcd(*diff_list)

# print(m)

ans = 10**10
a = A[0] // (2*m)

b = A[-1] - (2*m*a)

A[0] = A[-1]*2-A[0]
c = A[-1]//(2*m)
d = A[0] - (2*m*c)

ans = min(ans, b, d)

print(ans)

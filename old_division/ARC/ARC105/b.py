import math
from functools import reduce
n = int(input())
A = list(map(int, input().split()))


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


print(gcd_list(A))

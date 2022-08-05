import math
mod = 998244353

x = int(input())

if x == 1:
    print(1)
    exit()
elif x == 2:
    print(2)
    exit()

memo = {}


def cul(x):
    if x == 2:
        return 2
    elif x == 3:
        return 3
    else:
        if memo.get(x):
            return memo[x]
        else:
            memo[x] = cul(x//2)*cul((x*10+10)//20) % mod
            return memo[x]


print(cul(x))

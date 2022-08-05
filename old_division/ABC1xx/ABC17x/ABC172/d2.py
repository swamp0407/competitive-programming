import numpy as np
import sympy
n = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2, N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum


ans = 0
l = [{} for _ in range(n+1)]
dp = [0]*(n+1)
primes = seachPrimeNum(n)
for s in primes:
    dp[s] = 1
for i in range(1, n+1):
    if i == 1:
        l[i][i] = 1
    if dp[i]:
        l[i][i] = 1
    else:
        for prime in primes:
            if i % prime == 0:
                l[i] = l[i//prime].copy()
                l[i][prime] += 1
                break
ans = 1
for i in range(2, n+1):
    b = 1
    for s in l[i].values():
        b = b*(s+1)
    ans += i*b
print(ans)

from sympy import isprime
import sympy
n = int(input())
sympy.divisor_count(2016)
dp = [0]*(n+1)
ans = 0
l = [{} for _ in range(n+1)]
primes = [[] for _ in range(n+1)]
for i in range(1, n+1):
    if i == 1:
        l[i][i] = 1
    elif isprime(i):
        l[i][i] = 1
    elif dp[i]:
        ko = sympy.divisor_count(i)
        ans = i*ko
        s = 2
        while i*s <= n:
            if not primes[s]:
                c = prime_factorize(n)
                primes[s].extend(c)
            else:
                c = primes[s]
            for ss in c:
                l[i*s][ss] += 1
            i*s
            s += 1
            dp[i*s] = False


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


ans = 1
for i in range(1, n+1):
    b = 1
    for s in l[i].values():
        b = b*s
    ans += i*b
print(ans)

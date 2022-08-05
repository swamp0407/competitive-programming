import math
a, b, c, d = map(int, input().split())


def primes(x):
    if x < 2:
        return []

    primes = [i for i in range(x)]
    primes[1] = 0  # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x):
            break
        if prime == 0:
            continue
        for non_prime in range(2 * prime, x, prime):
            primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]


A = {}


def cul(x):

    if A.get(x):
        return A[x]
    A[x] = primes(x+1)
    return A[x]


for i in range(b+d+1):
    cul(i)

for i in range(a, b+1):
    if A[i+c] == A[i+d]:
        if A[i+c-1] != A[i+c]:
            continue
        print("Takahashi")
        exit()


print("Aoki")

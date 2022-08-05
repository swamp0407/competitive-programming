import sympy
import bisect


def fprimes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


n = int(input())
A = list(map(int, input().split()))
A.sort()
ue = 10**6+10
check = [False]*ue
yakusuu = [False]*ue
index = bisect.bisect(A, 1)
A = A[index:]


primes = fprimes(10**3+10)
na = len(A)
B = set(A)
nb = len(B)
pc = 1
sc = 0
if na != nb:
    print("not coprime")
    exit()

for a in A:
    check[a] = True
sc = 0
ll = sympy.divisors(A[0])
for l in primes:
    for a in A:
        boo = all([a % l == 0 for a in A])
        if boo == True and sc == 0:
            sc = 1
        if boo == True:

if sc == 1:
    print("not coprime")
    exit()


for a in A:

    yakul = sympy.divisors(10**9)
    for yaku in yakul:
        if yakusuu[yaku] == True:
            pc = 0
        else:
            yakusuu[yaku] = True

        for i in range(2, ue):
            if check[yaku*i] == True:
                pass

print("pairwise coprime")
print("setwise coprime")

n = int(input())
A = list(map(int, input().split()))

ok = 1
ng = 10**9+10


def solve(B):
    f = [-float("inf")]*(n+1)
    g = [-float("inf")]*(n+1)
    f[0] = 0
    for i in range(n):
        f[i+1] = max(f[i], g[i])+B[i]
        g[i+1] = f[i]
    return max(f[n], g[n])


def check1(m):
    B = [0]*n
    for i, a in enumerate(A):
        B[i] = A[i]*10**3-m
    return solve(B) >= 0


while abs(ok-ng) > 1:
    m = (ok+ng)//2
    if check1(m):
        ok = m
    else:
        ng = m
print(ok*10**-3)

ok = 1
ng = 10**9+10


def check2(m):
    B = [0]*n
    for i, a in enumerate(A):
        B[i] = 1 if a >= m else -1
    return solve(B) > 0


while abs(ok-ng) > 1:
    m = (ok+ng)//2
    if check2(m):
        ok = m
    else:
        ng = m

print(ok)

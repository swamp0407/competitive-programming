import sys
fiv = [1, 1]


def f(n):
    if n < len(fiv):
        return fiv[n]
    ans = (f(n-2)+f(n-1)) % (10**9+7)
    fiv.append(ans)
    return ans


sys.setrecursionlimit(10000)
print(f(6000))
print(len(fiv))

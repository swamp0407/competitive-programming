import scipy.special as sp
n, a, b = map(int, input().split())
ans = sp.comb(n, a)
print(ans)

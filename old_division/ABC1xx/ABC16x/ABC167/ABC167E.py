n, m, k = map(int, input().split())


mod = 998244353
sum = pow(m, n, mod)
for i in range(m-k):
    sum -= pow(i, n, mod)

print(sum % mod)

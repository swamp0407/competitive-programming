

from math import factorial
n, P = map(int, input().split())


def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)
# a = cmb(n, r, mod)

# def comb(n, r):
#     if n - r < r:
#         r = n - r
#     if r == 0:
#         return 1
#     if r == 1:
#         return n

#     numerator = [n - r + k + 1 for k in range(r)]
#     denominator = [k + 1 for k in range(r)]

#     for p in range(2, r+1):
#         pivot = denominator[p - 1]
#         if pivot > 1:
#             offset = (n - r) % p
#             for k in range(p-1, r, p):
#                 numerator[k - offset] /= pivot
#                 denominator[k] /= pivot

#     result = 1
#     for k in range(r):
#         if numerator[k] > 1:
#             result = (result*int(numerator[k]))

#     return result


ans = 0
for i in range(1, (n+1)//2):
    a = comb(n-1, i-1)
    a = a % P
    b = (a * 26) % P * pow(25, i-1, P)
    b = b % P
    # print(i, a, b)
    # print(b)
    ans = (ans+b) % P

print(ans)

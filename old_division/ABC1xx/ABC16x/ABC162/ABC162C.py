from fractions import gcd
n = int(input())


def gcds(a, b, c):
    d = gcd(a, b)
    e = gcd(d, c)
    return e


sum = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        for k in range(j, n+1):
            if i == j and j == k:
                sum = sum+gcds(i, j, k)
            elif i == j:
                sum = sum+2*gcds(i, j, k)
            else:
                sum = sum+6*gcds(i, j, k)

print(sum)

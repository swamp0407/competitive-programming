n = int(input())


d = {}


def cul(n):
    if n == 1:
        return [1]
    if d.get(n-1):
        a = d[n-1]
    else:
        a = cul(n-1)
    return a + [n] + a


print(*cul(n))

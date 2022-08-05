n = int(input())

ans = float("inf")


def cul(a, b):
    return (a+b)**3-2*a*b*(a+b)


i = 10**6+1

j = 0
while i >= 0:
    d = cul(i, j)
    while d < n:
        j += 1
        d = cul(i, j)

    ans = min(ans, d)
    i = i-1

print(ans)

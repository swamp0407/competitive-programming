import math
t = int(input())


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


for i in range(t):
    n, a, b, x, y, z = list(map(int, input().split()))

    can = [(x, 1), (y/a, 2), (z/b, 3)]
    can.sort(reverse=True)
    if y/a >= z/b:
        y, a, z, b = z, b, y, a

    if x <= y/a and x <= z/b:
        print(n*x)
        continue

    if y/a <= x and x <= z/b:
        aa = n//a
        aaa = n - aa*a
        cost = aa * y+aaa*x
        print(cost)
        continue

    if y/a <= x and z/b <= x:
        aa = n//a
        aaa = n - aa*a
        ans = float("inf")
        diff = 0
        prea = aa
        while True:
            bb = aaa//b
            bbb = aaa-bb*b
            cost = aa * y + bb*z + bbb*x
            ans = min(ans, cost)
            diff += 1
            aa = prea-diff
            aaa = aaa+a
            if lcm(a, b)//a+1 <= diff or aa < 0:
                break

        print(ans)

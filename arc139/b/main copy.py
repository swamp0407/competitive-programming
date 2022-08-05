t = int(input())


for i in range(t):
    n, a, b, x, y, z = list(map(int, input().split()))

    can = [(x, 1), (y/a, 2), (z/b, 3)]
    can.sort(reverse=True)
    if y/a > z/b:
        y, a, z, b = z, b, y, a

    if a*x == y and b*x < z:
        print(n*x)
        continue
    if a*x < y and b*x == z:
        print(n*x)
        continue

    if a*x < y and b*x < z:
        print(n*x)
        continue

    if y < a*x and x*b < z:
        aa = n//a
        aaa = n - aa*a
        cost = aa * y+aaa*x
        print(cost)
        continue

    if y < a*x and z < x*b:
        aa = n//a
        aaa = n - aa*a

        bb = aaa//b
        bbb = aaa-bb*b

        cost = aa * y + bb*z + bbb*x
        print(cost)

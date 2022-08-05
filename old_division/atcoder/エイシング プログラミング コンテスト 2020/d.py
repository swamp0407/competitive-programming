def popcnt(n):
    return bin(n).count("1")


def f(x, px):
    moto = x
    if ansl[x] != -1:
        return ansl[x]
    x = x % px
    if popl[x] == -1:
        px = popcnt(x)
        popl[x] = px
    else:
        px = popl[x]
    ans = f(x, px)+1
    ansl[moto] = ans
    return ans


n = int(input())
x = input()
xx = x
nx = int(x, 2)
pnx = popcnt(nx)

ansl = [-1]*(2*10**5+10)
popl = [-1]*(2*10**5+10)
ansl[0] = 0
for i in range(n):
    if i == 0:
        a = 1 << (n-1)
    else:
        a = a >> 1
    x = nx ^ a
    if xx[i] == "1":
        px = pnx-1
    else:
        px = pnx+1
    ans = 0
    if x != 0:
        x = x % px
        moto = x
        if popl[x] == -1:
            px = popcnt(x)
            popl[x] = px
        else:
            px = popl[x]
        ans = f(x, px)+1
        ansl[moto] = ans-1
    print(ans)

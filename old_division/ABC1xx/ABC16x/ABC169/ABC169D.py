n = int(input())
a = int(n**0.5)+1

if n == 1:
    print(0)
    exit()
ans = 0


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def waru(n, s, ans):
    a = int(n**0.5)+1
    for i in range(s, a+1):
        j = 1
        frag = 0
        while 1:
            if n % pow(i, j) == 0:
                frag = 1
                n = n//pow(i, j)
                ans += 1
                j += 1
            elif frag == 1:
                return (n, i, ans)
            else:
                break


a = prime_factorize(n)
c = set(a)
b = int(n**0.5)+1
ans = 0
for i in c:
    s = a.count(i)
    j = 1
    while 1:
        if s-j >= 0:
            ans += 1
            s = s-j
            j = j+1
        else:
            break
if ans == 0:
    print(1)
    exit()
print(ans)

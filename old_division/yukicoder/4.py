import sys
sys.setrecursionlimit(10000)
n = int(input())
win = [-1]*(n+1)

pflag = [True]*(n+1)
primes = []

for i in range(2, n):
    if pflag[i]:
        primes.append(i)
        num = 2
        while i*num <= n:
            pflag[i*num] = False
            num += 1


def ok(n):
    if n == 2 or n == 3:
        win[n] = 0
        return win[n]
    if win[n] != -1:
        return win[n]
    for prime in primes:
        if n-prime < 2:
            win[n] = 0
            return win[n]
        s = ok(n-prime)
        if s == 0:
            win[n] = 1
            return win[n]


d = ok(n)

if d == 0:
    print("Lose")
else:
    print("Win")

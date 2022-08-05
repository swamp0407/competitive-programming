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

win[2] = 0
win[3] = 0

for i in range(2, n+1):
    for prime in primes:
        if i-prime < 2:
            win[i] = 0
            break
        if win[i-prime] == 0:
            win[i] = 1
            break

if win[n] == 0:
    print("Lose")
else:
    print("Win")

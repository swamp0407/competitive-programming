
x = int(input())

for i in range(100):
    for j in range(100):
        if pow(i, 5)+pow(j, 5) == x:
            print(i, -j)
            exit()


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


for i in make_divisors(x):
    a = i
    b = 0
    while pow(a, 5)-pow(b, 5) <= x:
        if pow(a, 5)-pow(b, 5) == x:
            print(a, b)
            exit()
        b += 1
        a += 1

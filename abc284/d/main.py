###### 2023年 1月 7日 土曜日 21時00分20秒 JST ######

t = int(input())


def sol(n):
    s = int(n**0.5)
    for i in range(max(s-100, 0), s+100):
        if i*i == n:
            return i


def solve(n):
    for i in range(2, 3*10**6):
        if n % i == 0:
            if n % (i*i) == 0:
                return i, n//(i*i)
            return sol(n//i), i


for i in range(t):
    n = int(input())
    print(*solve(n))

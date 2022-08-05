from collections import defaultdict
n = int(input())

A = list(map(int, input().split()))


A.sort()


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    flag = 0
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
            else:
                flag = 1
        i += 1
    return lower_divisors + upper_divisors[::-1], flag


dict = dict()
ans = 0
for a in A:
    if dict.get(a):
        dict[a] += 1
    else:
        dict[a] = 1
# print(dict)
for key, value in dict.items():
    # print(key, value)
    divs, flag = make_divisors(key)
    for div in divs:
        if dict.get(div) and dict.get(key//div):
            ans += value*dict[div]*dict[key//div]
    # print(divs)

print(ans)

###### 2022年 11月12日 土曜日 21時00分18秒 JST ######
from collections import defaultdict

n, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort()


s = defaultdict(int)

pre = -1
now = A[0]
for i, a in enumerate(A):
    if a == pre:
        s[now] += a
        pre = a
    elif a - 1 == pre:
        s[now] += a
        pre = a
    else:
        now = a
        pre = a
        s[now] += a

    if i == n-1:
        if A[0] == 0 and a == m-1:
            # s[now] += s[0]
            if now != 0:
                s[now] += s[0]
# print(s)

a = max(s.values())

print(sum(A) - a)

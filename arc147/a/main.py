###### 2022年 9月 4日 日曜日 21時00分10秒 JST ######
from collections import deque
n = int(input())

A = list(map(int, input().split()))


# print(a)

d = deque()
A.sort()
for a in A:
    d.append(a)

count = 0
while len(d) != 1:
    b = d.pop()
    c = d.popleft()
    e = b % c
    if e == 0:
        d.appendleft(c)
    else:
        d.appendleft(c)
        d.appendleft(e)
    count += 1

print(count)

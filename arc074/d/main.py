###### 2022年 12月27日 火曜日 09時27分12秒 JST ######
# 数列の切り替わり時点を全探索
from heapq import heappop, heappush

n = int(input())
a = list(map(int, input().split()))

L = sum(a[:n])
l = []
for i in range(n):
    heappush(l, a[i])

tmp = a[n:]
tmp.sort()
R = sum(tmp[:n])
r = []
for i in range(n, 2*n):
    heappush(r, tmp[i])
rtaiki = []

ans = []
ans.append(L-R)

for i in range(n, 2*n):
    x = a[i]
    if x > l[0]:
        L -= heappop(l)
        L += x
        heappush(l, x)

    if x <= r[0]:
        R -= x
        R += heappop(r)
        while rtaiki and r[0] == rtaiki[0]:
            heappop(r)
            heappop(rtaiki)
    else:
        heappush(rtaiki, x)
        while rtaiki and r[0] == rtaiki[0]:
            heappop(r)
            heappop(rtaiki)

    ans.append(L-R)

print(max(ans))

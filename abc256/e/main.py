###### 2022年 6月18日 土曜日 21時00分23秒 JST ######

# heapqライブラリのimport
from heapq import heapify, heappush, heappop, heappushpop
from collections import defaultdict
n = int(input())

X = list(map(int, input().split()))

C = list(map(int, input().split()))

Z = []

for i in range(n):
    Z.append((X[i], i, C[i]))

d = defaultdict(int)
for i in range(n):
    d[X[i]] += C[i]


'''
a = [1, 6, 8, 0, -1]
heapify(a)  # リストを優先度付きキューへ(リストが空の場合はheapify()不要)
heappop(a)  # 最小値の取り出し
heappush(a, -2)  # 要素の挿入
nlargest(3, a) #リストから大きい順に3個取り出し([8,6,1])
'''
visited = [False] * n
hp = []
for i in range(1, n+1):
    hp.append((d[i], i))
heapify(hp)

# print(hp)
ans = 0
while hp:
    c, i = heappop(hp)
    if visited[i-1]:
        continue
    visited[i-1] = True

    ans += c

    d[X[i-1]] -= C[i-1]
    heappush(hp, (d[X[i-1]], X[i-1]))

print(ans)

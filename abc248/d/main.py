import heapq
from bisect import *
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
q = int(input())
Q = []
dict = dict()

for i, a in enumerate(A):
    if dict.get(a):
        heapq.heappush(dict[a], i)
    else:
        dict[a] = [i]

# for a in A:
#     dict[a].sort()
# print(dict)


for i in range(q):
    l, r, x = map(int, input().split())
    if not dict.get(x):
        print(0)
    else:
        a = bisect_right(dict[x], r-1)
        b = bisect_left(dict[x], l-1)
        print(a-b)


# dict = [defaultdict(int) for _ in range(n)]

# for a in A:

import collections
n = int(input())
d = collections.defaultdict(int)
for i in range(n):
    l = tuple(list(map(int, input().split())))
    d[l] += 1


print(len(d.keys()))

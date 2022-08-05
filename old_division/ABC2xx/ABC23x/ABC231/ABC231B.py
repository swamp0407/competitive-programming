import collections
n = int(input())

d = [input() for _ in range(n)]

c = collections.Counter(d)

print(c.most_common()[0][0])

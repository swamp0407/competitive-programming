# 12:55 13:06
import itertools
n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

a = []
for i in range(1, n+1):
    a.append(i)
a = list(itertools.permutations(a))
b = 0
c = 0
for i, v in enumerate(a):
    if list(v) == P:
        b = i
    if list(v) == Q:
        c = i

print(abs(b-c))

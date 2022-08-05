# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import copy
from collections import defaultdict
n = int(input())

l = [input() for _ in range(n)]

S = input()
d = defaultdict(set)

for i, a in enumerate(l):
    for b in a:
        d[b].add(i)
ok = 0
ans = 0


def solve(s, i):
    count = 0
    pre = copy.copy(d[s])
    while pre:
        count += 1
        if i+count == len(S):
            break
        pre = pre & d[S[i+count]]
    return count


for i, s in enumerate(S):
    if i < ok:
        continue
    ans += 1
    a = solve(s, i)
    ok += a


print(ans)

from collections import defaultdict
n = int(input())
L = list(map(int, input().split()))
L.sort()
s = defaultdict(int)
for l in L:
    s[l] += 1
L = set(L)

s = dict(s)
ans = 0
for a in L:
    for b in L:
        for c in L:
            if a < b and b < c and a+b > c and b+c > a and c+a > b:
                ans += s[a]*s[b]*s[c]
print(ans)

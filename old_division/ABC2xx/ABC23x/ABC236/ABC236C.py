

n, m = map(int, input().split())
S = list(input().split())
T = list(input().split())

s = {}

for t in T:
    s[t] = 1

for ss in S:
    if s.get(ss):
        print("Yes")
    else:
        print("No")

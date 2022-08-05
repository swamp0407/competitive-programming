n = int(input())

d = {}
T = []
for i in range(n):
    s, t = map(str, input().split())
    T.append([s, t])
    if d.get(s):
        d[s] += 1
    else:
        d[s] = 1
    if d.get(t):
        d[t] += 1
    else:
        d[t] = 1


for s, t in T:
    if d[s] >= 2 and d[t] >= 2:
        print("No")
        exit()
print("Yes")

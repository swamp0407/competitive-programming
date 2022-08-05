
n = int(input())

d = {}
T = []
for i in range(n):
    s, t = map(str, input().split())
    T.append([s, t])


for s, t in T:
    if d.get((s, t)):
        print("No")
        exit()
    d[(s, t)] = 1

for s, t in T:
    flags = 0
    flagt = 0
    for s2, t2 in T:
        if s == s2 and t == t2:
            continue
        if s == s2 or s == t2:
            flags = 1
        if t == t2 or t == s2:
            flagt = 1

    if flags and flagt:
        print("No")
        exit()

print("Yes")

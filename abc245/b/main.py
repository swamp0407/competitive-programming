n = int(input())
A = list(map(int, input().split()))

A.sort()
ok = {}
for a in A:
    ok[a] = 1

for i in range(2010):
    if not ok.get(i):
        print(i)
        exit()

from collections import deque

n = int(input())
A = list(map(int, input().split()))


q = deque()
last = {}
counts = 0
for a in A:
    if counts == 0:
        q.append([a, 1])
        counts += 1
        print(counts)
        continue
    d = q.pop()
    if d[0] == a:
        if d[1] == d[0]-1:
            counts -= d[1]
            print(counts)
            continue
        q.append([a, d[1]+1])
        counts += 1
        print(counts)
    else:
        q.append(d)
        q.append([a, 1])
        counts += 1
        print(counts)

A = [0, 2, 4, 5, 7, 9, 11]
N = int(input())
T = list(map(int, input().split()))
l = []
for i in range(12):
    B = []
    for j in A:
        c = (i+j) % 12
        B.append(c)
    flag = 1
    for t in T:
        if t in B:
            continue
        else:
            flag = 0
            break
    if flag == 1:
        l.append(i)


if len(l) == 1:
    print(*l)
else:
    print(-1)

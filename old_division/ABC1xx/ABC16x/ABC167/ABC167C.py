n, m, x = list(map(int, input().split()))
z = [list(map(int, input().split())) for _ in range(n)]
nux = 10**13
for i in range(2**n):
    alu = [-x]*m
    buy = []
    for j in range(n):
        if (i >> j) & 1:
            buy.append(j)
    num = 0
    if i == 30:
        s = 1
    for k in buy:
        num += z[k][0]
        for ss in range(m):
            alu[ss] += z[k][ss+1]
    if len([i for i in alu if i < 0]) == 0:
        nux = min(num, nux)
if nux == 10**13:
    print(-1)
else:
    print(nux)

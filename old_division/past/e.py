n, m, q = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(m)]
c = list(map(int, input().split()))

S = [list(map(int, input().split())) for _ in range(q)]
a = [[] for _ in range(n+1)]

for i in range(m):
    a[uv[i][1]].append(uv[i][0])
    a[uv[i][0]].append(uv[i][1])


for s in S:
    if s[0] == 1:
        print(c[s[1]-1])
        for ax in a[s[1]]:
            c[ax-1] = c[s[1]-1]
    elif s[0] == 2:
        print(c[s[1]-1])
        c[s[1]-1] = s[2]

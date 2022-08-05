n, m = map(int, input().split())
h = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(m)]
b = set()
for i, j in a:
    if h[i-1] < h[j-1]:
        b.add(i-1)
    elif h[i-1] > h[j-1]:
        b.add(j-1)
    else:
        b.add(j-1)
        b.add(i-1)


print(n-len(b))

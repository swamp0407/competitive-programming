# 他の人の参考にした

n, m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(m)]
nax = 0
for i in range(2**n):
    list1 = []
    for j in range(n):
        if (i >> j) & 1:
            list1.append(j+1)
    if all([list1[i], list1[j]]in xy for i in range(len(list1)) for j in range(i+1, len(list1))):
        nax = max(len(list1), nax)
print(nax)

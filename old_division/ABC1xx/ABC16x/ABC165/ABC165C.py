import itertools
n, m, q = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(q)]

num = 0
nax = 0

nums = [i for i in range(1, m+1)]

for com in list(itertools.combinations_with_replacement(nums, n)):
    num = 0
    for j in range(q):
        if com[l[j][1]-1]-com[l[j][0]-1] == l[j][2]:
            num += l[j][3]
    nax = max(num, nax)
print(nax)

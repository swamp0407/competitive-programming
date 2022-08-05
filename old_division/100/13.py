# import copy
# R, C = map(int, input().split())
# s = [list(map(int, input().split())) for i in range(R)]
# sums = 0
# nax = 0
# print(s)
# for i in range(2**R):
#    scopy = copy.deepcopy(s)
#    print(scopy)
#    print(scopy[1])
#    sums = 0
#    for t in range(R):
#        if (i >> t) & 1:
#            a = 1
#            for h in range(C):
#                scopy[t][h] += 1
# for j in range(C):
#    sums = sum([1 for scopy[t] in  if _ % 2 == 1] for t in range(R))
#    nax = max(nax, sums, C-sums)
# print(nax)
import numpy as np
n, m = map(int, input().split())  # 行と列の数
a = [list(map(int, input().split())) for _ in range(n)]  # お煎餅二次元配列
a = np.array(a)
ans = 0
print(a)
for i in range(1 << n):
    tmp = np.array([[i >> j & 1 for j in range(n)]]).T
    print([i >> j & 1 for j in range(n)])
    print(tmp)
    x = np.sum(a ^ tmp, axis=0)
    ans = max(ans, np.sum(np.maximum(x, n-x)))


print(ans)

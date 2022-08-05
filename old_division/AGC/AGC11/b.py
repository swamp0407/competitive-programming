import itertools
n = int(input())
A = list(map(int, input().split()))

A.sort()
num = 1
B = list(itertools.accumulate(A))
for i, a in enumerate(A[1:]):
    if B[i]*2 < a:
        num = 1
    else:
        num += 1
print(num)

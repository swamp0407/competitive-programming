import bisect
import numpy
n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = numpy.cumsum(A)
b = numpy.cumsum(B)
ans = 0
for i in range(n):
    if a[i] <= k:
        c = bisect.bisect(b, k-a[i])
        ans = max(ans, i+c+1)
for i in range(m):
    if b[i] <= k:
        c = bisect.bisect(a, k-b[i])
        ans = max(ans, i+c+1)

print(ans)

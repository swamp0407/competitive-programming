import math
n, l, w = map(int, input().split())
A = list(map(int, input().split()))

start = 0
ans = 0
for i in range(n):
    if w == 1:
        ans += max(A[i]-start, 0)
    else:
        ans += max(math.ceil((A[i]-start)/w), 0)
    start = A[i]+w

if A[n-1]+w < l:
    if w == 1:
        ans += l-(A[n-1]+w)
    else:
        ans += math.ceil((l-(A[n-1]+w))/w)

print(ans)

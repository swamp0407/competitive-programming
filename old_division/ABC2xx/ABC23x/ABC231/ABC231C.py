import bisect
n, q = map(int, input().split())

A = list(map(int, input().split()))
A.sort()
for i in range(q):
    x = int(input())
    a = bisect.bisect_left(A, x)
    print(n-a)

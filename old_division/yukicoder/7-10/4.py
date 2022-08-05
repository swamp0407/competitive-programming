from bisect import bisect_right
n, d = map(int, input().split())
A = [int(input()) for _ in range(n)]

B = sorted(A)
for i in A:
    print(bisect_right(B, i-d))

n, K, x = map(int, input().split())

A = list(map(int, input().split()))
c = 0
k = 0
L = []
for i, a in enumerate(A):
    if K == 0:
        L += A[i:]
        break
    k = min(a//x, K)
    K = K-k
    L.append(a-k*x)
i = 0
L.sort(reverse=True)
while 0 < K and i < len(L):
    L[i] = 0
    i = i+1
    K -= 1

print(sum(L))

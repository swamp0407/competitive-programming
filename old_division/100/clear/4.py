n, m = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
amax = 0
for i in range(m-1):
    for j in range(i+1, m):
        sum = 0
        for k in range(n):
            sum += max(A[k][j], A[k][i])
        if sum > amax:
            amax = sum
print(amax)

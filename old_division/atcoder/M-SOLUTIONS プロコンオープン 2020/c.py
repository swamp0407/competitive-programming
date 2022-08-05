n, k = map(int, input().split())
A = list(map(int, input().split()))


for i in range(n-k):
    if A[i+k]-A[i] > 0:
        print("Yes")
    else:
        print("No")

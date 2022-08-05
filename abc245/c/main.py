n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

at = 1
bt = 1
for i in range(1, n):
    nat, nbt = 0, 0
    if at:
        if abs(B[i]-A[i-1]) <= k:
            nbt = 1
        if abs(A[i]-A[i-1]) <= k:
            nat = 1
    if bt:
        if abs(B[i]-B[i-1]) <= k:
            nbt = 1
        if abs(A[i]-B[i-1]) <= k:
            nat = 1
    if nat == 0 and nbt == 0:
        print("No")
        exit()
    at, bt = nat, nbt

print("Yes")

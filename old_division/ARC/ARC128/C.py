import numpy as np
n, m, s = map(int, input().split())
A = list(map(int, input().split()))
AA = [0]+A
tukaus = [0]*n
nokori = s
cum = np.cumsum(AA)
for right in range(n-1, -1, -1):
    default = A[right]
    tleft = right

    for left in range(right-1, 0, -1):
        if (cum[right]-cum[left-1]) >= default * (right-left+1):
            tleft = left
            default = (cum[right]-cum[left])/(right-left+1)
            print("更新", right, left, default)
    tukau = min(nokori, m*(right-tleft+1))
    nokori = nokori-tukau
    for i in range(tleft, right+1):
        tukaus[i] = tukau/(right-tleft+1)

    if nokori == 0:
        break


ans = 0

for i in range(n):
    ans += A[i]*tukaus[i]

print(ans)

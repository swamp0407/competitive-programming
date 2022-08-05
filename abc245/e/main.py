
import bisect
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))


AB = []
CD = []
EF = []
for a, b in zip(A, B):
    AB.append((a, b))
    EF.append((a, b, 0))

for c, d in zip(C, D):
    CD.append((c, d))
    EF.append((c, d, 1))

AB.sort()
CD.sort()
EF.sort()

pc, pd = -1, -1
for i in range(m):
    if pc < CD[i][0]:
        ABp = []


print(EF)

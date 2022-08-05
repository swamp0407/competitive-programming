n = int(input())
A = list(map(int, input().split()))

B = [1]
for i in range(n):
    B.append((B[i]-A[i])*2)

C = [A[n]]

for i, s in enumerate(B):
    if i == len(B)-1:
        a = 1
    elif B[i] <= 0:
        print(-1)
        exit()
if B[-1]-A[n] < 0:
    print(-1)
    exit()

for i in range(n):
    C.append(C[i]+A[n-1-i])
C = C[::-1]

num = 0
frag = 0
for i in range(n):
    if B[i] >= C[i]:
        frag = 1
    if frag == 0:
        num += B[i]
    else:
        num += C[i]
num += C[n]
print(num)

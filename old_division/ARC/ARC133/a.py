n = int(input())
A = list(map(int, input().split()))


rm = A[0]
for i, a in enumerate(A):
    if i == 0:
        continue

    if A[i-1] > A[i]:
        rm = A[i-1]
        break
    else:
        rm = a
for a in A:
    if a == rm:
        continue
    print(a, end=" ")

print()

n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort(reverse=True)

# print(A)
# print(B)
if n % 2 == 1:
    a = (n+1)//2-1
    print(B[a]-A[a]+1)
else:
    a = n//2-1
    b = n//2
    print(B[a]+B[b]-(A[a]+A[b])+1)

# print(a)

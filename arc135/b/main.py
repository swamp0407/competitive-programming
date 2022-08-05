n = int(input())


S = list(map(int, input().split()))
C = []

A = []
B = []
C = []
for i in range(n-1):
    if i < 3:
        if i % 3 == 0:
            A.append(S[i+1]-S[i])
        if i % 3 == 1:
            B.append(S[i+1]-S[i])
        if i % 3 == 2:
            C.append(S[i+1]-S[i])
        continue
    if i % 3 == 0:
        A.append(A[(i-3) // 3] + S[i+1]-S[i])
    if i % 3 == 1:
        B.append(B[(i-3) // 3]+S[i+1]-S[i])
    if i % 3 == 2:
        C.append(C[(i-3) // 3]+S[i+1]-S[i])

a = 0 if A == [] else max(0, -min(A))
b = 0 if B == [] else max(0, -min(B))
c = 0 if C == [] else max(0, -min(C))

if a+b+c > S[0]:
    print("No")
    exit()
c = S[0]-a-b
if n == 1:
    print("Yes")
    print(0, 0, S[0])
    exit()
elif n == 2:
    print("Yes")
    print(S[0]-min(S), 0, min(S), S[1]-min(S))
    exit()


# la = A[(n-3) // 3]
# lb = B[(n-3) // 3]
# lc = C[(n-3) // 3]

# if S[0]+la+lb+lc > S[n-1]:
#     print("No")
#     exit()

ans = []
for i in range(n+2):
    if i < 3:
        if i % 3 == 0:
            # print(a, end=" ")
            ans.append(a)
        if i % 3 == 1:
            ans.append(b)
            # print(b, end=" ")
        if i % 3 == 2:
            ans.append(c)
            # print(c, end=" ")
        continue
    if i % 3 == 0:
        # print(a+A[(i-3) // 3], end=" ")
        ans.append(a+A[(i-3) // 3])
    elif i % 3 == 1:
        # print(b+B[(i-3) // 3], end=" ")
        ans.append(b+B[(i-3) // 3])
    elif i % 3 == 2:
        # print(c+C[(i-3) // 3], end=" ")
        ans.append(c+C[(i-3) // 3])
print("Yes")
print(*ans)

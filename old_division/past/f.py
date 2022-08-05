n = int(input())

A = [input() for _ in range(n)]


""" AC = [""]*n
for i in range(n):
    for j in range(n):
        AC[i] = AC[i]+A[j][i]

# print(AC)


for i in range(n):
    if AC[i] == AC[i][::-1]:
        print(AC[i])
        exit()

print(-1)
 """
f = 0
b = n-1
ans = ""
while b >= f:
    if b == f:
        print(ans+A[f][0]+ans[::-1])
        exit()
    ss = set(A[f]) & set(A[b])
    if len(ss) == 0:
        print(-1)
        exit()
    ans = ans+ss.pop()
    f += 1
    b -= 1

print(ans+ans[::-1])

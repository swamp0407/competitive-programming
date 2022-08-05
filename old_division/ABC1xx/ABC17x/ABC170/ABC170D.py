n = int(input())
A = sorted(map(int, input().split()))
nux = A[-1]+1
ans = 0
table = [True]*nux
for i, s in enumerate(A):
    if table[s] == False:
        continue
    if i == n-1:
        ans += 1
    elif A[i+1] != s:
        ans += 1
    b = 1
    while b*s < nux:
        table[b*s] = False
        b += 1
print(ans)

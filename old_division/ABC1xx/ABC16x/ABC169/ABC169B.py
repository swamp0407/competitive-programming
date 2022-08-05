n = int(input())
A = list(map(int, input().split()))
if A.count(0) != 0:
    print(0)
    exit()
for i, a in enumerate(A):
    if i == 0:
        ans = a
    elif ans > 10**18:
        print(-1)
        exit()
    else:
        ans = ans*a
if ans > 10**18:
    print(-1)
    exit()
print(ans)

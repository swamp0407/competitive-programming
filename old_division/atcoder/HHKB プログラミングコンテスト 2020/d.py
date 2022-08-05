t = int(input())
ans = 0
mod = 10**9+7
for i in range(t):
    n, a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    C = (n-a+1)**2
    D = (n-b+1)**2
    ans = C*D % mod
    ans = (ans-(a-b+1)**2*C) % mod
    maxv = min(n-a, b-1)
    sub = 0
    sub = (n-a+1)*(a-b+1)*2*maxv*(2*n-2*a+1-maxv) % mod

    sub += (maxv*(2*n-2*a+1-maxv) % mod)**2
    """for z in range(1, maxv+1):
        sub += (n-a+1)*(n-z-a+1)*(a-b+1)*4

    for x in range(1, maxv+1):
        for y in range(1, maxv+1):
            sub += (n-a-x+1)*(n-a-y+1)*4"""
    ans = (ans-sub) % mod
    print(ans)

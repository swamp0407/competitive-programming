x, k, d = map(int, input().split())

if k*d < abs(x):
    ans = abs(x)-k*d
    print(ans)
    exit()
x = abs(x)
n = x//d
ans = x-n*d
nn = k-n
if nn % 2 == 0:
    print(ans)
else:
    print(abs(ans-d))

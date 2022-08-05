from bisect import bisect
n, m = map(int, input().split())

H = list(map(int, input().split()))
W = list(map(int, input().split()))

H = sorted(H)

dpl = [0]*n
dpr = [0]*n

dpl[0] = 0
if n == 1:
    nux = float("inf")
    for i in range(m):
        nux = min(nux, abs(W[i]-H[0]))
    print(nux)
    exit()

for i in range(2, n, 2):
    dpl[i] = dpl[i-2]+abs(H[i-1]-H[i-2])

for i in range(2, n, 2):
    dpr[n-1-i] = dpr[n+1-i]+abs(H[n+1-i]-H[n-i])

nux = float("inf")
for i in range(m):
    a = bisect(H, W[i])
    t = a//2*2
    if a == 0:
        nux = min(nux, dpr[a]+abs(W[i]-H[0]))
    elif a == n:
        nux = min(nux, dpl[n-1]+abs(W[i]-H[n-1]))
    else:
        nux = min(nux, dpr[t]+dpl[t]+abs(W[i]-H[t]))

print(nux)

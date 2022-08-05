x, n = map(int, input().split())

if n == 0:
    print(x)
    exit()
P = list(map(int, input().split()))

for s in range(-101, 110):
    if s not in P:
        ans = s
        break

for s in range(-101, 110):
    if s not in P:
        if abs(ans-x) > abs(s-x):
            ans = s
        elif abs(ans-x) == abs(s-x):
            ans = min(ans, s)

print(ans)

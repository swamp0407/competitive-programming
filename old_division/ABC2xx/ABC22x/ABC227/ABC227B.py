
done = {}
n = input()
A = list(map(int, input().split()))


def cul(a, b):
    return 4*a*b+3*a+3*b


for a in range(1, 250):
    for b in range(1, 250):
        d = cul(a, b)
        if d > 1000:
            break
        done[d] = 1

ans = 0
for a in A:
    if done.get(a):
        continue
    else:
        ans += 1

print(ans)

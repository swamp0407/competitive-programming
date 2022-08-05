n = int(input())

S = []

for i in range(n):
    a, b = map(int, input().split())

    S.append((a, b))

total = 0
for a, b in S:
    total += a/b


ans = 0
cur = 0
for a, b in S:
    if cur + a/b < total/2:
        ans += a
        cur += a/b
    else:
        print(ans+(total/2-cur)*b)
        break

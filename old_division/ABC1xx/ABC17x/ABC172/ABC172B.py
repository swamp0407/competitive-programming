a = input()
b = input()

n = len(a)
ans = 0
for i in range(n):
    if a[i] != b[i]:
        ans += 1

print(ans)

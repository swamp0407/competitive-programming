n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
ans = 0
for i in range(n-1):
    if i == 0:
        ans += l[0]
    else:
        ans += l[(i+1)//2]

print(ans)

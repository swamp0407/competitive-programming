n = int(input())


s = int(pow(n, 1/3))+10

ans = 0
for a in range(1, s):
    for b in range(a, 10**6):
        c = int(n/a/b)
        if c < b:
            break
        else:
            ans += c-b+1


print(ans)

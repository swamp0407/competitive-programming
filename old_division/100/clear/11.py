# 23:20 他の人のコード参考にした(ほぼ写し)
n, m = map(int, input().split())
S = [list(map(int, input().split()))[1:] for i in range(m)]
P = list(map(int, input().split()))
ans = 0
for i in range(2**n):
    for s, p in zip(S, P):
        c = 0
        for t in s:
            if (i >> t-1) & 1:
                c += 1
        if c % 2 != p:
            break
    else:
        ans += 1
print(ans)

n, k = map(int, input().split())

S = []
ans = 0
for i in range(n):
    s = input()
    S.append(s)

for bit in range(1 << n):
    L = []
    for i in range(n):
        if bit & 1 << i:
            L.append(S[i])
    C = [0]*26
    for l in L:
        for ll in l:
            C[ord(ll)-ord("a")] += 1
    tmp = 0
    for i in range(26):
        if C[i] == k:
            tmp += 1

    ans = max(ans, tmp)

print(ans)

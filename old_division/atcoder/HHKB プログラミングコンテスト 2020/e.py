h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
mod = 10**9+7


ue = [[0]*w for _ in range(h)]
sita = [[0]*w for _ in range(h)]
hidari = [[0]*w for _ in range(h)]
migi = [[0]*w for _ in range(h)]

for i in range(1, h):
    for j in range(w):
        if S[i-1][j] == ".":
            ue[i][j] = ue[i-1][j]+1
        else:
            ue[i][j] = 0

l = range(h-1)
l = l[::-1]
for i in l:
    for j in range(w):
        if S[i+1][j] == ".":
            sita[i][j] = sita[i+1][j]+1
        else:
            sita[i][j] = 0

for j in range(1, w):
    for i in range(h):
        if S[i][j-1] == ".":
            migi[i][j] = migi[i][j-1]+1
        else:
            migi[i][j] = 0

l = range(w-1)
l = l[::-1]

for j in l:
    for i in range(h):
        if S[i][j+1] == ".":
            hidari[i][j] = hidari[i][j+1]+1
        else:
            hidari[i][j] = 0
ans = 0
k = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            k += 1
ans = k*pow(2, k, mod)
for i in range(h):
    for j in range(w):
        ko = ue[i][j]+migi[i][j]+hidari[i][j]+sita[i][j]
        if S[i][j] == ".":
            ko = ko+1
            ans = (ans-pow(2, k-ko, mod)) % mod


print(ans)

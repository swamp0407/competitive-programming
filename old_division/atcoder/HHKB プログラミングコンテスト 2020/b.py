h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w-1):
        if S[i][j] == "." and S[i][j+1] == ".":
            ans += 1


for i in range(w):
    for j in range(h-1):
        if S[j][i] == "." and S[j+1][i] == ".":
            ans += 1

print(ans)

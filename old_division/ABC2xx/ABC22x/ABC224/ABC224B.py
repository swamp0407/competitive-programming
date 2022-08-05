h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
for i1 in range(h):
    for i2 in range(i1+1, h):
        for j1 in range(w):
            for j2 in range(j1, w):
                if A[i1][j1]+A[i2][j2] <= A[i2][j1]+A[i1][j2]:
                    continue
                else:
                    print("No")
                    exit()

print("Yes")

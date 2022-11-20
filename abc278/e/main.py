###### 2022年 11月19日 土曜日 21時00分26秒 JST ######

from collections import defaultdict

H, W, n, h, w = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

dict = defaultdict(int)
for i in range(H):
    for j in range(W):
        dict[A[i][j]] += 1


for i in range(h):
    for j in range(w):
        dict[A[i][j]] -= 1
        if dict[A[i][j]] == 0:
            del dict[A[i][j]]


TEMP = dict.copy()


B = [0 for _ in range(H-h+1)]

B[0] = dict.copy()

for i in range(H-h+1):
    ans = []
    if i != 0:
        dict = B[i-1]
        for j in range(w):
            dict[A[i-1][j]] += 1
            dict[A[i+h-1][j]] -= 1
            if dict[A[i+h-1][j]] == 0:
                del dict[A[i+h-1][j]]
    B[i] = dict.copy()
    for j in range(W-w+1):
        if j == 0:
            pass
        else:
            for k in range(h):
                dict[A[i+k][j-1]] += 1
                dict[A[i+k][j+w-1]] -= 1
                if dict[A[i+k][j+w-1]] == 0:
                    del dict[A[i+k][j+w-1]]
        ans.append(len(dict))

    print(*ans)

# for i in range(H-h+1):
#     for j in range(W-w+1):

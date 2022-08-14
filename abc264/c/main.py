###### 2022年 8月13日 土曜日 21時00分23秒 JST ######

import itertools
h, w = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(h)]
h2, w2 = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(h2)]

r_h = h - h2
r_w = w - w2


def check(a, b):
    r_c = 0
    for row in a:
        c_c = 0
        for column in b:
            if A[row][column] != B[r_c][c_c]:
                return False
            c_c += 1
        r_c += 1

    return True


if r_h < 0 or r_w < 0:
    print("No")
    exit()
for a in itertools.combinations(range(h), h2):
    for b in itertools.combinations(range(w), w2):
        if check(a, b):
            print("Yes")
            exit()
print("No")

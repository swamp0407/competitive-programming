###### 2022年 10月15日 土曜日 21時00分19秒 JST ######
import bisect

h, w, nr, nc = map(int, input().split())

n = int(input())
blocks = {}
yoko = {}
tate = {}

for i in range(n):
    r, c = map(int, input().split())
    blocks[(r, c)] = True

    if r not in yoko:
        yoko[r] = []
    yoko[r].append(c)

    if c not in tate:
        tate[c] = []
    tate[c].append(r)

for i, l in yoko.items():
    yoko[i] = sorted(l)
for i, l in tate.items():
    tate[i] = sorted(l)


q = int(input())


for i in range(q):
    d, l = map(str, input().split())
    l = int(l)
    if d == "L":
        if nc == 1:
            print(nr, nc)
            continue
        if nr in yoko:
            t = bisect.bisect_left(yoko[nr], nc)
            if t == 0:
                nc = max(1, nc - l)
            else:
                nc = max(yoko[nr][t - 1]+1, nc-l)
        else:
            nc = max(1, nc - l)
    elif d == "R":
        if nc == w:
            print(nr, nc)
            continue
        if nr in yoko:
            t = bisect.bisect_left(yoko[nr], nc)
            if t == len(yoko[nr]):
                nc = min(w, nc + l)
            else:
                nc = min(yoko[nr][t]-1, nc+l)
        else:
            nc = min(w, nc + l)
    elif d == "U":
        if nr == 1:
            print(nr, nc)
            continue
        if nc in tate:
            t = bisect.bisect_left(tate[nc], nr)
            if t == 0:
                nr = max(1, nr - l)
            else:
                nr = max(tate[nc][t - 1]+1, nr-l)
        else:
            nr = max(1, nr - l)
    elif d == "D":
        if nr == h:
            print(nr, nc)
            continue
        if nc in tate:
            t = bisect.bisect_left(tate[nc], nr)
            if t == len(tate[nc]):
                nr = min(h, nr + l)
            else:
                nr = min(tate[nc][t]-1, nr+l)
        else:
            nr = min(h, nr + l)
    print(nr, nc)

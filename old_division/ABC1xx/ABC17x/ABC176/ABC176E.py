import heapq
h, w, m = map(int, input().split())

M = [list(map(int, input().split())) for _ in range(m)]
hh = [0]*(h+1)
ww = [0]*(w+1)
check = [[False]*(w+1) for _ in range(h+1)]
for i in range(m):
    h, w = M[i][0], M[i][1]
    hh[h] += 1
    ww[w] += 1
    check[h][w] = True
nux = 0
hhh = []
www = []
for i, ph in enumerate(hh):
    heapq.heappush(hhh, [-ph, i])

for i, pw in enumerate(ww):
    heapq.heappush(www, [-pw, i])

mh = heapq.heappop(hhh)
mhl = [mh[1]]
for dh in hhh:
    if dh[0] == mh[0]:
        mhl.append(dh[1])
    else:
        break
mw = heapq.heappop(www)
mwl = [mw[1]]
for dw in www:
    if dw[0] == mw[0]:
        mwl.append(dw[1])
    else:
        break

for hl in mhl:
    for hw in mwl:
        if check[hl][hw] == False:
            print(-mw[0]-mh[0])
            exit()

print(-mw[0]-mh[0]-1)

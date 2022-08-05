###### 2022年 6月18日 土曜日 21時00分23秒 JST ######

n = int(input())
S = []
for i in range(n):
    l, r = map(int, input().split())
    S.append((l, r))


S.sort()


# print(S)
ans = 0

pr = -1
pl = -1
first = 1
for l, r in S:
    if l > pr:
        if not first:
            print(pl, pr)
        pr = r
        pl = l
        first = 0
    elif l == pl:
        pr = r
    else:
        if r > pr:
            pr = r


print(pl, pr)

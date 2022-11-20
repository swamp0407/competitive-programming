###### 2022年 11月19日 土曜日 21時00分25秒 JST ######
n, q = map(int, input().split())


s = {}

for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if s.get(a):
            s[a][b] = 1
        else:
            s[a] = {b: 1}
    elif t == 2:
        if s.get(a):
            if s[a].get(b):
                s[a][b] = 0

    if t == 3:
        if s.get(a) and s[a].get(b) and s.get(b) and s[b].get(a):
            print("Yes")
        else:
            print("No")

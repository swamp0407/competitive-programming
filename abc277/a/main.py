###### 2022年 11月12日 土曜日 21時00分18秒 JST ######


n, x = map(int, input().split())

P = list(map(int, input().split()))

for i, p in enumerate(P):
    if p == x:
        print(i+1)
        exit()

###### 2022年 11月12日 土曜日 21時00分18秒 JST ######
n = int(input())

s = set()

ok = True
for i in range(n):
    a = input()
    if not a[0] in ['H', 'D', 'S', 'C']:
        ok = False

    if not a[1] in ['A', "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
        ok = False

    if a in s:
        ok = False

    s.add(a)


if ok:
    print("Yes")
else:
    print("No")

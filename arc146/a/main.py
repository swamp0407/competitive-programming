###### 2022年 8月20日 土曜日 21時00分17秒 JST ######
n = int(input())


A = list(map(str, input().split()))


B = []
for i, a in enumerate(A):
    B.append((len(list(a)), a))


B.sort(reverse=True)
# print(B)
anss = []
for i, b in enumerate(B):
    anss.append(b[1])
    if i == 2:
        break


anss.sort(reverse=True)

ans = 0

a = anss[0]
b = anss[1]
c = anss[2]

ans = max(list(map(int, [a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a])))


print(''.join(anss))

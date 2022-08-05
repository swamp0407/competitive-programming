###### 2022年 6月18日 土曜日 21時00分23秒 JST ######

h1, h2, h3, w1, w2, w3 = map(int, input().split())


if h1 + h2 + h3 != w1 + w2 + w3:
    print(0)
    exit()
h1 -= 3
h2 -= 3
h3 -= 3
w1 -= 3
w2 -= 3
w3 -= 3
ans = 0
for i in range(h1+1):
    for j in range(h1+1):
        if i+j > h1:
            break
        k = h1-i-j

        for l in range(h2+1):
            for m in range(h2+1):
                if l+m > h2:
                    break
                n = h2-l-m

                if i + l > w1:
                    continue

                if j + m > w2:
                    continue

                if k + n > w3:
                    continue

                ans += 1

print(ans)

###### 2022年 6月18日 土曜日 21時00分23秒 JST ######

n = int(input())

A = list(map(int, input().split()))

A = A[::-1]

B = []
s = 0
ans = 0
for a in A:
    s = s + a
    if s >= 4:
        ans += 1


print(ans)

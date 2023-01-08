###### 2023年 1月 7日 土曜日 21時00分20秒 JST ######
t = int(input())

for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        if a % 2 == 1:
            ans += 1
    print(ans)

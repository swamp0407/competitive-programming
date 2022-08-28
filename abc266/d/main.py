###### 2022年 8月27日 土曜日 21時00分19秒 JST ######
n = int(input())

Q = []
for i in range(n):
    t, x, a = map(int, input().split())
    Q.append((t, x, a))


dp = [[0] * 5 for _ in range(10**5 + 10)]
# dp[i][j] = 時刻iにおいて位置jにいるときの最大
# i = 0,1,2,...,10**5
# j = 0,1,2,3,4

sunuke = [[0] * 5 for _ in range(10**5 + 10)]

for i in range(n):
    t, x, a = Q[i]
    sunuke[t][x] += a


for i in range(4):
    for j in range(5):
        if j == 0:
            dp[i][j] = max(dp[max(i-1, 0)][0], dp[max(i-1, 0)][1], dp[max(i-2, 0)][2],
                           dp[max(i-3, 0)][3], dp[max(i-4, 0)][4]) + sunuke[i][j]
        elif j == 1:
            if i < 1:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[max(i-1, 0)][0], dp[max(i-1, 0)][1], dp[max(i-1, 0)][2],
                               dp[max(i-2, 0)][3], dp[max(i-3, 0)][4]) + sunuke[i][j]
        elif j == 2:
            if i < 2:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[max(i-2, 0)][0], dp[max(i-1, 0)][1], dp[max(i-1, 0)][2],
                               dp[max(i-1, 0)][3], dp[max(i-2, 0)][4]) + sunuke[i][j]
        elif j == 3:
            if i < 3:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[max(i-3, 0)][0], dp[max(i-2, 0)][1], dp[max(i-1, 0)][2],
                               dp[max(i-1, 0)][3], dp[max(i-1, 0)][4]) + sunuke[i][j]
        elif j == 4:
            if i < 4:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[max(i-4, 0)][0], dp[max(i-3, 0)][1], dp[max(i-2, 0)][2],
                               dp[max(i-1, 0)][3], dp[max(i-1, 0)][4]) + sunuke[i][j]


for i in range(4, 10**5+3):
    for j in range(5):
        if j == 0:
            a = max(dp[max(i-1, 0)][0], dp[max(i-1, 0)][1], dp[max(i-2, 0)][2],
                    dp[max(i-3, 0)][3], dp[max(i-4, 0)][4])
            dp[i][j] = max(dp[max(i-1, 0)][0], dp[max(i-1, 0)][1], dp[max(i-2, 0)][2],
                           dp[max(i-3, 0)][3], dp[max(i-4, 0)][4]) + sunuke[i][j]
        elif j == 1:
            dp[i][j] = max(dp[max(i-1, 0)][0], dp[max(i-1, 0)][1], dp[max(i-1, 0)][2],
                           dp[max(i-2, 0)][3], dp[max(i-3, 0)][4]) + sunuke[i][j]
        elif j == 2:
            dp[i][j] = max(dp[max(i-2, 0)][0], dp[max(i-1, 0)][1], dp[max(i-1, 0)][2],
                           dp[max(i-1, 0)][3], dp[max(i-2, 0)][4]) + sunuke[i][j]
        elif j == 3:
            dp[i][j] = max(dp[max(i-3, 0)][0], dp[max(i-2, 0)][1], dp[max(i-1, 0)][2],
                           dp[max(i-1, 0)][3], dp[max(i-1, 0)][4]) + sunuke[i][j]
        elif j == 4:
            dp[i][j] = max(dp[max(i-4, 0)][0], dp[max(i-3, 0)][1], dp[max(i-2, 0)][2],
                           dp[max(i-1, 0)][3], dp[max(i-1, 0)][4]) + sunuke[i][j]

print(max(dp[10**5+2]))

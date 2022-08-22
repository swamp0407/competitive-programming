###### 2022年 8月21日 日曜日 21時00分20秒 JST ######
n, m, t = map(int, input().split())

A = list(map(int, input().split()))

heals = [0]*n
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    heals[x] = y
# print(t, heals, A)

now = 0

while t > 0:
    if now == n-1:
        print("Yes")
        exit()
    t += heals[now]
    t -= A[now]
    now += 1


print("No")

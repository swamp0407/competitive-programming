###### 2022年 8月21日 日曜日 21時00分20秒 JST ######
x, y, n = map(int, input().split())


ans = n*x

ans = min(ans, y*(n//3) + (n % 3)*x)

print(ans)
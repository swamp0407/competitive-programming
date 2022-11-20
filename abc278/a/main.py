###### 2022年 11月19日 土曜日 21時00分25秒 JST ######
n, k = map(int, input().split())

A = list(map(int, input().split()))

for i in range(k):
    A = A[1:] + [0]

print(*A)

###### 2022年 11月20日 日曜日 21時00分13秒 JST ######
n, l = map(int, input().split())
A = list(map(int, input().split()))


s = -1

for i, a in enumerate(A[::-1]):
    if a == 2:
        s = n-i-1
        break

if s == -1:
    print("Yes")
    exit()

if s == 0:
    print("Yes")
    exit()

t = 0
for i in range(s):
    a = A[i]
    if a == 1:
        t += 2
    else:
        t += 3

if t >= l-1:
    print("No")
    exit()
print("Yes")

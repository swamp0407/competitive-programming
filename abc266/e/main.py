###### 2022年 8月27日 土曜日 21時00分19秒 JST ######


n = int(input())

c = 11/6+2/3*4.25
# print(c)
d = 11/6 + 2/3*c

# print(d)


e = 11/6+2/3*d

# print(e)  # 5回目

if n == 1:
    print(3.5)
elif n == 2:
    print(4.25)
elif n == 3:
    print(11/6+2/3*4.25)
elif n == 4:
    print(d)
elif n == 5:
    print(e)
else:
    for i in range(n-5):
        e = 1+e*(5/6)
    print(e)


memo = [0 for i in range(n+1)]

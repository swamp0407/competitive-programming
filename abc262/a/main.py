###### 2022年 7月31日 日曜日 21時00分22秒 JST ######

y = int(input())


a = y % 4

if a == 2:
    print(y)
elif a == 3:
    print(y+3)
elif a == 0:
    print(y+2)
elif a == 1:
    print(y+1)

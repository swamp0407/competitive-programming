###### 2022年 8月13日 土曜日 21時00分23秒 JST ######

r, c = map(int, input().split())


if r == 1 or r == 15 or c == 1 or c == 15:
    print("black")
    exit()

elif r == 2 or r == 14 or c == 2 or c == 14:
    print("white")
elif r == 3 or r == 13 or c == 3 or c == 13:
    print("black")
elif r == 4 or r == 12 or c == 4 or c == 12:
    print("white")
elif r == 5 or r == 11 or c == 5 or c == 11:
    print("black")
elif r == 6 or r == 10 or c == 6 or c == 10:
    print("white")
elif r == 7 or r == 9 or c == 7 or c == 9:
    print("black")
elif r == 8 or r == 8 or c == 8 or c == 8:
    print("white")

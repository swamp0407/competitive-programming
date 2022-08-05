###### 2022年 7月30日 土曜日 21時07分34秒 JST ######

n = int(input())

S = list(input())

RS = S[::-1]
life = 1
for i in range((n+1)//2):
    if S[i] != RS[i]:
        life = 0
        CS = S[::]
        CS[i] = "A"
        CS[i+1] = "B"
        CRS = RS[::]
        CRS[i] = "B"
        CRS[i+1] = "A"
        if CS == CS[::-1]:
            print("Yes")
            exit()
        if CRS == CRS[::-1]:
            print("Yes")
            exit()
        print("No")
        exit()


print("Yes")

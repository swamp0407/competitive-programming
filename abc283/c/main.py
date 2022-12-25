###### 2022年 12月24日 土曜日 21時00分19秒 JST ######

S = input()

i = 0
ans = 0
while i < len(S):
    if S[i] == '0':
        if i+1 < len(S) and S[i+1] == '0':
            ans += 1
            i += 2
            continue

    i += 1
    ans += 1


print(ans)

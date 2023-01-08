###### 2023年 1月 7日 土曜日 21時00分20秒 JST ######
import string

n = int(input())
t = input()
S = {i: 0 for i in string.ascii_lowercase}

for s in t:
    S[s] += 1

for i in S:
    if S[i] % 2 == 1:
        print(-1)
        exit()

###### 2023年 1月 7日 土曜日 21時00分20秒 JST ######
n = int(input())
S = [input() for _ in range(n)]

S = S[::-1]

for i in range(n):
    print(S[i])

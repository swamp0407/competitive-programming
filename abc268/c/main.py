###### 2022年 9月10日 土曜日 21時01分05秒 JST ######

n = int(input())

P = list(map(int, input().split()))


d = {}

for i, p in enumerate(P):
    d[p] = i


s = [0] * n

for i in range(n):
    a = (i - d[i])

    s[a % n] += 1
    s[(a+1) % n] += 1
    s[(a-1) % n] += 1


print(max(s))

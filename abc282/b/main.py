###### 2022年 12月17日 土曜日 21時00分29秒 JST ######


n, m = map(int, input().split())


S = [list(input()) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(m):
            if (S[i][k] != "o" and S[j][k] != "o"):
                break
        else:
            ans+=1
        

print(ans)

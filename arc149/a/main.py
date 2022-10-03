###### 2022年 10月 2日 日曜日 21時00分08秒 JST ######
n,m = map(int,input().split())


def check(x):
    return len(set(list(str(x))))==1 and x < 10**n and x%m==0

# print(check(222222))

d = [i % m for i in range(10)]

ans = 0

# for i in range(1,100):
#     if check(i):
#         ans =(1,i)
#         ans2 = i

# if n <=2:
#     print(ans2)
#     exit()




for i in range(n):
    for j in range(1,10):
        if d[j] == 0:
            ans = (i,j)
        d[j] = (d[j] * 10 + j)%m

    # print(d)

if ans  == 0:
    print(-1)
    exit()

print(str(ans[1]) * (ans[0]+1))

###### 2022年 12月24日 土曜日 21時00分19秒 JST ######

n = int(input())
A = list(map(int, input().split()))
q = int(input())
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A[query[1]-1] = query[2]
    else:
        print(A[query[1]-1])

###### 2022年 11月19日 土曜日 21時00分26秒 JST ######


from collections import defaultdict
n = int(input())

A = list(map(int, input().split()))

q = int(input())


a = 0
first = 1

dict = defaultdict(int)

for i in range(q):
    s = input().split()
    if s[0] == "1":
        if first == 1:
            first = 0
        a = int(s[1])
        dict = defaultdict(int)
    elif s[0] == "2":
        b = int(s[1])
        c = int(s[2])
        dict[b-1] += c

    else:
        if first == 1:
            print(A[int(s[1])-1]+dict[int(s[1])-1])
        else:
            print(a+dict[int(s[1])-1])

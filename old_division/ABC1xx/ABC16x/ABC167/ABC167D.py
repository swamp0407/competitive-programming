n, k = map(int, input().split())
a = list(map(int, input().split()))

b = [-1]*(n+1)
i = 0  # 回数
num = 1  # 場所
for j in range(k):
    if b[num] != -1:
        shu = i-b[num]
        ans = b[num]+(k-b[num]) % shu
        print(b.index(ans))
        exit()
    b[num] = i
    num = a[num-1]
    i += 1
print(num)

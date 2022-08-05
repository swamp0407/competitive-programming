k = int(input())
now = 0
for i in range(1, 10**6+10):
    now = now*10+7
    now = now % k
    if now == 0:
        print(i)
        exit()
print(-1)

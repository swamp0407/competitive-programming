n = int(input())
a = 100
for i in range(1, 10**9+7):
    a = int(1.01*a)
    if n <= a:
        print(i)
        exit()

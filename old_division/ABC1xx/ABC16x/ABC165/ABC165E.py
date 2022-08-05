n, m = map(int, input().split())

if n % 2 == 1:
    for i in range(m):
        print(1+i, n-1-i)
else:
    for i in range(m):
        if i % 2 == 0:
            print(n//2-i//2, n//2+1+i//2)
        else:
            print(1+i//2, n-1-i//2)

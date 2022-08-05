a, b = list(map(int, input().split()))
c = list(map(int, input().split()))
for i in range(b):
    a = a-c[i]

if a >= 0:
    print(a)
else:
    print(-1)

a, b, c, d = map(int, input().split())

for i in range(1000):
    a = a-d
    c = c-b
    if c <= 0:
        print("Yes")
        break
    if a <= 0:
        print("No")
        break

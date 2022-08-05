a, b, c = map(int, input().split())
k = int(input())

for i in range(k):
    print(1)
    if a >= b:
        b = b*2
    else:
        c = c*2


if a < b and b < c:
    print("Yes")
else:
    print("No")

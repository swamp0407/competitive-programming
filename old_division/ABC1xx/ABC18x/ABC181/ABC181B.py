n = int(input())
num = 0
for i in range(n):
    a, b = map(int, input().split())

    num += (b-a+1)*(a+b)/2

print(int(num))

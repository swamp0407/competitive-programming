n = int(input())
num = 0
sum = 0
for i in range(1, n+1, 2):
    for j in range(1, n+1):
        if i % j == 0:
            num += 1
    if num == 8:
        sum += 1
    num = 0
print(sum)

a, b, c, k = map(int, input().split())
sum = k
if k > a:
    sum = a
    if k-a <= b:
        sum = a
    else:
        sum = 2*a+b-k
print(sum)

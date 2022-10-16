
x, k = map(int, input().split())

for i in range(k):
    s = x // (10 ** i)
    if s % 10 < 5:
        x = x - (s % 10) * (10 ** i)
    else:
        x = x + (10 - s % 10) * (10 ** i)
print(x)

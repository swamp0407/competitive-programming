n, k = map(int, input().split())
d = []
for i in range(k):
    input()
    d = d+(list(map(int, input().split())))

d = list(set(d))
print(n-len(d))

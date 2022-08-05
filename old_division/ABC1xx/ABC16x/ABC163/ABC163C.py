a = int(input())
c = list(map(int, input().split()))
d = [0] * a

for i in range(a-1):
    d[c[i]-1] = d[c[i]-1]+1

for i in range(a):
    print(d[i])

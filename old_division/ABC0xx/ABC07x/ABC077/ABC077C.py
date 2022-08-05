import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
sum = 0
for i in b:
    sum += bisect.bisect_left(a, i)*(n-bisect.bisect_right(c, i))

print(sum)

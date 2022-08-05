from itertools import combinations
n = int(input())
x = [0]*n
y = [0]*n

for i in range(n):
    x[i], y[i] = map(int, input().split())


l = range(n)

for a, b, c in combinations(l, 3):
    if x[b] == x[a]:
        if x[a] == x[c]:
            print("Yes")
            exit()
    else:
        num = y[a]+(x[c]-x[a])*(y[b]-y[a])/(x[b]-x[a])
        if num == float(y[c]):
            print("Yes")
            exit()

print("No")

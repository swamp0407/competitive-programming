from collections import defaultdict
n = int(input())
X = defaultdict(int)
Y = defaultdict(int)
for i in range(n):
    x, y, p = map(int, input().split())
    X[x] = X[x]+p
    Y[y] = Y[y]+p
X = X.items()
X = list(X)
Y = Y.items()
Y = list(Y)
print(X)




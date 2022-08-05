import numpy as np

A = np.array(open(0).read().split(), np.int64)[1:]
N = len(A)

K = 30

X = np.append(A, 0)
sums = np.zeros(len(X), np.int64)

for k in range(K):
    one = X >> k & 1
    x1 = np.sum(one)
    x0 = N - x1
    sums += (x1 - (x1 - x0) * one) << k

ANS = sums.max()
print(ANS)

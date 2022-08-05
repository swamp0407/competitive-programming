from bisect import bisect_left
n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


pos = [0]*(n+1)
z = [10**9]*n
for i in range(n):
    pos[Q[i]] = i

for i in P:
    ls = []
    for j in range(i, n+1, i):
        ls.append(pos[j])
    ls.sort()
    ls.reverse()

    for j in ls:
        z[bisect_left(z, j)] = j


print(bisect_left(z, 10**9))

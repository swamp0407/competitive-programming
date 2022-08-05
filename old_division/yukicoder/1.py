from collections import deque
n = int(input())

l = [-1]*n

l[0] = 1
q = deque([0])

while q:
    x = q.popleft()
    bx = bin(x+1).count("1")
    if x+bx < n and l[x+bx] == -1:
        l[x+bx] = l[x]+1
        q.append(x+bx)
    if x-bx >= 0 and l[x-bx] == -1:
        l[x-bx] = l[x]+1
        q.append(x-bx)

print(l[n-1])

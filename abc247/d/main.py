from collections import deque
q = int(input())

d = deque()

for i in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        # print(query)
        d.append((query[1], query[2]))
    else:
        c = 0
        ans = 0
        while True:
            a = d.popleft()
            if query[1] == a[1]:
                ans += a[0]*a[1]
                break
            elif query[1] > a[1]:
                ans += a[0]*a[1]
                query[1] -= a[1]
            else:
                ans += a[0]*query[1]
                d.appendleft([a[0], a[1]-query[1]])
                break
        print(ans)

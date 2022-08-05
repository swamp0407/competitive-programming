import heapq
n = int(input())

P = map(int, input().split())

l = list(range(0, 200010))
heapq.heapify(l)
visited = [True]*(200000+10)
for p in P:
    visited[p] = False
    while 1:
        if visited[l[0]]:
            print(l[0])
            break
        else:
            heapq.heappop(l)

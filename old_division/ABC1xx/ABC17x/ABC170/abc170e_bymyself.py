from heapq import heappop, heappush, heapify
n, q = map(int, input().split())
inf = 2*10**5+10


def max_in_cls(q):
    while B[q]:
        rate, hito = B[q][0]
        if clase[hito] == q:
            return -rate
        heappop(B[q])
    return 0


B = [[] for _ in range(inf)]
clase = [[] for _ in range(inf)]
rates = [[] for _ in range(n+1)]
for i in range(1, n+1):
    a, b = map(int, input().split())
    clase[i] = b
    rates[i] = a
    heappush(B[b], [-a, i])
C = []
for i in range(inf):
    if B[i] != []:
        heappush(C, [max_in_cls(i), i])


for i in range(q):
    c, after = map(int, input().split())
    before = clase[c]
    clase[c] = after
    heappush(B[after], [-rates[c], c])
    a = max_in_cls(before)
    b = max_in_cls(after)
    if a != 0:
        heappush(C, [a, before])
    if b != 0:
        heappush(C, [b, after])
    while C:
        rate, clases = C[0]
        if rate == max_in_cls(clases):
            print(rate)
            break
        heappop(C)

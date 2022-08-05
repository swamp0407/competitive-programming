import time
N = int(input())

A = [list(map(int, input().split())) for _ in range(N*2-1)]

nax = 0


def cul(point, used):
    for i in range(2*N):
        if not used[i]:
            si = i
            break
    else:
        global nax
        nax = max(nax, point)
        return point

    for i in range(2*N):
        if not used[i] and si != i:
            used[i] = 1
            used[si] = 1
            # print(si, i)
            cul(point ^ A[si][i-si-1], used)
            used[i] = 0
            used[si] = 0


start = time.time()
cul(0, [False for _ in range(2*N)])

# print(time.time()-start)

print(nax)

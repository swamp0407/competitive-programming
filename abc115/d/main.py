n, x = map(int, input().split())


Level = [[] for _ in range(100)]


Level[0] = (1, 1)

for i in range(n+2):
    S = Level[i][0] * 2+3
    p = Level[i][1] * 2+1
    Level[i+1] = (S, p)


def cul(N, x):

    if x == 1:
        if N == 0:
            return 1
        return 0

    if x < Level[N-1][0]+1:
        return cul(N-1, x-1)

    if x == Level[N-1][0]+1:
        return Level[N-1][1]

    if x == Level[N-1][0]+2:
        return Level[N-1][1]+1
    if x == Level[N][0]:
        return Level[N][1]
    if x > Level[N-1][0]+2:
        return Level[N-1][1]+1+cul(N-1, x - Level[N-1][0]-2)


print(cul(n, x))

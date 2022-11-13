###### 2022年 11月13日 日曜日 11時50分23秒 JST ######

n = int(input())

XYZ = [list(map(int, input().split())) for _ in range(n)]


def cul(x1, y1, z1, x2, y2, z2):
    return abs(x1-x2) + abs(y1-y2) + max(0, z2-z1)


d = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        d[i][j] = cul(*XYZ[i], *XYZ[j])


dist = [[float("inf") for _ in range(n)] for _ in range(1 << n)]

# for i in range(n):
#     dist[1 << i][i] = d[0][i]
dist[0][0] = 0

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            continue
        for k in range(n):
            if i == 0 or i & (1 << k):
                dist[i | (1 << j)][j] = min(dist[i | (1 << j)]
                                            [j], dist[i][k] + d[k][j])


# for i in range(1 << n):
#     for k in range(n):
#         if i != 0 and not i & (1 << k):
#             continue
#         for j in range(n):
#             if i & (1 << j):
#                 continue
#             dist[i | (1 << j)][j] = min(dist[i | (1 << j)]
#                                             [j], dist[i][k] + d[k][j])


print(dist[-1][0])

"""
    ###### 2022年 11月13日 日曜日 11時50分23秒 JST ######

n = int(input())

XYZ = [list(map(int, input().split())) for _ in range(n)]


def cul(x1, y1, z1, x2, y2, z2):
    return abs(x1-x2) + abs(y1-y2) + max(0, z2-z1)


d = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        d[i][j] = cul(*XYZ[i], *XYZ[j])


dist = [[float("inf") for _ in range(n)] for _ in range(1 << n)]

for i in range(n):
    dist[1 << i][i] = d[0][i]


for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            continue
        for k in range(n):
            if i & (1 << k):
                dist[i | (1 << j)][j] = min(dist[i | (1 << j)]
                                            [j], dist[i][k] + d[k][j])


print(dist[-1][0])
    """

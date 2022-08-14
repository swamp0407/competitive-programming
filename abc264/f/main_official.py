###### 2022年 8月13日 土曜日 21時00分23秒 JST ######

import time
start = time.time()
h, w = map(int, input().split())


R = list(map(int, input().split()))
C = list(map(int, input().split()))

A = [list(map(int, list(input()))) for _ in range(h)]
print(time.time()-start, "入出力")


def solve():
    print(time.time()-start, "solve 開始")

    dp = [[[[10**12] * 2 for _ in range(2)]
           for _ in range(2005)] for _ in range(2005)]

    # dp[i][j][k][l] := (i,j)にいるときにkを向いている方向にl回flipしたときの最小コスト
    for i in range(2):
        j = A[0][0] ^ i
        dp[0][0][0][j] = i * R[0] + j * C[0]  # 下を向いている j == 1 だと 0列をflip
        dp[0][0][1][i] = i * R[0] + j * C[0]  # 右を向いている i == 1 だと 0行をflip

    dij = [(1, 0), (0, 1)]

    for i in range(h):
        for j in range(w):
            for k in range(2):  # k== 0 下を向いている　k == 1 右を向いている
                for l in range(2):
                    ni = i + dij[k][0]
                    nj = j + dij[k][1]
                    if ni < 0 or ni >= h or nj < 0 or nj >= w:
                        continue

                    flip = A[ni][nj] ^ l
                    cost = 0
                    if k == 0:  # 下を向いている nI行をflip
                        cost = flip * R[ni]
                    else:  # 右を向いている nj列をflip
                        cost = flip * C[nj]
                    for nk in range(2):
                        nl = l
                        if k != nk:
                            nl = flip
                        dp[ni][nj][nk][nl] = min(
                            dp[ni][nj][nk][nl], dp[i][j][k][l] + cost)

    ret = float("inf")
    for i in range(2):
        for j in range(2):
            ret = min(ret, dp[h-1][w-1][i][j])
    print(time.time()-start, "solve 終了")

    return ret


ans = solve()

for i in range(h):
    for j in range(w):
        A[i][j] ^= 1

ans = min(ans, solve())

print(ans)

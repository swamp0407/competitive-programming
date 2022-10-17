# 解説見てからの挑戦

import bisect  # .bisect_left(list, key)
import sys
from itertools import product


def input(): return sys.stdin.readline().rstrip()


def main():
    # 入力
    N, X = map(int, input().split())
    wall = list(map(int, input().split()))
    hammer = list(map(int, input().split()))
    # 計算・出力
    P = [[0, -1, 0], [X, -1, 0]]  # 座標, 対応するidx, 種類 [ゴール, 壁, ハンマー]
    for i in range(N):
        P.append([wall[i], i, 1])
        P.append([hammer[i], i, 2])
    P.sort()
    START = bisect.bisect_left(P, [0, -1, 0])
    GOAL = bisect.bisect_left(P, [X, -1, 0])
    # print(P)
    # print(START, GOAL)
    if START < GOAL:  # GOALが右側にある
        L = START  # start から左側にあるイベントの個数
        R = GOAL - START  # start から ゴールまでのイベントの個数(ゴールを含む)
        O = 1
    else:
        L = START - GOAL
        # start から右側にあるイベントの個数 スタートの分 -1をしている スタートが右端で10こあるとき スタートは9になるので
        R = len(P) - 1 - START
        O = 0
    # print(L, R, O)
    # dp[i][j][k] i:左側のイベントの個数 j:右側のイベントの個数 k:0:左にいる 1:右にいる
    dp = [[[10**15, 10**15] for __ in range(R+1)] for _ in range(L+1)]
    dp[0][0] = [0, 0]
    # dp[l][r] -> dp[l+1][r]
    for l, r, n in product(range(L+1), range(R+1), range(2)):
        prevX = P[START + (-l if n == 0 else r)][0]  # 前のイベントの座標　スタートから左にl個右にr個
        # print(l, r, n)
        # l + 1 を見る
        if l < L:
            x, idx, p = P[START - l - 1]
            if p != 1 or x <= hammer[idx] <= P[START + r][0]:
                dp[l+1][r][0] = min(dp[l+1][r][0], dp[l][r]
                                    [n] + abs(prevX - x))
        # n = 0のときは左にいる 1のときは右にいるのでそれぞれからの距離を計算
        # r + 1 を見る
        if r < R:
            x, idx, p = P[START + r + 1]
            if p != 1 or P[START - l][0] <= hammer[idx] <= x:
                dp[l][r+1][1] = min(dp[l][r+1][1], dp[l][r]
                                    [n] + abs(prevX - x))
        # pprint(dp)
    if O == 1:
        # ゴールが右側にあるので dp[i][R][1]を見ていく　(右側にいてスタートからR番目のイベント（ゴール）にいる)
        ans = min([dp[l][R][1] for l in range(L+1)])
    else:
        ans = min([dp[L][r][0] for r in range(R+1)])
    if ans == 10**15:
        ans = -1
    print(ans)


if __name__ == "__main__":
    main()

###### 2022年 9月10日 土曜日 21時01分05秒 JST ######


import itertools
n = int(input())
S = [input() for _ in range(n)]


def cul(S):
    ans = 0
    c = 0
    for s in S:
        if s == "X":
            c += 1
        else:
            ans += c * int(s)

    return ans


def cul2(S):
    ans = 0
    c = 0
    d = 0
    for s in S:
        if s == "X":
            c += 1
        else:
            ans += c * int(s)
            d += int(s)

    return ans, c, d, len(S)


l = [i for i in range(n)]
for v in itertools.permutations(l):
    T = ""
    for a in v:
        T += S[a]
    print(cul(T))


for s in S:
    ans, c, d, e = cul2(s)
    print(f"ans = {ans}, xの数 = {c}, 数字の和 = {d}, 数列の長さ = {e}")

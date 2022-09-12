###### 2022年 9月10日 土曜日 21時01分05秒 JST ######

import itertools
n, m = map(int, input().split())

S = [input() for _ in range(n)]

T = [input() for _ in range(m)]

S.sort(key=lambda x: -len(x))

a = 0
for s in S:
    a += (len(s))


if n == 1 and a <= 2:
    print(-1)
    exit()


X = {}
for t in T:
    X[t] = 1


def dfs(v, remain, ans):
    if len(v) == 0:
        if X.get(ans) is None:
            print(ans)
            exit()
        return

    t = S[v[0]]
    if ans == "":
        dfs(v[1:], remain, t)
    else:
        for i in range(remain+1):
            dfs(v[1:], remain-i, ans + "_"*i + "_" + t)


l = [i for i in range(n)]
b = 16 - a-(n-1)
for v in itertools.permutations(l):
    dfs(v, b, "")

print(-1)

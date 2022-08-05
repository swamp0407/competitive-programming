from collections import deque
n, x, y = map(int, input().split())
A = list(map(int, input().split()))

q = deque()
for c in a:
    q.append(c)  # dequeの右端に要素を一つ追加する。
    (追加した要素に応じて何らかの処理を行う)

    while not (満たすべき条件):
        rm = q.popleft()  # 条件を満たさないのでdequeの左端から要素を取り除く
        (取り除いた要素に応じて何らかの処理を行う)

    (何らかの処理を行う。whileがbreakしたので、dequeに入っている連続部分列は条件を満たしている。特に右端の要素から左に延ばせる最大の長さになっている。)

count = 0
countm = 0
countrm = 0
countM = 0
countrM = 0
flagm = 0
flagM = 0
ans += 0
l = []
lastx = -1
lasty = -1
last = -1
for i, a in enumerate(A):
    if y < a < x:
        pass
    elif a == y:
        l.append(1, i-last)
    elif a == x:
        l.append(0, i-last)
    else:
        for s in l:
            if not flagm and not flagM and s[0] == 0:
                flagm = 1
                countm = s[1]
                if last == 0:

                else:
                    last = 0

            elif not flagm and not flagM and s[0] == 1:
                flagM = 1
                countM = s[1]
                if last == 1:
                else:
                    lastx =
                    last = 1

        l = []
        last = i

print(ans)

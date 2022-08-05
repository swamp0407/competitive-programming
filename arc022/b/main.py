# しゃくとり法
"""
    ポイント
    right =0 の初期化
    right の追加は判定の直後
    right+=1の後には追加しない
    """

# 解説AC
from collections import deque
n = int(input())
A = list(map(int, input().split()))


res = 0
right = 0
l = set()
ans = 0
for left in range(n):
    while right < n and not A[right] in l:
        l.add(A[right])
        right += 1

    ans = max(ans, right-left)

    if right == left:
        right += 1
    else:
        l.discard(A[left])


print(ans)
q = deque()
for c in a:
    q.append(c)  # dequeの右端に要素を一つ追加する。
    (追加した要素に応じて何らかの処理を行う)

    while not (満たすべき条件):
        rm = q.popleft()  # 条件を満たさないのでdequeの左端から要素を取り除く
        (取り除いた要素に応じて何らかの処理を行う)

    (何らかの処理を行う。whileがbreakしたので、dequeに入っている連続部分列は条件を満たしている。特に右端の要素から左に延ばせる最大の長さになっている。)


move = ([1, 0], [-1, 0], [0, 1], [0, -1])
# move = ([-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]) #縦横斜め移動
# 歩数カウント不要ならvisited = set([])として、都度visited.add(new_x+new_y*C)して管理する方法も可


def bfs(sy, sx, gy, gx):
    queue = deque([[sy, sx]])
    visited = [[-1]*C for j in range(R)]
    visited[sy][sx] = 0
    while queue:
        y, x = queue.popleft()
        if [y, x] == [gy, gx]:
            return visited[y][x]
        for dy, dx in move:
            new_y, new_x = y+dy, x+dx
            if maze[new_y][new_x] == "." and visited[new_y][new_x] == -1:
                visited[new_y][new_x] = visited[y][x] + 1
                queue.append([new_y, new_x])


R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1

maze = [input() for i in range(R)]
print(bfs(sy, sx, gy, gx))

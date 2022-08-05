
n, q = map(int, input().split())

X = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False]*n
# 統合部


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged


def merge_center(left, right, center):
    merged = []
    l_i, r_i = 0, 0
    ok = 0
    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            if not ok and left[l_i] > center:
                merged.append(center)
                ok = 1
                continue
            merged.append(left[l_i])
            l_i += 1
        else:
            if not ok and right[r_i] > center:
                merged.append(center)
                ok = 1
                continue
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        for i in range(l_i, len(left)):
            if ok:
                merged.extend(left[l_i:])
                break
            if left[l_i] > center and not ok:
                merged.append(center)
                merged.extend(left[i:])
                break
            merged.append(left[i])
    if r_i < len(right):
        for i in range(r_i, len(right)):
            if ok:
                merged.extend(right[r_i:])
                break
            if right[r_i] > center and not ok:
                merged.append(center)
                merged.extend(right[i:])
                break
            merged.append(right[i])
    if not ok:
        merged.append(center)
    return merged


ans = {}


def search(x):
    can = []
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            can.append(i)
    if len(can) == 0:
        ans[x] = [X[x]]
        return ans[x]
    if len(can) == 1:
        ans[x] = sorted((search(can[0])+[X[x]]))
        return ans[x]
    if len(can) == 2:
        ans[x] = sorted(search(can[0])+search(can[1])+[X[x]])
        return ans[x]
    arr = []
    for i in range(len(can)):
        arr += search(can[i])
    ans[x] = sorted(arr)
    return ans[x]


visited[0] = True
search(0)

# print(ans)
for i in range(q):
    v, k = map(int, input().split())
    print(ans[v-1][-k])

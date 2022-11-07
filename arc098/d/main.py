###### 2022年 11月 7日 月曜日 12時47分25秒 JST ######

n = int(input())
A = list(map(int, input().split()))


d = {}


keys = [[] for _ in range(n)]
for j, a in enumerate(A):
    s = 1
    i = 0
    while s <= a:
        if a & s:
            keys[j].append(i)
        s *= 2
        i += 1


def check(C):
    for k, v in C.items():
        if v > 1:
            return False
    return True


C = {}
ans = 0
left = 0
right = 0
ans = -1
while right < len(A):
    for c in keys[right]:
        C[c] = C.get(c, 0) + 1
    while not check(C):  # 条件を満たすまでlを増やす
        # 現在のleftの値を消す前に条件を更新:
        for c in keys[left]:
            C[c] -= 1
        # print(C)
        left += 1  # leftを増やす
    ans += (right - left+1)
    right += 1  # rightを増やす

print(ans)

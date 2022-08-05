n, m, q = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(q)]

a = [[] for _ in range(n+1)]  # nさんが解いた問題

b = [n]*(m+1)  # 配点


for s in S:
    if s[0] == 1:
        num = 0
        for i in a[s[1]]:
            num += b[i]
        print(num)
    elif s[0] == 2:
        a[s[1]].append(s[2])
        b[s[2]] -= 1

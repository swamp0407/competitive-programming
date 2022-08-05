###### 2022年 7月31日 日曜日 21時00分22秒 JST ######

n, m = map(int, input().split())

G = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        for k in range(j, n+1):
            if i in G[j] and j in G[k] and k in G[i]:
                ans += 1
print(ans)

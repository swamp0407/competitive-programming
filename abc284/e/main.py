###### 2023年 1月 7日 土曜日 21時00分20秒 JST ######
import sys

n, m = map(int, input().split())


graph = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    graph[u].append(v)
    graph[v].append(u)

ans = 0

visit = [False]*n


sys.setrecursionlimit(10**7)


def dfs(s):
    global ans
    if visit[s]:
        return
    ans += 1
    if ans >= 10**6:
        print(10**6)
        exit()
    visit[s] = True
    for i in graph[s]:
        dfs(i)
    visit[s] = False


dfs(0)
print(ans)

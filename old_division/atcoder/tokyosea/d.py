n = int(input())

S = [list(map(int, input().split())) for _ in range(n)]
q = int(input())

vl = [list(map(int, input().split())) for _ in range(q)]

dp = [[-1]*(10**5+10) for _ in range(n+1)]


def knapsack(v, L):
    if v == 1:
        if S[v-1][1] > L:
            dp[v][L] = 0
            return 0
        else:
            dp[v][L] = S[v-1][0]
            return S[v-1][0]
    if dp[v][L] != -1:
        return dp[v][L]
    if L < S[v-1][1]:
        dp[v][L] = knapsack(v//2, L)
    else:
        #print(knapsack(v//2, L))
        #print(knapsack(v//2, L-S[v-1][1])+S[v-1][0])
        dp[v][L] = max(knapsack(v//2, L),
                       knapsack(v//2, L-S[v-1][1])+S[v-1][0])
    return dp[v][L]


for v, L in vl:
    print(knapsack(v, L))

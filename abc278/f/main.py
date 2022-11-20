# # ###### 2022年 11月19日 土曜日 21時00分26秒 JST ######
# # n = int(input())

# # S = []
# # for i in range(n):
# #     S.append(input())


# # dist = [[-float("inf") for _ in range(n)] for _ in range(n)]

# # G = [[] for _ in range(n)]

# # for i in range(n):
# #     for j in range(n):
# #         if i == j:
# #             pass
# #         if S[i-1][-1] == S[j-1][0]:
# #             dist[i][j] = 1
# #             G[i].append(j)

# # print(dist)
# # print(G)
# # dp = [[-float("inf") for _ in range(n)] for _ in range(1 << n)]
# # for i in range(n):
# #     dp[1 << i][i] = dist[0][i]


# # for i in range(n):
# #     if G[i] == []:
# #         print("first")
# #         exit()


# # def popcount(x): return bin(x).count("1")


# # nax = 1

# # INF = 10**18


# # def rec(S, v):
# #     if S == 0:
# #         return False

# #     if S & (1 << v) == 0:
# #         return False

# #     a = (n-popcount(S)) % 2

# #     if a == 0:

# #         print("先行")
# #             return True
# #         return False

# #     else:
# #         if any():
# #             False
# #         return True


# # ans = rec((1 << n)-1, 0)

# # if ans:
# #     print("first")
# # else:
# #     print("second")


# n = int(input())
# S = []
# for i in range(n):
#     s = input()
#     S.append(s)

# dp = [[0 for _ in range(26)] for _ in range(n)]

# for bit in range(1<<n):
#     for c in range(n):
#         if bit & (1<<c):


# n = int(input())
# S = []
# for i in range(n):
#     S.append(input())


# memo = {}


# def calc(bit, tmp):
#     if (bit << 5)+tmp in memo:
#         return memo[(bit << 5)+tmp]
#     flag = False
#     for i in range(n):
#         if (bit >> i) & 1 == 0:
#             if bit == 0 or S[tmp][-1] == S[i][0]:
#                 if calc(bit+(1 << i), i) == False:
#                     flag = True
#     memo[(bit << 5)+tmp] = flag
#     return flag


# if calc(0, -1):
#     print('First')
# else:
#     print('Second')


N = int(input())
S = [input() for _ in range(N)]
dp = [[False]*N for _ in range(1 << N)]

m = 1 << N

dp = [[False]*N for _ in range(1 << N)]


def rec(life, s):
    if life == 0:
        return False

    for k in range(N):
        if (life >> k) & 1:
            if life == m-1 or S[s][-1] == S[k][0]:
                if not rec(life ^ (1 << k), k):
                    return True
    return False


print("First" if rec(m-1, -1) else "Second")

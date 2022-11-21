# ###### 2022年 11月20日 日曜日 21時00分13秒 JST ######

# import itertools
# import operator
# n, l = map(int, input().split())

# A = list(map(int, input().split()))


# A = A + [2*l-a for a in A[::-1]]
# cumsum = [0] + list(itertools.accumulate(A, func=operator.add))


# print(A)
# print(cumsum)


# diff = [A[0]*2]+[A[i+1] - A[i] for i in range(2*n-1)]


# ans = 2*l

# s = 0
# t = 0

# # 尺取り法で最大値を求めるやり方。left = 0, right = 0, ans = -1としておく。leftとrightはそれぞれ左端と右端のインデックスを表す。区間は[left, right]（rightを含む）であり空文字は無し。
# d = {}
# left = 0
# right = 0
# ans = -1


# def check():
#     return (True or Falseを返す)


# while right < 2*n:
#     if:
#         d[s[right]] = d.get(s[right], 0) + 1
#     while not check():  # 条件を満たすまでlを増やす
#         # 現在のleftの値を消す前に条件を更新:
#         if s[left].islower():
#             if d[s[left]] == 0:
#                 del d[s[left]]
#         left += 1  # leftを増やす
#     ans = max(ans, right - left + 1)
#     right += 1　  # rightを増やす


N, L = list(map(int, input().split()))
A = list(map(int, input().split()))
# import random

# N = random.randint(1, 20)
# L = random.randint(1, 30)

# A = [random.randint(1, L) for _ in range(N)]
# A.sort()

B = [L - a for a in A][::-1]
# print(N, L)
# print(A, B)


def sol1():
    ai = 0
    bi = 0
    dist = L
    while (True):
        dist = min(dist, abs(A[ai] - B[bi]))
        if ai == N-1 and bi == N-1:
            break
        elif ai == N-1:
            bi += 1
        elif bi == N-1:
            ai += 1
        else:
            if abs(A[ai + 1] - B[bi]) < abs(A[ai] - B[bi + 1]):
                ai += 1
            else:
                bi += 1
    #
    ans = L * 2 + dist * 2
    print(ans)


# sol1()


def sol2():
    C = A + [2*L - a for a in A][::-1]
    # print(C)
    # C = C + C[::-1]
    left = 0
    right = 0
    ans = float('inf')

    while right < len(C):
        # print(left, right, C[left], C[right])
        ans = min(ans, abs(C[right] - C[left]-L))
        while C[right]-C[left] > L:  # 条件を満たすまでlを増やす
            # 現在のleftの値を消す前に条件を更新:
            left += 1  # leftを増やす
            ans = min(ans, abs(C[right] - C[left]-L))
        right += 1  # rightを増やす
    print(L*2+ans*2)


sol2()

###### 2022年 9月 4日 日曜日 21時00分10秒 JST ######
import random
m = 0


def main(l=None):
    if l is None:
        n = int(input())
        P = list(map(int, input().split()))
    else:
        P = l

    sP = sorted(P)

    d = {}
    for i, sp in enumerate(sP):
        d[sp] = i % 2
    ans = []

    o_e = []  # 偶数番目の奇数
    e_o = []  # 奇数番目の偶数
    for i, p in enumerate(P):
        if i % 2 == 0:
            if d[p] == 1:
                o_e.append(i)
        else:
            if d[p] == 0:
                e_o.append(i)

    print(o_e, e_o)
    print(P)
    dd = [i for i in range(len(P))]
    for i in range(len(o_e)):
        e = o_e[i]  # 号数番目の奇数
        o = e_o[i]  # 奇数番目の偶数
        while abs(o-e) != 1:
            if o > e:
                # print("B", o-1)
                ans.append((("B", o-1)))
                P[o-2], P[o] = P[o], P[o-2]
                if o-2 < 0:
                    raise Exception("o-2<0")
                print(P)
                o -= 2
            else:
                # print("B", o+1)
                ans.append((("B", o+1)))

                P[o], P[o+2] = P[o+2], P[o]

                print(P)
                o += 2
        if o > e:
            ans.append((("A", e+1)))
        else:
            ans.append((("A", o+1)))

        P[e], P[o] = P[o], P[e]

        print(P)

    def bubbleSort_odd(A):
        count = 0
        for i in range(len(A)):
            for j in range(len(A)-1, i, -1):
                if A[j] < A[j-1]:
                    A[j], A[j-1] = A[j-1], A[j]
                    print(A)
                    count += 1
                    ans.append((("B", 2*j)))

        return count

    def bubbleSort_even(A):
        count = 0
        for i in range(len(A)):
            for j in range(len(A)-1, i, -1):
                if A[j] < A[j-1]:
                    A[j], A[j-1] = A[j-1], A[j]
                    count += 1
                    print(A)
                    ans.append((("B", 2*(j-1)+1)))

        return count

    # print(P)

    o_A = []
    e_A = []
    for i, a in enumerate(P):
        if i % 2 == 0:
            e_A.append(a)
        else:
            o_A.append(a)

    print(e_A, o_A)

    bubbleSort_even(e_A)
    bubbleSort_odd(o_A)
    print(len(ans))
    for a in ans:
        if a[0] == "A":
            if not 1 <= a[1] <= 399:
                raise Exception("A")
        else:
            if not 1 <= a[1] <= 398:
                raise Exception("B")
        print(*a)
    global m
    m = max(len(ans), m)
    return ans


# for i in range(300):
#     S = [i for i in range(8)]
#     random.shuffle(S)
#     # print(400)
#     print("""sumary_line""",    S)
#     oS = S[::]
#     ans = main(S)
#     print("""sumary_line2""",    oS)
#     S = oS
#     # n = int(input())
#     for ab, x in ans:
#         x = int(x)
#         if ab == "A":
#             S[x-1], S[x] = S[x], S[x-1]
#         else:
#             S[x-1], S[x+1] = S[x+1], S[x-1]

#     if S != sorted(S):
#         print("だめ", S)
#         raise Exception("WA")


# print(m)
main()

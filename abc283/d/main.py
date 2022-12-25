###### 2022年 12月24日 土曜日 21時00分19秒 JST ######

import sys
from bisect import (bisect, bisect_left, bisect_right, insort, insort_left,
                    insort_right)
from collections import deque

S = input()

di = {}
di_rev = {}
d = deque()

# alphabet_index = []
for i, s in enumerate(S):
    if s == "(":
        d.append(i)
    elif s == ")":
        if len(d) == 0:
            print("No")
            exit()
        di[i] = d.pop()
        di_rev[di[i]] = i

# print(di)
# print(di_rev)
'''
bisect(A,x) #ソートされたリストAにソートを崩さずに値xを挿入するとき、xの入るべきインデックスを返す。
bisect_left(A,x) #リストAに値xを入れ、xが複数になるとき、一番左の値xのインデックスを返す。
bisect_right(A,x) #リストAに値xを入れ、xが複数になるとき、一番右の値xのインデックスを返す(bisect.bisectと同じ)。
insort(A,x) #リストAに含まれるxのうち、どのエントリーよりも後ろにxをO(N)で挿入する。
'''

sys.setrecursionlimit(10**9)


def check(left, right, ng):
    pre_right = right
    # print(left, right, ng)
    new_ng = ng.copy()
    # if right in di:
    #     if di[right] == left:
    #         left += 1
    #         right -= 1
    i = left
    # print(left, right, ng)
    while i <= right:
        if S[i] == "(":
            if i == left:
                i += 1
                continue
            pre_i = i
            assert i in di_rev
            i = di_rev[i]
            if check(pre_i, i, new_ng) == False:
                return False
        elif S[i] == ")":
            return True
        else:
            if S[i] in new_ng:
                return False
            new_ng.add(S[i])
        i += 1
    return True


if check(0, len(S) - 1, ng=set()) == False:
    print("No")
else:
    print("Yes")


# a_z = [True for _ in range(26)]

# for i, s in enumerate(S):
#     if s == "(":
#         pass
#     elif s == ")":
#         st = di[i]
#         st_ind = bisect_left(alphabet_index, (st, "a"))
#         end_ind = bisect_left(alphabet_index, (i, "z"))
#         print(st_ind, end_ind, alphabet_index)
#         for j in range(st_ind, end_ind):
#             # a_z[alphabet_index[j][1]] = False
#             print(alphabet_index[j])
#         print()
#     if s == "?":
#         a_z[i] = False

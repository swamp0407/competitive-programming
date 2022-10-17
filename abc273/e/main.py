###### 2022年 10月15日 土曜日 21時00分20秒 JST ######
import sys

input = sys.stdin.readline
q = int(input())


class Node:
    def __init__(self, val, par):
        self.val = val
        self.par = par


start = Node(-1, 0)
v = 0
ans = []
mp = {}

vec = [start]

for i in range(q):
    query = input()
    type_ = "DELETE"
    if query[0] != "D":
        type_, x = query.split()
        x = int(x)

    if type_ == "ADD":
        vec.append(Node(x, v))
        v = len(vec) - 1
    elif type_ == "DELETE":
        v = vec[v].par
    elif type_ == "SAVE":
        mp[x] = v
    else:
        if x in mp:
            v = mp[x]
        else:
            v = 0
    ans.append(vec[v].val)
print(*ans)

###### 2023年 1月 7日 土曜日 21時00分20秒 JST ######
import string

n = int(input())
t = input()
rt = t[::-1]


"""
h1_1 = RollingHash(t1, 41, 10**9 + 9)
rh2_2 = RollingHash(t2_2, 41, 10**9 + 9)

for i in range(n+1):
    h1_1 = rh1_1.get(0,i)
get(0,3)とするとS[0:3](S[0],S[1],S[2])のハッシュ値を返す
get(1,3)とするとS[1:3]のハッシュ値を返す
閉区間
"""


class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod


ht = RollingHash(t, 41, 10**9 + 9)
hhr = RollingHash(rt, 41, 10**9 + 9)

for i in range(n+1):
    if ht.get(0, i) == hhr.get(n-i, n) and ht.get(i, n) == hhr.get(0, n-i):
        print(t[i:i+n][::-1])
        print(i)
        exit()
print(-1)

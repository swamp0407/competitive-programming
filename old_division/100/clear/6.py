# 19:04 #19:27 python 通らなかったけどpypyだと通った。
n = int(input())
s = input()


def check(s, i, j, k):
    ii = 0
    jj = 0
    for l in range(len(s)):
        if ii == 1:
            if jj == 1:
                if s[l] == str(k):
                    return 1
            elif s[l] == str(j):
                jj = 1
        elif s[l] == str(i):
            ii = 1
    return 0


sum = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            sum += check(s, i, j, k)


print(sum)

n = int(input())
A = list(map(int, input().split()))
l = [0]*50
for s in A:
    b = list(bin(s))
    b = b[::-1]
    for ii, ss in enumerate(b):
        if ss == "b":
            break
        if ss == "1":
            l[ii] = (l[ii]+1) % 2
e = 1
num = 0
for i in range(50):
    num += l[i]*e
    e = e*2
for s in A:
    print(s ^ num)

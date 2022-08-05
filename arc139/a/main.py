n = int(input())

T = list(map(int, input().split()))


S = [0] * (100000+200)
value = 0
tmp = 0
for i, t in enumerate(T):
    flag = 0
    tmp = value
    s = 0
    # print(value)
    for j in range(100000+200):
        if j < t:
            if S[j] == 1:
                tmp -= 2**j
            S[j] = 0
        elif j == t:
            if S[j] == 0:
                S[j] = 1
                tmp += 2**j
            break
    if tmp > value:
        value = tmp
        continue
    t = t+1
    while True:
        if S[t] == 0:
            S[t] = 1
            tmp += 2**t
            break
        else:
            S[t] = 0
            tmp -= 2**t
            t = t+1
    value = tmp

print(value)

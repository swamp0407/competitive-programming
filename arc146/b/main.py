###### 2022年 8月20日 土曜日 21時00分17秒 JST ######

n, m, k = map(int, input().split())
A = list(map(int, input().split()))


max_a = max(A)

# max_i = 0
# for i in range(31):
#     if max_a >= 2**i:
#         max_i = i
#     else:
#         break
x = 11
remain = [[0] * (x) for _ in range(n)]

for i in range(n):
    abin = bin(A[i])[2:]
    # print(abin)
    for j in range(x):
        if len(abin) <= j:
            remain[i][j] = 2**(j) - A[i]
        elif abin[-j-1] == "1":
            remain[i][j] = 0
        else:
            # print(A[i], j, "abin", abin[-j-1:])
            remain[i][j] = 2 ** (j) - int(abin[-j-1:], 2)


remain_n = [[] for _ in range(x)]

for i in range(n):
    for j in range(x):
        remain_n[j].append(remain[i][j])


for i in range(x):
    remain_n[i].sort()
print(remain)
print(remain_n)
s = 0
for i in range(x-1, -1, -1):
    if sum(remain_n[i][:k]) > m:
        continue
    else:
        s = i
        break


s_1 = []
s_0 = []
for i in range(n):
    abin = bin(A[i])[2:]
    # print(abin)
    if len(abin) <= s:
        s_0.append(A[i])
    elif abin[-s-1] == "1":
        s_1.append(A[i])
    else:
        s_0.append(A[i])

print(s_1)
print(s_0)

d = m - sum(remain_n[s][:k])

s_1 = s_1 + [2**s]*(k-len(s_1))
print(s_1, d)

#  abin = bin(A[i])[2:]
# print(abin)
#   for j in range(x):
#        if len(abin) <= j:
#             remain[i][j] = 2**(j) - A[i]
#         elif abin[-j-1] == "1":
#             remain[i][j] = 0
#         else:
#             # print(A[i], j, "abin", abin[-j-1:])
#             remain[i][j] = 2 ** (j) - int(abin[-j-1:], 2)
# if d >= k:
#     s += 1
#     ans = 2 ** (s+1) - 1
#     d = d - k
ans = 2**s
for f in range(s-1, -1, -1):
    c = 0
    for ss in s_1:
        abin = bin(ss)[2:]
        if abin[-f-1] == "1":
            continue
        else:
            c += 2 ** (f) - int(abin[-f-1:], 2)
    if d >= c:
        ans += 2 ** (f)
        d -= c
print(ans)

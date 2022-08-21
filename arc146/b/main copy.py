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
x = 4
remain = [[0] * (x) for _ in range(n)]

for i in range(n):
    abin = bin(A[i])[2:]
    # print(abin)
    for j in range(x):
        if len(abin) <= j:
            remain[i][j] = 2**(j+1) - 1 - A[i]
        else:
            # print("abin", abin[j:])
            remain[i][j] = 2 ** (j+1) - 1 - int(abin[-j-1:], 2)


remain_n = [[] for _ in range(x)]

for i in range(n):
    for j in range(x):
        remain_n[j].append(remain[i][j])


for i in range(x):
    remain_n[i].sort()
ans = 0
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
    elif abin[s] == "1":
        s_1.append(A[i])
    else:
        s_0.append(A[i])

print(s_1)
print(s_0)

d = m - sum(remain_n[s][:k])
if d >= k:
    s += 1
    ans = 2 ** (s+1) - 1
    d = d - k
    for f in range(i, 0, -1):
        if d >= k * 2**f:
            ans += 2 ** f
            d -= k * 2**f
else:
    ans = 2 ** (i+1) - 1
print(ans)

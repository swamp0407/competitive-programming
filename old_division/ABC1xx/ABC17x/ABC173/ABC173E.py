from heapq import heappush
n, k = map(int, input().split())

A = list(map(int, input().split()))
mod = 10**9+7
l = []

for a in A:
    if a < 0:
        heappush(l, [a, a, -1])
    else:
        heappush(l, [-a, a, 1])
mcount = 0
comp = 0
mflag = 1
pflag = 2
kouhom = 0
kouhop1 = 0
kouhop2 = 0

for i, m in enumerate(l):
    if i < k:
        if m[2] == -1:
            lastm = i
            mcount += 1
    if i == k-1:
        if mcount % 2 == 0:
            comp = 1
            break
    if i >= k:
        if m[2] == -1 and mflag:
            kouhom = i
            mflag = 0
        if m[2] == 1 and pflag:
            if pflag == 2:
                kouhop2 = i
            elif pflag == 1:
                kouhop1 = i
            kouhop = i
            pflag -= 1
        if mflag == 0 and pflag == 0:
            break

ans = 1
if comp == 1:
    for i in range(k-1):
        ans = ans*l[i][1] % mod
    print(ans)
    exit()
if mflag == 0 and pflag != 0:
    s = l[kouhom][1]*l[lastm][1]

s = max(l[kouhom][1]*l[lastm][1], l[kouhop1][1]*l[kouhop2][1])
for i in range(k):
    if i == lastm:
        continue
    ans = ans*l[i][1] % mod
ans = ans*s % mod
print(ans)
exit()

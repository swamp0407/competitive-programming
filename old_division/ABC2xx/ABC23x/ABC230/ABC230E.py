import math
n = int(input())
ans = 0
s = 0
for i in range(1, int(n**0.5)+10):
    if i*i > n:
        break
    ans += n//i
    s = i

for i in range(1, s+1):
    if i == s:
        ans += i * (n//i-(s))
        break
    count = (n//i - n//(i+1))
    ans += i * count
print(ans)

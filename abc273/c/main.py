###### 2022年 10月15日 土曜日 21時00分19秒 JST ######
import bisect

n = int(input())

A = list(map(int, input().split()))
B = list(set(A))

B.sort()
ans = [0] * n
for i in range(n):
    ans[len(B)-bisect.bisect_right(B, A[i])] += 1

for i in range(n):
    print(ans[i])

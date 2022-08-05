# 2247

n = int(input())
nums = [int(c) for c in str(n)]
nums.reverse()
a = [0]*2019
a[0] = 1
now = 0
pow10 = [1]*len(nums)
for i, num in enumerate(nums):
    if i < len(nums)-1:
        pow10[i+1] = pow10[i]*10 % 2019
for i, num in enumerate(nums):
    now = (now+num*pow10[i]) % 2019
    a[now] += 1
sum = 0
for i in range(2019):
    sum += a[i]*(a[i]-1)//2
print(sum)

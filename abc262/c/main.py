###### 2022年 7月31日 日曜日 21時00分22秒 JST ######

n = int(input())

A = list(map(int, input().split()))

IND = [0]*(n+1)
cumsum = [0]*(n+1)
for i, a in enumerate(A):
    a = a-1
    IND[a] = i
    if i == a:
        cumsum[i] = 1

rcumsum = cumsum[::-1]
for i in range(n+1):
    if i == 0:
        continue
    rcumsum[i] = rcumsum[i-1] + rcumsum[i]

cumsum = rcumsum[::-1]

# print(cumsum)
# print(IND)

ans = 0
for i in range(n):
    a = A[i]-1
    if a == i:
        ans += cumsum[i+1]
        # print(a, i+1)
    elif A[a]-1 == i:
        if i < a:
            ans += 1
        # print("a", a, i+1)


print(ans)

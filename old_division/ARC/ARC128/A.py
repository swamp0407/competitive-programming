n = int(input())
A = list(map(int, input().split()))

status = 1  # 1 金 0 銀
ans = []
for i in range(n):
    if i == n-2:
        if status:
            if A[i] > A[i+1]:
                ans.append(1)
                ans.append(1)
            else:
                ans.append(0)
                ans.append(0)
        else:
            if A[i] < A[i+1]:
                ans.append(1)
                ans.append(0)
            else:
                ans.append(0)
                ans.append(1)

        break
    if status:
        if A[i] > A[i+1]:
            status = 0
            ans.append(1)
        else:
            ans.append(0)
    else:
        if A[i] < A[i+1]:
            status = 1
            ans.append(1)
        else:
            ans.append(0)

print(*ans)

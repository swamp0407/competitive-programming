n = int(input())
A = list(map(int, input().split()))
par = {i: i for i in range(1, n+1)}


def cal(par, A):
    sum = 0
    for i in range(1, n+1):
        sum = sum+A[i-1]*abs(par[i]-i)
    return sum


print(cal(par, A))

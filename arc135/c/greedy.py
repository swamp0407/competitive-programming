import random


# n = int(input())

# A = list(map(int, input().split()))


def cul(a, B, n):
    for i in range(n):
        B[i] ^= a


def many(A, n):
    ans = 0

    for i in range(n):
        B = A[::]

        for j in range(n):
            B[j] ^= A[i]
        for j in range(500):
            cul(B[random.randint(0, n-1)], B, n)
            ans = max(ans, sum(B))

    print(A, ans)


for i in range(1, 30):
    many(list(range(i)), i)

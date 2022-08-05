n = int(input())


for i in range(n):
    A = list(map(int, input().split()))
    A.sort()
    ans = float("inf")
    # rとg
    r, g, b = A
    if (g-r) % 3 == 0:
        ans = g
        # gとb
    if (b-g) % 3 == 0:
        ans = min(ans, b)
        # rとb
    elif (b-r) % 3 == 0:
        ans = min(ans, b)

    if ans == float("inf"):
        print(-1)
    else:
        print(ans)

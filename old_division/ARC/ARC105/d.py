t = int(input())


for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    if n % 2 == 1:
        print("Second")
        continue
    A = sorted(A)
    ok = 1
    for i in range(len(A)//2):
        if A[2*i] == A[2*i+1]:
            ok = 1
        else:
            ok = 0
            break
    if ok:
        print("Second")
    else:
        print("First")

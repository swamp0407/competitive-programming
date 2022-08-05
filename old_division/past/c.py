a, r, n = map(int, input().split())

present = a

if r == 1:
    if a > 10**9:
        print("large")
        exit()
    print(a)
    exit()
for i in range(n-1):
    if present > 10**9:
        print("large")
        exit()
    present *= r
if present > 10**9:
    print("large")
    exit()
print(present)

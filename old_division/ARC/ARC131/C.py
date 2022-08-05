n = int(input())
A = list(map(int, input().split()))

a = 0
print(A)
for i in A:
    a ^= i
    print(bin(a))

print(a)
if a in A:
    print("Win")
else:
    print("Lose")

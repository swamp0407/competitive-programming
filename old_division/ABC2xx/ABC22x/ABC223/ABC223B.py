n = input()


s = len(n)

ansmax = n
ansmin = n

for i in range(s):
    n = n[-1] + n[:-1]
    if n >= ansmax:
        ansmax = n
    if n <= ansmin:
        ansmin = n


print(ansmin)
print(ansmax)

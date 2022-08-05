s = input()
t = input()


ns = len(s)
nt = len(t)

nux = 0
for i in range(1000):
    count = 0
    if i+nt-1 >= ns:
        break
    for j in range(nt):
        if s[i+j] == t[j]:
            count += 1

    nux = max(nux, count)

print(nt-nux)

a = input()


s = {}

low = 0
up = 0
da = 0
for l in a:
    if l.islower():
        low = 1
    if l.isupper():
        up = 1

    if s.get(l):
        da = 1

    s[l] = 1

if not da and low and up:
    print("Yes")
else:
    print("No")

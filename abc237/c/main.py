

oword = input()
count = 0
for s in oword:
    if s == "a":
        count += 1
    else:
        break

word = oword.rstrip("a")
if str(word) == str(word)[::-1]:
    pass
else:
    if oword[-count:] == "a"*count:
        word = word.lstrip("a")

if str(word) == str(word)[::-1]:
    print("Yes")
else:
    print("No")

s = int(input())

num = [0]*20

for i in str(s):
    num[int(i)] += 1

if s < 100:
    if s % 8 == 0:
        print("Yes")
        exit()
    if len(list(str(s))) == 1:
        print("No")
        exit()
    if (int(list(str(s))[1])*10+int(list(str(s))[0])) % 8 == 0:
        print("Yes")
        exit()

if num[2] >= 1:
    if num[1] >= 1:
        if num[1] >= 2 or num[3] or num[5] or num[7] or num[9]:
            print("Yes")
            exit()
    elif num[5] >= 1:
        if num[1] or num[3] or num[5] >= 2 or num[7] or num[9]:
            print("Yes")
            exit()
    elif num[9] >= 1:
        if num[1] or num[3] or num[5] or num[7] or num[9] >= 2:
            print("Yes")
            exit()
    elif num[3]:
        if num[2] >= 2 or num[4] or num[6] or num[8]:
            print("Yes")
            exit()
    elif num[7]:
        if num[2] >= 2 or num[4] or num[6] or num[8]:
            print("Yes")
            exit()

elif num[4] >= 1:
    if num[4] >= 2:
        if num[1] or num[3] or num[5] or num[7] or num[9]:
            print("Yes")
            exit()
    elif num[8] >= 1:
        if num[1] or num[3] or num[5] or num[7] or num[9]:
            print("Yes")
            exit()
    elif num[2] >= 1:
        if num[2] >= 2 or num[4] >= 2 or num[6] or num[8]:
            print("Yes")
            exit()
    elif num[6]:
        if num[2] >= 1 or num[4] >= 2 or num[6] >= 2 or num[8]:
            print("Yes")
            exit()


elif num[6] >= 1:
    if num[1] >= 1:
        if num[2] >= 1 or num[4] or num[6] >= 2 or num[8]:
            print("Yes")
            exit()
    elif num[5] >= 1:
        if num[2] >= 1 or num[4] or num[6] >= 2 or num[8]:
            print("Yes")
            exit()
    elif num[9] >= 1:
        if num[2] >= 1 or num[4] or num[6] >= 2 or num[8]:
            print("Yes")
            exit()
    elif num[3]:
        if num[1] >= 1 or num[3] >= 2 or num[5] or num[7] or num[9]:
            print("Yes")
            exit()
    elif num[7]:
        if num[1] >= 1 or num[3] or num[5] or num[7] >= 2 or num[9]:
            print("Yes")
            exit()
elif num[8] >= 1:
    if num[2] >= 1:
        if num[1] or num[3] or num[5] or num[7] or num[9]:
            print("Yes")
            exit()
    elif num[6] >= 1:
        if num[1] or num[3] or num[5] or num[7] or num[9]:
            print("Yes")
            exit()
    elif num[4] >= 1:
        if num[2] >= 1 or num[4] >= 2 or num[6] or num[8] >= 2:
            print("Yes")
            exit()
    elif num[8] >= 2:
        if num[2] >= 1 or num[4] >= 1 or num[6] or num[8] >= 3:
            print("Yes")
            exit()

print("No")

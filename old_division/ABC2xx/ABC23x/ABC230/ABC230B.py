S = input()


T = "oxx"*80

n = len(S)
for i in range(20):
    if S == T[i:i+n]:
        print("Yes")
        exit()

print("No")

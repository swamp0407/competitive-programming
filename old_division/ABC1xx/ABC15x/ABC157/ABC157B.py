S = [list(map(int, input().split())) for _ in range(3)]
s = []
for i in range(3):
    for j in range(3):
        s.append(S[i][j])
n = int(input())
a = [int(input()) for i in range(n)]
if (s[0]in a and s[1] in a and s[2] in a)or(s[3]in a and s[4] in a and s[5] in a)or(s[6]in a and s[7] in a and s[8] in a)or(s[0]in a and s[3] in a and s[6] in a)or(s[4]in a and s[1] in a and s[7] in a)or(s[2]in a and s[5] in a and s[8] in a)or(s[0]in a and s[4] in a and s[8] in a)or(s[2]in a and s[4] in a and s[6] in a):
    print("Yes")
else:
    print("No")

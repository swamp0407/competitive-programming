a, b, c, d = map(int, input().split())
s = a+b+c+d

if a*2 == s or b*2 == s or c*2 == s or d*2 == s:
    print("Yes")
elif (a+b)*2 == s or (a+c)*2 == s or (a+d)*2 == s:
    print("Yes")
else:
    print("No")

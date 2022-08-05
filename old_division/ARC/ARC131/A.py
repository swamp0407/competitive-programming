a = int(input())
b = int(input())

ans = ""
if b == 1:
    ans = "5"+str(a)
elif b % 2 == 1:
    ans = str(b//2)+"5"+str(a)
else:
    ans = str(b//2)+"0"+str(a)

print(ans)

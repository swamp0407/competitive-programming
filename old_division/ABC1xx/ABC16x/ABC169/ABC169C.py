a, b = map(str, input().split())
a = int(a)
b1 = int(b[0])
b2 = int(b[2])
b3 = int(b[3])

print(int(a*b1*100+a*b2*10+a*b3)//100)

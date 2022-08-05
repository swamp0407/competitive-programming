n=input()

d0=0
d1=0
d2=0
for i in list(n):
    d=int(i)
    if d%3==0:
        d0+=1
    elif d%3==1:
        d1+=1
    elif d%3==2:
        d2+=1
if d0 == 0 and ((d1<=2 and d2<=0)  or (d1<=1 and d2<=0) or (d1<=0 and d2<=2)):
    print(-1)
    exit()

s1=d1-d1//3*3
s2=d2-d2//3*3
s=s1+s2
ans=0
if s%3==0:
    print(0)
    exit()
if s%3==1 and d1>=1:
    print(1)
    exit()
elif s%3==2 and d2>=1:
    print(1)
    exit()
elif s%3==2 and d1>=2:
    print(2)
    exit()
elif s%3==1 and d2>=2:
    print(2)
    exit()
else:
    print(d1+d2)
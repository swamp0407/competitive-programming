n,m=map(int,input().split())

T=[]
A=[]
for i in range(n):
    l,r=map(int,input().split())
    T.append([r,l])
    A.append([l,r])

T.sort()
A.sort()
print(T)
print(A)
nux=0
tcount=0
for t in T:
    tnux=t[1]
    if nux>tnux:
        continue
    nux=t[0]
    tcount+=1

nux=0
acount=0
for t in A:
    tnux=t[0]
    if nux>tnux:
        continue
    nux=t[1]
    acount+=1
print(tcount-acount,m)



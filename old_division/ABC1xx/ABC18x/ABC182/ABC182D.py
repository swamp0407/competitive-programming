n=int(input())
A=list(map(int,input().split()))

B=[0]*n
B[0]=A[0]
for i,a in enumerate(A):
    if i==0:
        continue
    B[i]+=B[i-1]+a

nin=-float("inf")
num=0
idxs=[]
nax=0
for i,b in enumerate(B):
    num+=b
    if nin <num:
        nin=num
        idxs=[i]
    elif nin == num:
        idxs.append(i)
if nin<0:
    print(0)
    exit()
for idx in idxs:
    if idx==n-1:
        print(nin)
        exit()
    n=max(B[:idx])
    nax=max(nax,nin+n)
print(nax)

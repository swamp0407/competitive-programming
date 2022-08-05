n=int(input())
A=list(map(int,input().split()))
ans=2
nux=0
for i in range(2,1001):
    tmp=0
    for a in A:
        if a%i==0:
            tmp+=1

    if tmp>nux:
        nux=tmp
        ans=i
print(ans)

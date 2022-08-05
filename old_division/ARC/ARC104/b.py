n,s=map(str,input().split())
n=int(n)
ans=0
dic={}
a=[0]*(n+1)
t=[0]*(n+1)
c=[0]*(n+1)
g=[0]*(n+1)


for i in range(1,n+1):
    if s[i-1]=="A":
        a[i]=a[i-1]+1
        t[i]=t[i-1]
        c[i]=c[i-1]
        g[i]=g[i-1]
    if s[i-1]=="T":
        a[i]=a[i-1]
        t[i]=t[i-1]+1
        c[i]=c[i-1]
        g[i]=g[i-1]
    if s[i-1]=="C":
        a[i]=a[i-1]
        t[i]=t[i-1]
        c[i]=c[i-1]+1
        g[i]=g[i-1]
    if s[i-1]=="G":
        a[i]=a[i-1]
        t[i]=t[i-1]
        c[i]=c[i-1]
        g[i]=g[i-1]+1

for i in range(1,n):
    r=i
    l=i+1
    while l<=n:
        if a[l]-a[r-1]==t[l]-t[r-1] and c[l]-c[r-1]==g[l]-g[r-1]:
            ans+=1
        l+=1
print(ans)


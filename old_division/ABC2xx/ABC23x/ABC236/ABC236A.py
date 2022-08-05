S = list(input())
n, m = map(int, input().split())


t = S[n-1]
s = S[m-1]
S[n-1] = s
S[m-1] = t

print(*S, sep="")

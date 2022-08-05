mod = pow(10, 9)+7
N, K = map(int, input().split())
sum = 0
for i in range(K, N+2):
    sum = sum+i*(2*N+1-i)/2.0 - 1/2.0*i*(i-1)+1
    sum = sum % mod

print(int(sum))

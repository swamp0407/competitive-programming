n = int(input())
A = list(map(int, input().split()))


now = 1000
kabu = 0
amari = 1000

for i, a in enumerate(A):
    now = max(kabu*a+amari, now)
    kabu = now//a
    amari = now-a*kabu

print(now)

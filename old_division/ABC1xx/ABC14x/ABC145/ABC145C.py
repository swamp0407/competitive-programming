# 12:03
import itertools
import math
n = int(input())

cities = [list(map(int, input().split())) for _ in range(n)]
a = []
for i in range(n):
    a.append(i)
a = list(itertools.permutations(a))
sum = 0
for city in a:
    for i in range(n-1):
        sum += ((cities[city[i+1]][0]-cities[city[i]][0])**2 +
                (cities[city[i+1]][1]-cities[city[i]][1])**2)**0.5
print(sum/math.factorial(n))

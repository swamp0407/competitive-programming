from collections import Counter
n = int(input())
m = list(map(int, input().split()))


c = Counter(m)

for k, v in c.items():
    if v % 4 != 0:
        print(k)
        break

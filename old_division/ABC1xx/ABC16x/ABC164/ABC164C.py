n = int(input())
s = []
for i in range(n):
    s.append(input())
nums_unique = list(set(s))
print(len(nums_unique))

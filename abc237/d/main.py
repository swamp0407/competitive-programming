N = int(input())
S = input()

ans = [0]
prev = 0
for i, s in enumerate(S):
    if s == "R":
        prev += 1
        ans.insert(prev, i+1)
        print(prev)
    else:
        ans.insert(prev, i+1)
        print(prev)


print(*ans)

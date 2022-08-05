x1, y1, x2, y2 = map(int, input().split())


# if (x1-x2) > 5 or (y1-y2) > 5:
#     print("No")
#     exit()

A = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2)]
ans = []
for dx, dy in A:
    ans.append((x1+dx, y1+dy))

for dx, dy in A:
    if (x2+dx, y2+dy) in ans:
        print("Yes")
        exit()


print("No")

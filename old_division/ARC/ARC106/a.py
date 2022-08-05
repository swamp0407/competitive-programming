n=int(input())

for i in range(1,100):
    s=3**i
    if s>n:
        break
    for j in range(1,100):
        q=5**j
        if q >n:
            break
        if q+s ==n:
            print(i,j)
            exit()

print(-1)
